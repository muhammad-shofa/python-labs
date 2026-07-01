# pandas merupakan library python yang sering digunakan untuk pemrosesan, manipulasi data dll dalam bentuk table atau csv

import pandas as pd

# membuat Dataset Mentah dalam bentuk Dictionary
# Di dunia ML, ini mirip seperti tabel database / excel
raw_data = {
    "Ukuran_Rumah_M2": [50, 80, 120, 45, 150],
    "Jumlah_Kamar": [2, 3, 4, 1, 5],
    "Lokasi_Pusat_Kota": [1, 1, 0, 0, 1], # 1 = Ya, 0 = Tidak
    "Harga_Rupiah": [500, 800, 1200, 400, 1800] # dalam juta
}

# mengubah dictionary menjadi DataFrame (table pandas)
df = pd.DataFrame(raw_data)

print('DataFrame Rumah:\n', df)

# .describe() digunakan untuk melihat rata-rata, nilai min, dan max dataset
print('Ringkasan data statistik dataset:\n', df.describe())

# mengambil Kolom Spesifik (Memisahkan Fitur dan Target)
# Di ML, kita harus memisahkan kolom 'Target' yang mau diprediksi (Harga)
# dengan kolom 'Fitur' (Ukuran, Kamar, Lokasi)
fitur_data = df[["Ukuran_Rumah_M2", "Jumlah_Kamar", "Lokasi_Pusat_Kota"]]
target_data = df["Harga_Rupiah"]

print('Fitur data:\n', fitur_data)
print('Target data:\n', target_data)

