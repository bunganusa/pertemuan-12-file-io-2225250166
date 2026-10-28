with open("../data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        try:
            nim, teks_nilai = baris.split(",")
            print(nim, float(teks_nilai))
        except ValueError:
            print(f"Format tidak valid pada baris: {baris}")