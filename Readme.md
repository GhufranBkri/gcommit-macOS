# Panduan Instalasi gcommit untuk macOS

Ikuti langkah-langkah berikut untuk mengatur alat gcommit di macOS Anda.

## 1. Persiapan Awal

Sebelum memulai, pastikan Anda memiliki **Python** dan **Git** terinstal di komputer Anda.

- **Python 3.x**:
  Python 3 mungkin sudah terinstal. Anda bisa memeriksanya dengan membuka **Terminal** dan menjalankan `python3 --version`. Jika belum, Anda bisa menginstalnya menggunakan [Homebrew](https://brew.sh/) dengan perintah `brew install python`.
- **Git**:
  Git seringkali sudah terinstal atau dapat diinstal dengan Xcode Command Line Tools. Buka **Terminal** dan jalankan `xcode-select --install`. Alternatif lain adalah melalui [Homebrew](https://brew.sh/) dengan perintah `brew install git`.

Buka **Terminal** untuk menjalankan semua perintah berikut.

---

## 2. Clone Repository gcommit

Clone repository gcommit ke komputer Anda menggunakan perintah berikut di Terminal:

```bash
git clone https://github.com/GhufranBkri/gcommit.git # Ganti dengan URL repository Anda
cd gcommit
```

lalu jalankan
`pip install GitPython google-generativeai`

---

## 3. Dapatkan dan Atur Google Gemini API Key

gcommit membutuhkan API Key dari Google Gemini untuk berkomunikasi dengan model AI.

### Dapatkan API Key

1. Buka [Google AI Studio](https://ai.google.com/studio) di browser Anda.
2. Login dengan akun Google Anda.
3. Klik **"Get API key"** di bagian kiri.
4. Klik **"Create API key in new project"** dan salin key yang muncul (diawali dengan `AIza...`).

### Atur API Key sebagai Variabel Lingkungan di macOS

1. Buka file konfigurasi shell Anda di Terminal. Jika Anda menggunakan Zsh (default di macOS Catalina ke atas), jalankan:
   ```bash
   open ~/.zshrc
   ```
   Jika Anda menggunakan Bash, jalankan:
   ```bash
   open ~/.bash_profile
   ```
   Jika file tersebut tidak ada, perintah `open` mungkin akan memberitahu Anda. Dalam kasus tersebut, Anda bisa membuatnya atau menggunakan file profil shell yang sesuai.
2. Tambahkan baris berikut ke akhir file, ganti `API_KEY_ANDA` dengan API Key yang telah Anda salin:
   ```bash
   export GOOGLE_API_KEY="API_KEY_ANDA"
   ```
3. Simpan file dan tutup editor.
4. Muat ulang konfigurasi shell Anda. Jika Anda mengedit `~/.zshrc`, jalankan:
   ```bash
   source ~/.zshrc
   ```
   Jika Anda mengedit `~/.bash_profile`, jalankan:
   ```bash
   source ~/.bash_profile
   ```
   > **Penting**: Buka jendela Terminal baru atau tab baru agar perubahan variabel lingkungan berlaku.

---

## 4. Buat Skrip `gcommit` dan Tambahkan ke PATH Sistem di macOS

Langkah ini memungkinkan Anda menjalankan `gcommit` dari direktori mana saja di Terminal.

1.  Pastikan Anda berada di direktori root proyek `gcommit` yang telah di-clone.
2.  Buat file `gcommit` tersebut dapat dieksekusi dengan menjalankan perintah berikut di Terminal:
    ```bash
    chmod +x gcommit
    ```
3.  Buka file konfigurasi shell Anda (misalnya `~/.zshrc` atau `~/.bash_profile`) seperti pada langkah pengaturan API Key.
4.  Tambahkan baris berikut ke akhir file, ganti `/path/to/your/gcommit/folder` dengan path absolut ke direktori tempat Anda meng-clone repository `gcommit`.
    ```bash
    export PATH="/path/to/your/gcommit/folder:$PATH"
    ```
    Contoh: Jika Anda meng-clone `gcommit` ke `~/Documents/gcommit`, barisnya akan menjadi:
    ```bash
    export PATH="$HOME/Documents/gcommit:$PATH"
    ```
    Anda bisa mendapatkan path absolut ke direktori `gcommit` saat ini dengan menjalankan `pwd` di dalam direktori tersebut.
5.  Simpan file dan muat ulang konfigurasi shell Anda (misalnya `source ~/.zshrc`).

> **Penting**: Buka jendela Terminal baru atau tab baru agar perubahan PATH berlaku.

---

## 5. Instal Dependensi Python

Proyek ini memerlukan beberapa pustaka Python.

1.  Pastikan Anda memiliki file `requirements.txt` di direktori root proyek `gcommit` dengan konten seperti:
    ```text
    GitPython
    google-generativeai
    ```
2.  Instal dependensi menggunakan pip:
    ```bash
    pip3 install -r requirements.txt
    ```
    Jika Anda menggunakan lingkungan virtual, aktifkan terlebih dahulu.

---

## Cara Menggunakan gcommit

1. Buka **Terminal**.
2. Pindah ke direktori proyek Git Anda:

```bash
cd /path/to/your/git/project
```

3. Lakukan staging perubahan yang ingin Anda commit:

```bash
git add . # atau git add <file1> <file2> ...
```

4. Jalankan alat gcommit:

```bash
gcommit
```

gcommit akan menampilkan pesan commit yang disarankan oleh AI. Ketik `y` untuk melakukan commit dengan pesan tersebut atau `n` untuk membatalkannya.
