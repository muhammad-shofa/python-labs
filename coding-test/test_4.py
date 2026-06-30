# Tugas:
# - Buat sebuah fungsi bernama hitung_error(nilai_asli, nilai_prediksi)
# - Di dalam fungsi, hitung selisihnya: $nilai\_asli - nilai\_prediksi$.
# - Kuadratkan hasil selisih tersebut (di Python, pangkat dua menggunakan operator  2).
# - Kembalikan (return) hasil kuadrat tersebut.
# - Panggil fungsi tersebut dengan nilai asli = 90 dan nilai prediksi = 82, lalu cetak hasilnya di terminal Ubuntu kamu!

# Kalkulator Loss Function MSE Mean Squared Error
def hitung_error(nilai_asli, nilai_prediksi):
    selisih = nilai_asli - nilai_prediksi
    hasil_akhir = selisih ** 2
    return hasil_akhir

loss_prediction = hitung_error(nilai_asli=90, nilai_prediksi=82)
print(loss_prediction)

