# Pertemuan 12: File I/O dan Penanganan Error Dasar

**Nama:** Bunga Nusa Pertiwi  
**NIM:** 2225250166 
**Kelas:** 3F
**Mata Kuliah:** Algoritma dan Pemrograman  

---

## 📌 Tujuan Praktikum
1. Membuka, membaca, menulis, dan menambahkan data pada file teks (`.txt`) menggunakan mode `r`, `w`, dan `a` di Python.
2. Menggunakan context manager `with` dan encoding `UTF-8` untuk menangani file I/O secara aman.
3. Memproses data teks berbasis baris menggunakan method `.strip()`, `.split()`, serta konversi tipe data.
4. Menangani exception/error spesifik seperti `FileNotFoundError` dan `ValueError` menggunakan struktur `try-except`.
5. Membangun program modular berbasis fungsi untuk memvalidasi dan merekapitulasi data nilai mahasiswa.
6. Mengelola version control proyek dan mengunggah bukti kerja ke GitHub secara berkala.

---

## 📂 Struktur Folder
```text
pertemuan-12-file-io-2225250162/
├── .gitignore
├── README.md
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
    └── rekap_nilai_file.py
```

---

## 📄 Format File Input (`data/nilai.txt`)
File input `data/nilai.txt` berisi rekaman data mahasiswa dengan format **`NIM,nilai`** di setiap barisnya:
```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

---

## 🖥️ Cara Menjalankan Program

### 1. Jalankan Latihan File I/O:
```bash
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
```

### 2. Jalankan Program Rekap Utama (Tugas 5):
```bash
python tugas/rekap_nilai_file.py
```

---

## ⚠️ Penanganan Error (Exception Handling)
Program diproteksi menggunakan `try-except` spesifik agar tidak crash saat menghadapi masalah berikut:
- **`FileNotFoundError`**: Ditangani ketika file input (`data/nilai.txt`) tidak ditemukan saat dibuka. Program akan memberikan pesan peringatan tanpa menghentikan eksekusi secara mendadak.
- **`ValueError`**: Ditangani saat konversi tipe data angka (`float()`) gagal akibat format baris tidak valid (misal: nilai berisi teks `abc`). Baris yang error akan dilewati dan dilaporkan, sementara baris valid lainnya tetap diproses.

---

## 🧪 Hasil Pengujian (Test Case)

| No | Kasus Uji | Kondisi Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | **Normal** | Seluruh baris sesuai format (`NIM,nilai`) | Semua record diproses dan statistik dihitung dengan benar | Data valid dihitung, rata-rata dan statistik sesuai | **PASS** |
| 2 | **File Hilang** | `data/nilai.txt` dihapus/tidak ada | Pesan error tampil, program tidak *crash* | Peringatan file tidak ditemukan muncul di terminal | **PASS** |
| 3 | **Nilai Invalid** | Baris berisi `A004,abc` | Baris invalid dilewati, baris valid tetap diolah | Peringatan baris 4 dilewati, data lainnya tetap masuk rekap | **PASS** |
| 4 | **Baris Kosong** | Terdapat baris kosong di antara data | Baris kosong dilewati tanpa memicu error | Baris kosong berhasil diabaikan oleh `.strip()` | **PASS** |
| 5 | **Batas Lulus** | Nilai pas 60 | Dihitung ke dalam kategori lulus | Nilai $x \ge 60$ masuk hitungan lulus | **PASS** |

---

## 💡 Refleksi
Dalam praktikum ini, saya mempelajari pentingnya pemrosesan data berbasis file persisten dibandingkan menyimpan data sementara di memori RAM. Salah satu penanganan kendala utama yang saya temukan adalah ketika menangani data tidak valid seperti `A004,abc` pada file input. Dengan menerapkan blok `try-except ValueError` di dalam perulangan pembacaan baris, program dapat secara fleksibel melepaskan baris yang rusak (*graceful error handling*) tanpa membatalkan pembacaan baris-baris valid setelahnya. Penggunaan context manager `with` juga memastikan file ditutup secara otomatis sehingga menghindari kebocoran memori (*resource leak*).