# Tugas: Buat sebuah fungsi bernama filter_nilai_ai(daftar_nilai) yang menerima sebuah list berisi angka (nilai akurasi model).
# Di dalam fungsi: Saring angka-angka tersebut menggunakan for loop dan if. Ambil hanya nilai yang di atas atau sama dengan 80.
# Output: Fungsi harus mengembalikan (return) sebuah list baru yang hanya berisi nilai-nilai yang lolos saringan.

# contoh input: akurasi_model = [75, 82, 90, 55, 80, 64, 95]
# contoh ouput yang diharapkan: Nilai yang lolos spesifikasi AI: [82, 90, 80, 95] 

akurasi_model = [44,53,67,73,85,87,92,96]

def filter_nilai_ai(daftar_nilai):
    ouput = []
    for nilai in daftar_nilai:
        if nilai >= 80:
            ouput.append(nilai)

    return ouput

print(f'Nilai yang lolos spesifikasi AI: {filter_nilai_ai(akurasi_model)}')