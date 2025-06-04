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
- **🚀 Developer-Friendly**: Integrates seamlessly with existing Git workflow

## 📸 Demo

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

 ✨ Done!
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+**: Check with `python3 --version`
- **Git**: Check with `git --version`
- **Google Gemini API Key**: Get from [Google AI Studio](https://ai.google.com/studio)

### Installation by Platform

#### 🍎 macOS Installation (This Repository)

**Method 1: Quick Install (Recommended)**

```bash
# Clone the repository
git clone https://github.com/GhufranBkri/gcommit.git
cd gcommit

# Install dependencies
pip3 install --break-system-packages GitPython google-generativeai

# Make executable
chmod +x gcommit

# Add to PATH (add this to your ~/.zshrc or ~/.bash_profile)
export PATH="$(pwd):$PATH"
```

**Method 2: Using Virtual Environment**

```bash
# Clone and setup
git clone https://github.com/GhufranBkri/gcommit.git
cd gcommit

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x gcommit
```

#### 🐧 Linux/Ubuntu Installation

For Linux/Ubuntu users, please use the dedicated Ubuntu version:

**👉 [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu)**

This version is specifically optimized for Ubuntu/Linux systems with:

- Proper package management
- Linux-specific installation scripts
- System-wide installation support
- Distribution-specific configurations

#### 🪟 Windows Installation

For Windows users, please use the dedicated Windows version:

**👉 [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows)**

This version includes:

- Windows batch scripts
- PowerShell installation support
- Windows-specific path handling
- Executable files for easy setup

### Setup Google Gemini API Key

1. Get your API key from [Google AI Studio](https://ai.google.com/studio)
2. Set up environment variable based on your platform:

#### 🍎 macOS Setup:

```bash
# For Zsh (default on macOS)
echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc

# For Bash
echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.bash_profile
source ~/.bash_profile
```

#### 🐧 Linux/Ubuntu Setup:

Please refer to [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu) for detailed Linux-specific setup instructions.

#### 🪟 Windows Setup:

Please refer to [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows) for detailed Windows-specific setup instructions.

## 💡 Usage

1. **Stage your changes**:

   ```bash
   git add .
   # or selectively: git add file1.py file2.py
   ```

2. **Run GCommit**:

   ```bash
   gcommit
   ```

3. **Review and confirm** the AI-generated commit message

4. **Done!** Your changes are committed with a professional message

## 🎯 Features in Detail

### Conventional Commits Support

GCommit automatically generates commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks

### Smart Analysis

The AI analyzes your staged changes and generates contextually appropriate commit messages by examining:

- File modifications
- Code additions and deletions
- File types and patterns
- Change scope and impact

## 🛠️ Configuration

### Custom Model Settings

You can modify the AI model in `gcommit.py`:

```python
model_name = "gemini-1.5-flash-002"  # Default model
```

### Environment Variables

- `GOOGLE_API_KEY`: Your Google Gemini API key (required)

## 🐛 Troubleshooting

### Common Issues

**"GOOGLE_API_KEY not found"**

- Ensure you've set the environment variable correctly
- Restart your terminal after setting the variable

**"No files staged"**

- Run `git add <files>` before using gcommit
- Check `git status` to see unstaged changes

**"Not a valid git directory"**

- Ensure you're in a Git repository
- Run `git init` if needed

**Dependencies installation error on macOS**

- Use `--break-system-packages` flag with pip3
- Or use virtual environment (recommended)

### Platform-Specific Issues

**macOS Issues**: Check this repository's issues
**Linux Issues**: Check [MhmmdIchsan/gcommit-ubuntu issues](https://github.com/MhmmdIchsan/gcommit-ubuntu/issues)
**Windows Issues**: Check [Papazy/gcommit-windows issues](https://github.com/Papazy/gcommit-windows/issues)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the appropriate repository** for your platform
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. \*\*Open a Pull Request`

### Development Setup

**For macOS:**

```bash
git clone https://github.com/GhufranBkri/gcommit.git
cd gcommit
pip install -r requirements.txt
```

**For Linux/Ubuntu:**
See [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu) for development setup

**For Windows:**
See [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows) for development setup

## 📊 Project Stats

- **Language**: Python 3.7+
- **Dependencies**: GitPython, google-generativeai
- **License**: MIT
- **Platform**: Cross-platform (macOS, Linux, Windows)

## 🔗 Related Projects & Repositories

### Official Repositories:

- **macOS**: [GhufranBkri/gcommit](https://github.com/GhufranBkri/gcommit) (Main)
- **Linux/Ubuntu**: [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu)
- **Windows**: [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows)

### External Resources:

- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitPython](https://github.com/gitpython-developers/GitPython)
- [Google Generative AI](https://github.com/google/generative-ai-python)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If you find GCommit helpful, please consider:

- ⭐ Starring the repositories:
  - [Main macOS repository](https://github.com/GhufranBkri/gcommit)
  - [Ubuntu repository](https://github.com/MhmmdIchsan/gcommit-ubuntu)
  - [Windows repository](https://github.com/Papazy/gcommit-windows)
- 🐛 Reporting bugs on the appropriate platform repository
- 💡 Suggesting new features
- 🤝 Contributing to the project

## 📞 Support

### General Support:

- **Issues**: [GitHub Issues](https://github.com/GhufranBkri/gcommit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/GhufranBkri/gcommit/discussions)
- **Email**: ghufranbakrie@gmail.com

### Platform-Specific Support:

- **macOS**: [This repository](https://github.com/GhufranBkri/gcommit/issues)
- **Linux/Ubuntu**: [MhmmdIchsan/gcommit-ubuntu](https://github.com/MhmmdIchsan/gcommit-ubuntu/issues)
- **Windows**: [Papazy/gcommit-windows](https://github.com/Papazy/gcommit-windows/issues)

---

**Keywords**: git commit generator, ai commit message, conventional commits, google gemini ai, git automation, developer tools, python git tools, commit message generator, ai git helper, automated git commits, git workflow optimization

Made with ❤️ by developers, for developers across all platforms.
