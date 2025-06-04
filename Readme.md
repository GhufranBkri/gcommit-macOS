# 🚀 GCommit - AI-Powered Git Commit Message Generator

> Automatically generate professional commit messages using Google Gemini AI for macOS, Linux, and Windows

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/GhufranBkri/gcommit.svg)](https://github.com/GhufranBkri/gcommit/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/GhufranBkri/gcommit.svg)](https://github.com/GhufranBkri/gcommit/network)

**GCommit** is an intelligent Git commit message generator that uses Google Gemini AI to create professional, conventional commit messages automatically. Perfect for developers who want to maintain consistent commit history without the hassle of writing commit messages manually.

## 📱 Platform-Specific Versions

| Platform            | Repository                                                                  | Description                        |
| ------------------- | --------------------------------------------------------------------------- | ---------------------------------- |
| 🍎 **macOS**        | [GhufranBkri/gcommit](https://github.com/GhufranBkri/gcommit)               | Main repository with macOS support |
| 🐧 **Linux/Ubuntu** | [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu) | Optimized for Ubuntu/Linux systems |
| 🪟 **Windows**      | [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows)         | Windows-compatible version         |

## 🌟 Why GCommit?

- **🤖 AI-Powered**: Leverages Google Gemini AI for intelligent commit message generation
- **📝 Professional Format**: Follows Conventional Commits standard automatically
- **⚡ Fast & Simple**: One command to analyze changes and commit
- **🎨 Beautiful Interface**: Clean terminal UI with animated loading spinners
- **🔒 Secure**: Uses environment variables for API key management
- **🌍 Cross-Platform**: Works on macOS, Linux, and Windows
- **🚀 Auto-Push Support**: Commit and push in one command
- **🔄 Smart Validation**: Validates Git repository and push parameters

## 📸 Demo

### Basic Commit

```bash
$ gcommit

┌─────────────────────────────────────────────────────────┐
│ 🚀 GCOMMIT - AI Git Commit Generator                    │
└─────────────────────────────────────────────────────────┘

 ✓ API Key OK
 ✓ Repository: my-awesome-project
 ✓ Files staged: 3
   📄 src/auth.py
   📄 tests/test_auth.py
   📄 README.md

 ⠋ Generating commit message...
 ✓ Commit message generated

┌─ Commit Message ─────────────────────────────────────────┐
│ feat: add user authentication with JWT tokens           │
└──────────────────────────────────────────────────────────┘

 Continue with commit? [Y/n]: y
 ✓ Commit successful [a1b2c3d4]

 ✨ Commit completed!
```

### Commit with Auto-Push

```bash
$ gcommit --push origin main

┌─────────────────────────────────────────────────────────┐
│ 🚀 GCOMMIT - AI Git Commit Generator                    │
└─────────────────────────────────────────────────────────┘

 ✓ API Key OK
 ✓ Repository: my-awesome-project
 ✓ Push target: origin/main
 ✓ Files staged: 2

 ⠋ Generating commit message...
 ✓ Commit message generated

┌─ Commit Message ─────────────────────────────────────────┐
│ fix: resolve memory leak in user session handler        │
└──────────────────────────────────────────────────────────┘

 Continue with commit and push to origin/main? [Y/n]: y
 ✓ Commit successful [b2c3d4e5]
 ⠋ Pushing to origin/main...
 ✓ Push successful to origin/main

 ✨ Commit and push completed!
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+**: Check with `python3 --version`
- **Git**: Check with `git --version`
- **Google Gemini API Key**: Get from [Google AI Studio](https://ai.google.com/studio)

### 🍎 macOS Installation (This Repository)

#### Method 1: Quick Install (Recommended)

1. **Clone the repository**

   ```bash
   git clone https://github.com/GhufranBkri/gcommit.git
   cd gcommit
   ```

2. **Install Python dependencies**

   ```bash
   # Option A: System-wide (with override)
   pip3 install --break-system-packages GitPython google-generativeai

   # Option B: User installation (safer)
   pip3 install --user GitPython google-generativeai
   ```

3. **Make executable**

   ```bash
   chmod +x gcommit
   ```

4. **Add to PATH** (choose one method):

   **Temporary (current session only):**

   ```bash
   export PATH="$(pwd):$PATH"
   ```

   **Permanent (recommended):**

   ```bash
   # For Zsh (default on macOS)
   echo 'export PATH="/path/to/gcommit:$PATH"' >> ~/.zshrc
   source ~/.zshrc

   # For Bash
   echo 'export PATH="/path/to/gcommit:$PATH"' >> ~/.bash_profile
   source ~/.bash_profile
   ```

#### Method 2: Virtual Environment (Isolated)

1. **Clone and setup**

   ```bash
   git clone https://github.com/GhufranBkri/gcommit.git
   cd gcommit
   ```

2. **Create virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install GitPython google-generativeai
   ```

4. **Create requirements.txt**

   ```bash
   pip freeze > requirements.txt
   ```

5. **Make executable**
   ```bash
   chmod +x gcommit
   ```

**Note**: With virtual environment, you need to activate it each time:

```bash
cd /path/to/gcommit
source venv/bin/activate
```

#### Method 3: Global Symlink (Advanced)

1. **After installing with Method 1, create global symlink:**

   ```bash
   sudo ln -sf $(pwd)/gcommit /usr/local/bin/gcommit
   ```

2. **Verify installation:**
   ```bash
   which gcommit
   gcommit --help
   ```

### 🐧 Linux/Ubuntu Installation

For Linux/Ubuntu users, please use the dedicated optimized version:

**👉 [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu)**

Features include:

- APT package management integration
- Systemd service support
- Linux-specific installation scripts
- Distribution-specific configurations
- System-wide installation support

### 🪟 Windows Installation

For Windows users, please use the dedicated Windows version:

**👉 [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows)**

Features include:

- Windows batch scripts (.bat files)
- PowerShell installation support
- Windows PATH handling
- Executable files (.exe)
- Windows Defender compatibility

## 🔑 Setup Google Gemini API Key

### Step 1: Get API Key

1. Visit [Google AI Studio](https://ai.google.com/studio)
2. Sign in with your Google account
3. Create a new API key
4. Copy the generated key

### Step 2: Set Environment Variable

#### 🍎 macOS Setup:

**Option A: Permanent Setup (Recommended)**

```bash
# For Zsh (default on macOS Catalina+)
echo 'export GOOGLE_API_KEY="your-actual-api-key-here"' >> ~/.zshrc
source ~/.zshrc

# For Bash
echo 'export GOOGLE_API_KEY="your-actual-api-key-here"' >> ~/.bash_profile
source ~/.bash_profile
```

**Option B: Temporary Setup (Current session)**

```bash
export GOOGLE_API_KEY="your-actual-api-key-here"
```

**Verify Setup:**

```bash
echo $GOOGLE_API_KEY
```

#### 🐧 Linux/Ubuntu Setup:

Please refer to [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu) for detailed Linux-specific setup instructions.

#### 🪟 Windows Setup:

Please refer to [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows) for detailed Windows-specific setup instructions.

## 💡 Usage

### Basic Commands

1. **Stage your changes:**

   ```bash
   git add .                    # Stage all changes
   git add file1.py file2.py    # Stage specific files
   git add src/                 # Stage entire directory
   ```

2. **Generate commit message and commit:**

   ```bash
   gcommit
   ```

3. **Commit and push in one command:**
   ```bash
   gcommit --push origin main           # Push to origin/main
   gcommit --push upstream develop      # Push to upstream/develop
   gcommit -p origin feature/auth       # Short form
   ```

### Advanced Usage

**Check help:**

```bash
gcommit --help
```

**Examples:**

```bash
# Basic workflow
git add .
gcommit

# Commit and push workflow
git add src/
gcommit --push origin main

# Feature branch workflow
git checkout -b feature/new-auth
git add .
gcommit --push origin feature/new-auth
```

### Command Options

| Option   | Short | Description                      | Example                  |
| -------- | ----- | -------------------------------- | ------------------------ |
| `--push` | `-p`  | Commit and push to remote/branch | `gcommit -p origin main` |
| `--help` | `-h`  | Show help message                | `gcommit --help`         |

## 🎯 Features in Detail

### 🤖 AI-Powered Commit Messages

GCommit automatically generates commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 🔍 Smart Analysis

The AI analyzes your staged changes and generates contextually appropriate commit messages by examining:

- **File modifications**: What files were changed
- **Code additions and deletions**: The actual changes made
- **File types and patterns**: Understanding the context
- **Change scope and impact**: Determining the appropriate commit type

### 🚀 Auto-Push Feature

New auto-push functionality allows you to:

- Commit and push in a single command
- Validate remote and branch existence
- Handle push errors gracefully
- Provide helpful error messages

**Auto-Push Validation:**

- ✅ Checks if remote exists
- ✅ Validates branch exists locally
- ✅ Provides clear error messages
- ✅ Suggests solutions for common issues

## 🛠️ Configuration

### Custom AI Model

You can modify the AI model in `gcommit.py`:

```python
model_name = "gemini-1.5-flash-002"  # Default model
# model_name = "gemini-pro"         # Alternative model
```

### Environment Variables

| Variable         | Required | Description                |
| ---------------- | -------- | -------------------------- |
| `GOOGLE_API_KEY` | ✅ Yes   | Your Google Gemini API key |

### File Structure

```
gcommit/
├── gcommit              # Main executable script
├── gcommit.py          # Python source code
├── README.md           # This documentation
├── LICENSE             # MIT License
├── requirements.txt    # Python dependencies (if using venv)
└── .gitignore         # Git ignore rules
```

## 🐛 Troubleshooting

### Common Issues

#### ❌ "GOOGLE_API_KEY not found"

**Solution:**

```bash
# Check if variable is set
echo $GOOGLE_API_KEY

# Set the variable (replace with your actual key)
export GOOGLE_API_KEY="your-actual-api-key-here"

# Make it permanent
echo 'export GOOGLE_API_KEY="your-actual-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

#### ❌ "No files staged"

**Solution:**

```bash
# Check git status
git status

# Stage files
git add .                    # Stage all
git add specific-file.py     # Stage specific file
```

#### ❌ "Not a valid git directory"

**Solution:**

```bash
# Initialize git repository
git init

# Or navigate to existing repository
cd /path/to/your/git/repository
```

#### ❌ "Command not found: gcommit"

**Solution:**

```bash
# Check if gcommit is in PATH
which gcommit

# Add to PATH temporarily
export PATH="/path/to/gcommit:$PATH"

# Add to PATH permanently
echo 'export PATH="/path/to/gcommit:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

#### ❌ Dependencies installation error on macOS

**Solution:**

```bash
# Option 1: Use break-system-packages flag
pip3 install --break-system-packages GitPython google-generativeai

# Option 2: Use user installation
pip3 install --user GitPython google-generativeai

# Option 3: Use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install GitPython google-generativeai
```

#### ❌ Push-related errors

**Solutions:**

```bash
# Authentication failed
git config --global credential.helper store

# Permission denied
# Check repository permissions on GitHub/GitLab

# Non-fast-forward
git pull origin main  # Pull latest changes first
```

### Platform-Specific Issues

- **macOS Issues**: [Create issue](https://github.com/GhufranBkri/gcommit/issues)
- **Linux Issues**: [MhmmdIchsan/gcommit-ubuntu issues](https://github.com/MhmmdIchsan/gcommit-ubuntu/issues)
- **Windows Issues**: [Papazy/gcommit-windows issues](https://github.com/Papazy/gcommit-windows/issues)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Quick Contribution Guide

1. **Fork the appropriate repository** for your platform:

   - macOS: This repository
   - Linux: [gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu)
   - Windows: [gcommit-windows](https://github.com/Papazy/gcommit-windows)

2. **Create a feature branch:**

   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes and test them**

4. **Commit your changes:**

   ```bash
   git add .
   gcommit  # Use gcommit itself! 😄
   ```

5. **Push to your fork:**

   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**

### Development Setup

**For macOS development:**

```bash
git clone https://github.com/GhufranBkri/gcommit.git
cd gcommit
python3 -m venv venv
source venv/bin/activate
pip install GitPython google-generativeai
```

**For other platforms:**

- Linux: See [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu)
- Windows: See [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows)

## 📊 Project Stats

- **Language**: Python 3.7+
- **Dependencies**: GitPython, google-generativeai
- **License**: MIT
- **Platforms**: macOS, Linux, Windows
- **Features**: AI commit generation, auto-push, conventional commits

## 🔗 Related Projects & Repositories

### Official GCommit Repositories:

- **macOS**: [GhufranBkri/gcommit](https://github.com/GhufranBkri/gcommit) (Main)
- **Linux/Ubuntu**: [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu)
- **Windows**: [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows)

### External Resources:

- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitPython Documentation](https://github.com/gitpython-developers/GitPython)
- [Google Generative AI](https://github.com/google/generative-ai-python)
- [Google AI Studio](https://ai.google.com/studio)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If you find GCommit helpful, please consider:

- ⭐ **Starring the repositories:**
  - [Main macOS repository](https://github.com/GhufranBkri/gcommit)
  - [Ubuntu repository](https://github.com/MhmmdIchsan/gcommit-ubuntu)
  - [Windows repository](https://github.com/Papazy/gcommit-windows)
- 🐛 **Reporting bugs** on the appropriate platform repository
- 💡 **Suggesting new features**
- 🤝 **Contributing to the project**
- 📢 **Sharing with other developers**

## 📞 Support & Community

### General Support:

- **Issues**: [GitHub Issues](https://github.com/GhufranBkri/gcommit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/GhufranBkri/gcommit/discussions)
- **Email**: ghufranbakrie@gmail.com

### Platform-Specific Support:

- **macOS**: [This repository](https://github.com/GhufranBkri/gcommit/issues)
- **Linux/Ubuntu**: [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu/issues)
- **Windows**: [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows/issues)

### Community Guidelines:

- Be respectful and constructive
- Provide detailed information for bug reports
- Search existing issues before creating new ones
- Use appropriate repository for platform-specific issues

---

**Keywords**: git commit generator, ai commit message, conventional commits, google gemini ai, git automation, developer tools, python git tools, commit message generator, ai git helper, automated git commits, git workflow optimization, auto push, ai powered git

Made with ❤️ by developers, for developers across all platforms.

⭐ **Star this project if it helped you!**
