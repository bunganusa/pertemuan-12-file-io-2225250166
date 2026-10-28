# Program: Rekap Nilai Mahasiswa (Tugas 5 - Pertemuan 12)

def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue
                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim.strip(), nilai))
                except ValueError:
                    print(f"[Peringatan] Baris {nomor} dilewati karena tidak valid: '{baris}'")
    except FileNotFoundError:
        print(f"[Error] File '{nama_file}' tidak ditemukan!")
    return data

def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai_list = [item[1] for item in data]
    jumlah_data = len(nilai_list)
    rata_rata = sum(nilai_list) / jumlah_data
    nilai_min = min(nilai_list)
    nilai_max = max(nilai_list)
    jumlah_lulus = sum(1 for x in nilai_list if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("=== REKAPITULASI NILAI MAHASISWA ===\n")
        file.write(f"Jumlah data valid : {jumlah_data}\n")
        file.write(f"Rata-rata        : {rata_rata:.2f}\n")
        file.write(f"Nilai Minimum    : {nilai_min:.2f}\n")
        file.write(f"Nilai Maksimum    : {nilai_max:.2f}\n")
        file.write(f"Jumlah Lulus (>=60): {jumlah_lulus}\n")

def main():
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"

    print("=" * 45)
    print("      PROSES REKAPITULASI DATA NILAI FILE    ")
    print("=" * 45)

    data_valid = baca_data(input_file)

    if data_valid:
        tulis_rekap(output_file, data_valid)
        print("\n--- Ringkasan Data Valid ---")
        for nim, nilai in data_valid:
            print(f"NIM: {nim} | Nilai: {nilai}")
        print("-" * 45)
        print(f"[Sukses] Rekapitulasi berhasil ditulis ke '{output_file}'")
    else:
        print("[Gagal] Pemrosesan file dihentikan.")

if __name__ == "__main__":
    main()