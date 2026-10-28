
print("PROGRAM MENENTUKAN KELULUSAN SISWA")
print("----------------------------------")

nama = input("Masukkan nama siswa: ")
nilai = float(input("Masukkan nilai siswa: "))

if nilai >= 75:
    print("Nama siswa:", nama)
    print("Nilai:", nilai)
    print("Keterangan: LULUS")
else:
    print("Nama siswa:", nama)
    print("Nilai:", nilai)
    print("Keterangan: TIDAK LULUS")
