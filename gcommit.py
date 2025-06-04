import git
import os
import sys
import google.generativeai as genai
import time
import threading
import argparse
import subprocess
import re

model_name = "gemini-1.5-flash-002"

class LoadingSpinner:
    """Animated loading spinner"""
    def __init__(self, message="Loading"):
        self.spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.message = message
        self.spinning = False
        self.thread = None
    
    def spin(self):
        while self.spinning:
            for char in self.spinner_chars:
                if not self.spinning:
                    break
                print(f"\r {char} {self.message}...", end="", flush=True)
                time.sleep(0.1)
    
    def start(self):
        self.spinning = True
        self.thread = threading.Thread(target=self.spin)
        self.thread.start()
    
    def stop(self):
        self.spinning = False
        if self.thread:
            self.thread.join()
        print("\r" + " " * (len(self.message) + 10), end="\r")  # Clear line

def print_banner():
    """Display minimal and professional banner"""
    print("\n┌─────────────────────────────────────────────────────────┐")
    print("│ 🚀 GCOMMIT - AI Git Commit Generator                    │")
    print("└─────────────────────────────────────────────────────────┘")

def print_status(message, status_type="info"):
    """Display status messages with minimal format"""
    icons = {
        "info": " • ",
        "success": " ✓ ",
        "error": " ✗ ",
        "warning": " ⚠ ",
        "loading": " ⋯ "
    }
    print(f"{icons.get(status_type, ' • ')}{message}")

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="AI-powered Git commit message generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  gcommit                           # Normal commit
  gcommit --push origin main        # Commit and push to origin/main
  gcommit --push upstream dev       # Commit and push to upstream/dev
  gcommit -p origin feature/login   # Commit and push (short form)
        """
    )
    
    parser.add_argument(
        '--push', '-p',
        nargs=2,
        metavar=('REMOTE', 'BRANCH'),
        help='Automatically push after commit (e.g., --push origin main)'
    )
    
    return parser.parse_args()

def check_ssh_agent():
    """Check if SSH agent is running and has keys loaded"""
    try:
        # Check if SSH agent is running
        ssh_auth_sock = os.environ.get('SSH_AUTH_SOCK')
        if not ssh_auth_sock:
            return False, "SSH agent not running"
        
        # Check if SSH agent has keys loaded
        result = subprocess.run(['ssh-add', '-l'], capture_output=True, text=True)
        if result.returncode == 0:
            return True, "SSH keys loaded"
        elif result.returncode == 1:
            return False, "No SSH keys loaded"
        else:
            return False, "SSH agent error"
            
    except FileNotFoundError:
        return False, "ssh-add command not found"
    except Exception as e:
        return False, f"SSH check error: {e}"

def is_ssh_remote(repo, remote_name):
    """Check if remote uses SSH"""
    try:
        remote = repo.remotes[remote_name]
        remote_url = list(remote.urls)[0]
        
        # Check if URL uses SSH format
        ssh_patterns = [
            r'^git@.*:.*\.git$',           # git@github.com:user/repo.git
            r'^ssh://.*@.*:.*\.git$',      # ssh://git@github.com:22/user/repo.git
            r'^.*@.*:.*\.git$'             # user@server:repo.git
        ]
        
        for pattern in ssh_patterns:
            if re.match(pattern, remote_url):
                return True, remote_url
                
        return False, remote_url
        
    except Exception as e:
        return False, f"Error checking remote: {e}"

def validate_ssh_setup(repo, remote_name):
    """Validate SSH setup for push operations"""
    try:
        is_ssh, remote_url = is_ssh_remote(repo, remote_name)
        
        if is_ssh:
            print_status(f"SSH remote detected: {remote_url}", "info")
            
            # Check SSH agent
            ssh_ok, ssh_msg = check_ssh_agent()
            if ssh_ok:
                print_status(ssh_msg, "success")
            else:
                print_status(ssh_msg, "warning")
                print_status("SSH setup suggestions:", "info")
                print("   1. Start SSH agent: eval \"$(ssh-agent -s)\"")
                print("   2. Add SSH key: ssh-add ~/.ssh/id_rsa")
                print("   3. Test connection: ssh -T git@github.com")
                return False
                
        else:
            print_status(f"HTTPS remote detected: {remote_url}", "info")
            
        return True
        
    except Exception as e:
        print_status(f"SSH validation error: {e}", "warning")
        return True  # Continue anyway

def validate_environment():
    """Validate API Key with minimal output"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print_status("GOOGLE_API_KEY not found", "error")
        print_status("Set environment variable: export GOOGLE_API_KEY=\"your-key\"", "info")
        sys.exit(1)
    
    print_status("API Key OK", "success")
    return api_key

def validate_git_repository():
    """Validate git repository with minimal output"""
    try:
        repo = git.Repo('.')
        if not repo.git.rev_parse('--is-inside-work-tree'):
            print_status("Not a valid git directory", "error")
            sys.exit(1)
            
        print_status(f"Repository: {os.path.basename(repo.working_dir)}", "success")
        return repo
        
    except git.InvalidGitRepositoryError:
        print_status("No git repository found", "error")
        print_status("Run: git init", "info")
        sys.exit(1)
    except Exception as e:
        print_status(f"Git error: {e}", "error")
        sys.exit(1)

def validate_push_parameters(repo, remote_name, branch_name):
    """Validate push parameters including SSH setup"""
    try:
        # Check if remote exists
        remotes = [remote.name for remote in repo.remotes]
        if remote_name not in remotes:
            print_status(f"Remote '{remote_name}' not found", "error")
            print_status(f"Available remotes: {', '.join(remotes)}", "info")
            return False
        
        # Check if branch exists locally
        try:
            repo.heads[branch_name]
        except IndexError:
            print_status(f"Branch '{branch_name}' not found locally", "error")
            current_branch = repo.active_branch.name
            print_status(f"Current branch: {current_branch}", "info")
            return False
        
        # Validate SSH setup
        if not validate_ssh_setup(repo, remote_name):
            print_status("SSH setup validation failed", "warning")
            response = input(" Continue anyway? [y/N]: ").strip().lower()
            if response not in ['y', 'yes']:
                return False
        
        print_status(f"Push target: {remote_name}/{branch_name}", "success")
        return True
        
    except Exception as e:
        print_status(f"Push validation error: {e}", "error")
        return False

def get_staged_changes(repo):
    """Get staged changes with concise output"""
    try:
        staged_files = repo.git.diff('HEAD', cached=True, name_only=True).splitlines()
        
        if not staged_files:
            print_status("No files staged", "warning")
            print_status("Run: git add <files>", "info")
            sys.exit(0)
        
        print_status(f"Files staged: {len(staged_files)}", "success")
        for file in staged_files[:3]:  # Maximum 3 files
            print(f"   📄 {file}")
        if len(staged_files) > 3:
            print(f"   ... and {len(staged_files) - 3} more files")
            
        diff_detail = repo.git.diff('HEAD', cached=True)
        return staged_files, diff_detail
        
    except Exception as e:
        print_status(f"Error: {e}", "error")
        sys.exit(1)

def generate_ai_commit_message(api_key, staged_files, diff_detail):
    """Generate commit message with cool loading animation"""
    try:
        # Start loading animation
        spinner = LoadingSpinner("Connecting to AI")
        spinner.start()
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name)
        
        spinner.stop()
        print_status("AI connected", "success")
        
        prompt_text = f"""
Create a concise and professional commit message based on the following changes:

FILES:
{chr(10).join(f"- {file}" for file in staged_files)}

DIFF:
{diff_detail[:1500]}

FORMAT: [type]: [short description]
TYPES: feat, fix, docs, style, refactor, test, chore
MAX: 60 characters
LANGUAGE: English

EXAMPLES:
- feat: add login system
- fix: resolve validation bug
- docs: update readme

RETURN ONLY THE COMMIT MESSAGE:
"""

        # Start generating animation
        spinner = LoadingSpinner("Generating commit message")
        spinner.start()
        
        response = model.generate_content(prompt_text)
        
        spinner.stop()
        
        if not response or not response.text:
            print_status("AI failed to generate message", "error")
            sys.exit(1)
            
        commit_message = response.text.strip().replace('"', '').replace("'", "")
        print_status("Commit message generated", "success")
        
        return commit_message
        
    except Exception as e:
        if 'spinner' in locals():
            spinner.stop()
        print_status(f"AI Error: {str(e)[:50]}...", "error")
        sys.exit(1)

def display_commit_message(commit_message):
    """Display commit message with clean format"""
    print(f"\n┌─ Commit Message ─────────────────────────────────────────┐")
    
    # Handle long messages by wrapping
    if len(commit_message) > 56:
        # Split into lines if too long
        words = commit_message.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + " " + word) <= 56:
                current_line += (" " + word if current_line else word)
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        for i, line in enumerate(lines):
            if i == 0:
                print(f"│ {line:<56} │")
            else:
                print(f"│ {line:<56} │")
    else:
        print(f"│ {commit_message:<56} │")
    
    print(f"└──────────────────────────────────────────────────────────┘")

def confirm_commit_and_push(will_push=False, remote_name=None, branch_name=None):
    """Confirmation with simple format"""
    while True:
        if will_push:
            response = input(f"\n Continue with commit and push to {remote_name}/{branch_name}? [Y/n]: ").strip().lower()
        else:
            response = input("\n Continue with commit? [Y/n]: ").strip().lower()
            
        if response in ['', 'y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print(" ⚠ Type 'y' or 'n'")

def perform_commit(repo, commit_message):
    """Perform commit with cool loading and minimal output"""
    try:
        # Cool commit animation
        spinner = LoadingSpinner("Committing changes")
        spinner.start()
        
        repo.index.commit(commit_message)
        
        spinner.stop()
        
        commit_hash = repo.head.commit.hexsha[:8]
        print_status(f"Commit successful [{commit_hash}]", "success")
        
        return True
        
    except Exception as e:
        if 'spinner' in locals():
            spinner.stop()
        print_status(f"Commit error: {e}", "error")
        return False

def perform_push(repo, remote_name, branch_name):
    """Perform git push with loading animation and SSH handling"""
    try:
        # Start push animation
        spinner = LoadingSpinner(f"Pushing to {remote_name}/{branch_name}")
        spinner.start()
        
        # Get remote
        remote = repo.remotes[remote_name]
        
        # Check if it's SSH and provide pre-push info
        is_ssh, remote_url = is_ssh_remote(repo, remote_name)
        
        # Push to remote
        push_info = remote.push(branch_name)
        
        spinner.stop()
        
        # Check push result
        if push_info:
            push_result = push_info[0]
            if push_result.flags & push_result.ERROR:
                print_status(f"Push failed: {push_result.summary}", "error")
                
                # SSH-specific error handling
                if is_ssh:
                    print_status("SSH troubleshooting:", "info")
                    print("   1. Check SSH agent: ssh-add -l")
                    print("   2. Test connection: ssh -T git@github.com")
                    print("   3. Add SSH key: ssh-add ~/.ssh/id_rsa")
                
                return False
            elif push_result.flags & push_result.UP_TO_DATE:
                print_status(f"Already up to date with {remote_name}/{branch_name}", "success")
                return True
            else:
                print_status(f"Push successful to {remote_name}/{branch_name}", "success")
                return True
        else:
            print_status("Push completed", "success")
            return True
            
    except Exception as e:
        if 'spinner' in locals():
            spinner.stop()
        
        error_msg = str(e).lower()
        print_status(f"Push error: {e}", "error")
        
        # Provide helpful suggestions based on error type
        if "authentication failed" in error_msg:
            print_status("Check your Git credentials", "info")
        elif "permission denied" in error_msg:
            if is_ssh_remote(repo, remote_name)[0]:
                print_status("SSH authentication failed", "info")
                print("   Solutions:")
                print("   1. ssh-add ~/.ssh/id_rsa")
                print("   2. ssh-keygen -t rsa -b 4096 -C 'your_email@example.com'")
                print("   3. Add public key to GitHub/GitLab")
                print("   4. Test: ssh -T git@github.com")
            else:
                print_status("Check repository permissions", "info")
        elif "host key verification failed" in error_msg:
            print_status("SSH host key verification failed", "info")
            print("   Solution: ssh-keyscan -H github.com >> ~/.ssh/known_hosts")
        elif "non-fast-forward" in error_msg:
            print_status("Try: git pull before pushing", "info")
        elif "could not read from remote repository" in error_msg:
            print_status("Repository access error", "info")
            if is_ssh_remote(repo, remote_name)[0]:
                print("   SSH troubleshooting:")
                print("   1. Test SSH: ssh -T git@github.com")
                print("   2. Check SSH key: ssh-add -l")
        
        return False

def main():
    """Main function with clean flow"""
    try:
        # Parse command line arguments
        args = parse_arguments()
        
        print_banner()
        print()
        
        # Quick validation
        api_key = validate_environment()
        repo = validate_git_repository()
        
        # Validate push parameters if provided
        will_push = args.push is not None
        if will_push:
            remote_name, branch_name = args.push
            if not validate_push_parameters(repo, remote_name, branch_name):
                sys.exit(1)
        
        staged_files, diff_detail = get_staged_changes(repo)
        
        print()
        
        # Generate and display
        commit_message = generate_ai_commit_message(api_key, staged_files, diff_detail)
        display_commit_message(commit_message)
        
        # Confirm and commit
        if confirm_commit_and_push(will_push, args.push[0] if will_push else None, args.push[1] if will_push else None):
            # Perform commit
            if perform_commit(repo, commit_message):
                print()
                
                # Perform push if requested
                if will_push:
                    if perform_push(repo, args.push[0], args.push[1]):
                        print("\n ✨ Commit and push completed!\n")
                    else:
                        print("\n ⚠ Commit succeeded but push failed\n")
                        print_status(f"Manual push: git push {args.push[0]} {args.push[1]}", "info")
                else:
                    print("\n ✨ Commit completed!\n")
            else:
                sys.exit(1)
        else:
            print_status("Cancelled", "warning")
            push_cmd = f" && git push {args.push[0]} {args.push[1]}" if will_push else ""
            print(f" Manual: git commit -m \"{commit_message}\"{push_cmd}\n")
        
    except KeyboardInterrupt:
        print("\n\n ⚠ Cancelled (Ctrl+C)\n")
        sys.exit(0)
    except Exception as e:
        print_status(f"Error: {e}", "error")
        sys.exit(1)

if __name__ == "__main__":
    main()



