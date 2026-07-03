# scikit-learn merupakan library python yang diguankan untuk membuat model machine learning

import pandas as pd
import numpy as np

# import model linear regression dari scikit learn
from sklearn.linear_model import LinearRegression

print('--- Train My First AI Model using Scikit-learn ---')

# dataset rumah (fitur & target)
raw_data = {
    "Ukuran_Rumah_M2": [50, 80, 120, 45, 150],
    "Jumlah_Kamar": [2, 3, 4, 1, 5],
    "Harga_Rupiah": [500, 800, 1200, 400, 1800]
}

df = pd.DataFrame(raw_data)

# memisahkan fitur (x) & target (y) | stanar notasi dalam machine learning
x = df[["Ukuran_Rumah_M2", "Jumlah_Kamar"]]
y = df["Harga_Rupiah"]

# inisialisasi model
model_ai = LinearRegression()

# proses training .fit()
# Di baris ini, AI mencari pola hubungan antara Ukuran + Kamar dengan Harga
model_ai.fit(x, y)

print("[DONE]Model AI selesai di training")

# Sekarang, bayangkan ada rumah baru di pasar dengan spesifikasi:
# Rumah Baru 1: Ukuran 70 M2, Kamar 2
# Rumah Baru 2: Ukuran 100 M2, Kamar 3
rumah_baru = np.array([
    [70, 2],
    [100, 3]
])

# menggunakan model ai yang sudah ditraining untuk prediksi harga terhadap data baru
hasil_prediksi = model_ai.predict(rumah_baru)

print("--- HASIL PREDIKSI AI ---")
print(f"Rumah 1 (70m2, 2 Kamar)  -> Prediksi Harga AI: Rp {hasil_prediksi[0]:.1f} Juta")
print(f"Rumah 2 (100m2, 3 Kamar) -> Prediksi Harga AI: Rp {hasil_prediksi[1]:.1f} Juta")

