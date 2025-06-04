import git
import os
import sys
import google.generativeai as genai
import time
import threading
from datetime import datetime

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

def confirm_commit():
    """Confirmation with simple format"""
    while True:
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
        
    except Exception as e:
        if 'spinner' in locals():
            spinner.stop()
        print_status(f"Commit error: {e}", "error")
        sys.exit(1)

def main():
    """Main function with clean flow"""
    try:
        print_banner()
        print()
        
        # Quick validation
        api_key = validate_environment()
        repo = validate_git_repository()
        staged_files, diff_detail = get_staged_changes(repo)
        
        print()
        
        # Generate and display
        commit_message = generate_ai_commit_message(api_key, staged_files, diff_detail)
        display_commit_message(commit_message)
        
        # Confirm and commit
        if confirm_commit():
            perform_commit(repo, commit_message)
            print("\n ✨ Done!\n")
        else:
            print_status("Cancelled", "warning")
            print(f" Manual: git commit -m \"{commit_message}\"\n")
        
    except KeyboardInterrupt:
        print("\n\n ⚠ Cancelled (Ctrl+C)\n")
        sys.exit(0)
    except Exception as e:
        print_status(f"Error: {e}", "error")
        sys.exit(1)

if __name__ == "__main__":
    main()



