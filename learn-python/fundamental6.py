import numpy as np

# generate data otomatis (np.arange & np.zeros)
# di machine learning kita sering membuat data buatan untuk testing atau inisialisasi bobot (weights) awal model
data_berurutan = np.arange(1, 10) # membuat data berurutan dari 1 sampai dengan sebelum 10
matriks_nol = np.zeros((3, 3)) # Membuat matriks ukuran 3x3 yang isinya angka 0 semua

print('Data berurutan: ', data_berurutan)
print('Data matriks nol:\n', matriks_nol)

# mengubah bentuk matriks np.reshape (sangat penting dalam machine learning)
# Gambar di komputer dibaca sebagai array 1 dimensi yang panjang. 
# Sebelum masuk ke model AI (misal CNN), kita harus mengubah bentuknya menjadi 2D atau 3D.
# Kita ubah 'data_berurutan' (9 elemen, 1D) menjadi Matriks 2D ukuran 3x3.
matriks_3x3 = data_berurutan.reshape(3,3)

print('Bentuk awal: ', data_berurutan)
print('Bentuk setelah di re-shape matriks 2D 3x3:\n', matriks_3x3)
print('Bentuk shape: ', matriks_3x3.shape)

# statistik dataset (np.sum, np.min, np.max) 
# digunakan untuk menganalisis dataset (misal untuk mencari niali piksel tertinggi)
print('Total nilai seluruhnya: ', np.sum(matriks_3x3))
print('Total nilai terkecil: ', np.min(matriks_3x3))
print('Total nilai terbesar: ', np.max(matriks_3x3))

# filtering data secara instan (boolean indexing)
# Bayangkan kamu mau membuang semua data pencilan (outliers) yang nilainya di bawah 5.
# Di NumPy, kamu tidak butuh 'if' di dalam 'for loop' lagi!
kondisi = matriks_3x3 > 5
data_terfilter = matriks_3x3[kondisi]

print('Data sebelum difilter:\n', matriks_3x3)
print('Data sesusah difilter:\n', data_terfilter)


