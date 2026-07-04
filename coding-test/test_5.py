# Tugas:
# - Kita punya data mahasiswa: [Jam_Belajar_Per_Hari, Kehadiran_Kelas_Persen].
# - Targetnya adalah 1 (Lulus) atau 0 (Gagal).
# - Silakan ketik dan lengkapi kode di bawah ini

import pandas as pd
import numpy as np
# 1. Import Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

print("--- TRAINING DECISION TREE MODEL ---")

# Dataset 4 Mahasiswa historis
raw_data = {
    "Jam_Belajar": [2, 8, 1, 7],
    "Kehadiran_Persen": [60, 90, 50, 85],
    "Status_Lulus": [0, 1, 0, 1] # 0 = Gagal, 1 = Lulus
}

df = pd.DataFrame(raw_data)
X = df[["Jam_Belajar", "Kehadiran_Persen"]]
y = df["Status_Lulus"]

# 2. Inisialisasi Model Decision Tree
# (TULIS KODEMU DI SINI: Inisialisasi DecisionTreeClassifier dan lakukan .fit(X, y))
decision_model_ai = DecisionTreeClassifier()

# decision_model_ai.fit(X, y)

print("[SUKSES] Model Pohon Keputusan sudah selesai belajar!")

# 3. Prediksi Mahasiswa Baru
# Mahasiswa Baru A: Belajar 1 jam, Kehadiran 40%
# Mahasiswa Baru B: Belajar 6 jam, Kehadiran 95%
# mahasiswa_baru = np.array([
#     [1, 40],
#     [6, 95]
# ])

# gunkaan DataFrame untuk data yang akan diprediksi dan tambahan columns agar model tahu dan tidak complain terkait data yang tidak ada labelnya (karena ia dilatih dengan data berlabel)
mahasiswa_baru = pd.DataFrame(
    [[1, 40], [6, 95]],
    columns=["Jam_Belajar", "Kehadiran_Persen"]
)

# (TULIS KODEMU DI SINI: Lakukan prediksi menggunakan .predict() terhadap mahasiswa_baru)
hasil_prediksi = decision_model_ai.predict(mahasiswa_baru)

print("--- HASIL PREDIKSI KELULUSAN ---")
# Tampilkan hasil prediksinya di sini!
print("Hasil prediksi: ", hasil_prediksi)