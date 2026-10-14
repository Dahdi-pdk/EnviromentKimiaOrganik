# Roadmap Pengembangan Environment Belajar

## Tujuan

Membuat aplikasi yang mampu mempersiapkan seluruh lingkungan belajar secara otomatis, efisien, dan dapat dikembangkan lebih lanjut.

---

# Tahap 1 — Launcher Dasar

## Target

Menggantikan script `.cmd` dengan aplikasi Python.

### Fitur

* Membuka website.
* Membuka aplikasi.
* Membuka folder.
* Membuka terminal.
* Memberikan jeda antar proses.
* Menampilkan log pada terminal.

### Contoh

```
Membuka ChatGPT...
✓ Berhasil

Membuka VS Code...
✓ Berhasil

Membuka Folder Penelitian...
✓ Berhasil
```

Status: **Mudah**

---

# Tahap 2 — File Konfigurasi

## Target

Seluruh konfigurasi dipindahkan ke file eksternal.

Contoh:

```json
{
    "website": [],
    "application": [],
    "folder": [],
    "command": []
}
```

Keuntungan:

* Tidak perlu mengubah source code.
* Mudah membuat beberapa profil belajar.
* Mudah dibagikan.

Status: **Mudah**

---

# Tahap 3 — Profil Belajar

Mendukung beberapa konfigurasi.

Contoh:

```
Kimia
Pemrograman
Arduino
Kuliah
Penelitian
Presentasi
```

Setiap profil memiliki:

* Website
* Folder
* Program
* Terminal
* Script

Status: **Mudah**

---

# Tahap 4 — Dashboard GUI

Menggunakan salah satu framework GUI Python.

Pilihan:

* Tkinter
* CustomTkinter
* PySide6

Contoh tampilan:

```
====================================

 Environment Belajar

[ Mulai ]

----------------------------

✓ Browser
✓ Website
✓ VS Code
✓ Folder
✓ Terminal

====================================
```

Status: **Sedang**

---

# Tahap 5 — Sistem Queue

Tidak lagi membuka semuanya sekaligus.

Misalnya:

```
Website 1
↓

Tunggu 3 detik

↓

Website 2

↓

Website 3

↓

VS Code

↓

Folder

↓

Terminal
```

Keuntungan:

* Mengurangi lonjakan penggunaan CPU.
* Mengurangi penggunaan RAM secara tiba-tiba.
* Mengurangi beban jaringan.

Status: **Sedang**

---

# Tahap 6 — Scheduler Pintar

Jeda tidak lagi menggunakan timeout tetap.

Contoh kondisi:

```
CPU turun

↓

RAM stabil

↓

Disk idle

↓

Program berikutnya dijalankan
```

Kemungkinan menggunakan:

* psutil
* WMI
* Performance Counter Windows

Status: **Sedang**

---

# Tahap 7 — Browser Automation

Mengendalikan browser menggunakan Playwright.

Target:

* Membuka tab satu per satu.
* Menunggu halaman selesai dimuat.
* Login otomatis (jika diperlukan).
* Screenshot otomatis.
* Monitoring status halaman.

Catatan:

Perlu mempelajari:

* Playwright
* Chrome DevTools Protocol (CDP)

Status: **Sedang - Sulit**

---

# Tahap 8 — Plugin System

Setiap aplikasi memiliki plugin sendiri.

Contoh:

```
plugins/

browser.py

vscode.py

explorer.py

cmd.py

arduino.py

flask.py
```

Keuntungan:

* Mudah dikembangkan.
* Mudah menambah aplikasi baru.

Status: **Sulit**

---

# Tahap 9 — Monitoring

Membuat dashboard status.

Contoh:

```
Browser
✓

VS Code
✓

Folder
✓

Flask
Running

Arduino
Ready

NotebookLM
Loaded
```

Status: **Sulit**

---

# Tahap 10 — Smart Environment Manager

Target akhir.

Fitur:

* Startup otomatis.
* Queue pintar.
* Monitoring resource.
* Monitoring browser.
* Logging.
* Konfigurasi profil.
* Plugin.
* Dashboard.
* Riwayat penggunaan.
* Statistik waktu startup.

Contoh alur:

```
Menjalankan Environment

↓

Membuka Browser

↓

Website selesai

↓

Membuka VS Code

↓

VS Code siap

↓

Membuka Folder

↓

Menjalankan Flask

↓

Environment Ready
```

Status: **Lanjutan**

---

# Teknologi yang Dipelajari

## Dasar

* Python
* subprocess
* pathlib
* os
* json
* time

---

## Menengah

* psutil
* threading
* asyncio
* logging

---

## GUI

* Tkinter
* CustomTkinter
* PySide6

---

## Browser

* Playwright
* Chrome DevTools Protocol (CDP)

---

## Windows

* PowerShell
* Windows Registry
* WMI
* Performance Counter

---

# Target Jangka Panjang

Membangun sebuah **Environment Manager** yang dapat digunakan untuk berbagai aktivitas, seperti:

* Belajar
* Penelitian
* Pemrograman
* Penulisan artikel
* Presentasi
* Arduino
* Flask
* React Native

Sistem ini diharapkan mampu menyiapkan seluruh lingkungan kerja hanya dengan satu kali menjalankan aplikasi, serta dapat dikembangkan menjadi platform otomatisasi personal yang modular dan mudah dipelihara.
