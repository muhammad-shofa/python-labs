import numpy as np

print('---Numpy Here!---')

# membuat array numpy, berbeda dengan list biasa
# contoh casenya seolah ini adalah data nilai asli dan prediksi real dari model ai
nilai_asli = np.array([90,83,67,88,93])
nilai_prediksi = np.array([89,76,50,73,86])

# operasi vektorisasi (kekuatan utama numpy)
# Di NumPy, kamu bisa langsung mengurangkan dan memangkatkan seluruh isi array 
# tanpa perlu menggunakan 'for loop' atau 'zip' terlebih dahulu
selisih = nilai_asli - nilai_prediksi
kuadrat_error = selisih ** 2

print("Nilai asli: ", nilai_asli)
print("Nilai prediksi: ", nilai_prediksi)
print("Selisih error: ", selisih)
print("Kuadrat error: ", kuadrat_error)

# Menghitung Rata-rata dari Kuadrat Error (Inilah Mean Squared Error yang asli!)
mse = np.mean(kuadrat_error)
print(f'Skor akhir MSE model kamu: {mse}')

