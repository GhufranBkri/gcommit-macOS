# Panduan Instalasi gcommit

Ikuti langkah-langkah berikut untuk mengatur alat gcommit.

## 1. Persiapan Awal

Sebelum memulai, pastikan Anda memiliki **Python** dan **Git** terinstal di komputer Anda.

- **Python 3.x**:
  - **Windows**: Jika belum terinstal, unduh dari [python.org](https://www.python.org). Pastikan mencentang opsi "Add Python to PATH" saat instalasi.
  - **macOS**: Python 3 mungkin sudah terinstal. Anda bisa memeriksanya dengan `python3 --version`. Jika belum, Anda bisa menginstalnya menggunakan [Homebrew](https://brew.sh/) dengan perintah `brew install python`.
- **Git**:
  - **Windows**: Unduh dari [git-scm.com](https://git-scm.com/download/win) dan ikuti instruksi default.
  - **macOS**: Git seringkali sudah terinstal atau dapat diinstal dengan Xcode Command Line Tools (`xcode-select --install`) atau melalui [Homebrew](https://brew.sh/) (`brew install git`).

Buka **Terminal** (di macOS) atau **Command Prompt/PowerShell** (di Windows) untuk menjalankan semua perintah berikut.

---

## 2. Clone Repository gcommit

Clone repository gcommit ke komputer Anda menggunakan perintah berikut:

```bash
git clone https://github.com/username/gcommit.git # Ganti dengan URL repository Anda
cd gcommit
```

> **Catatan**: Ganti `username/gcommit.git` dengan URL repository Anda yang sebenarnya.

lalu jalankan 
```pip install GitPython google-generativeai```

---

## 3. Dapatkan dan Atur Google Gemini API Key

gcommit membutuhkan API Key dari Google Gemini untuk berkomunikasi dengan model AI.

### Dapatkan API Key
1. Buka [Google AI Studio](https://ai.google.com/studio) di browser Anda.
2. Login dengan akun Google Anda.
3. Klik **"Get API key"** di bagian kiri.
4. Klik **"Create API key in new project"** dan salin key yang muncul (diawali dengan `AIza...`).

### Atur API Key sebagai Variabel Lingkungan

**Untuk Windows:**
1. Cari **"Edit the system environment variables"** di Start Menu Windows dan klik.
2. Pada jendela **System Properties**, klik tombol **Environment Variables...**.
3. Di bagian **User variables**, klik **New...**.
  - **Variable name**: `GOOGLE_API_KEY`
  - **Variable value**: Tempel API Key yang sudah disalin.
4. Klik **OK** pada semua jendela.
> **Penting**: Tutup dan buka kembali Command Prompt/PowerShell agar perubahan variabel lingkungan berlaku.

**Untuk macOS/Linux:**
1. Buka file konfigurasi shell Anda. Ini bisa `~/.bash_profile`, `~/.zshrc` (jika Anda menggunakan Zsh, default di macOS Catalina ke atas), atau `~/.profile`.
   Contoh untuk `~/.zshrc`:
   ```bash
   open ~/.zshrc
   ```
   Atau untuk `~/.bash_profile`:
   ```bash
   open ~/.bash_profile
   ```
2. Tambahkan baris berikut ke akhir file, ganti `API_KEY_ANDA` dengan API Key yang telah Anda salin:
   ```bash
   export GOOGLE_API_KEY="API_KEY_ANDA"
   ```
3. Simpan file dan tutup editor.
4. Muat ulang konfigurasi shell Anda dengan menjalankan (sesuaikan dengan file yang Anda edit):
   ```bash
   source ~/.zshrc
   ```
   atau
   ```bash
   source ~/.bash_profile
   ```
> **Penting**: Buka jendela Terminal baru agar perubahan variabel lingkungan berlaku.

---

## 4. Tambahkan Folder ke PATH Sistem

Langkah ini memungkinkan Anda menjalankan `gcommit` dari mana saja.

**Untuk Windows:**
1. Pastikan Anda memiliki file `gcommit.bat` di direktori root proyek `gcommit`.
2. Cari **"Edit the system environment variables"** di Start Menu.
3. Klik tombol **Environment Variables...**.
4. Di bagian **User variables**, pilih variabel `Path` dan klik **Edit...**.
5. Klik **New** dan tambahkan path lengkap ke folder `gcommit` Anda (misalnya, `D:\gcommit\`).
6. Klik **OK** pada semua jendela.
> **Penting**: Tutup dan buka kembali Command Prompt/PowerShell agar perubahan PATH berlaku.

**Untuk macOS/Linux:**
1. Pastikan Anda telah membuat file `gcommit` (tanpa ekstensi) di direktori root proyek `gcommit` dan membuatnya dapat dieksekusi (`chmod +x gcommit`).
2. Buka file konfigurasi shell Anda (misalnya `~/.zshrc` atau `~/.bash_profile`) seperti pada langkah pengaturan API Key.
3. Tambahkan baris berikut ke akhir file, ganti `/path/to/your/gcommit/folder` dengan path absolut ke direktori tempat Anda meng-clone repository `gcommit`:
   ```bash
   export PATH="/path/to/your/gcommit/folder:$PATH"
   ```
   Contoh: Jika Anda meng-clone `gcommit` ke `~/Documents/gcommit`, barisnya akan menjadi:
   ```bash
   export PATH="$HOME/Documents/gcommit:$PATH"
   ```
4. Simpan file dan muat ulang konfigurasi shell Anda (misalnya `source ~/.zshrc`).
> **Penting**: Buka jendela Terminal baru agar perubahan PATH berlaku.

---

## Cara Menggunakan gcommit

1. Buka Terminal (macOS/Linux) atau Command Prompt/PowerShell (Windows).
2. Pindah ke direktori proyek Git Anda:
  ```bash
  cd /path/to/your/git/project
  ```
3. Lakukan staging perubahan:
  ```bash
  git add .
  ```
4. Jalankan alat gcommit:
  ```bash
  gcommit
  ```

gcommit akan menampilkan pesan commit yang disarankan oleh AI. Ketik `y` untuk melakukan commit atau `n` untuk membatalkannya.
