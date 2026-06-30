# Di library ML (seperti Scikit-Learn), saat kamu memanggil model, model tersebut punya pengaturan bawaan (default parameter) yang bisa kamu ubah kalau mau.
# fungsi untuk mensimulasikan train model ai
# learning_rate dan epochs punya nilai default jika user tidak memasukkannya
def train_model(nama_model, learning_rate=0.01, epochs=100):
    print(f'Melatih {nama_model}...')
    print(f'Learning Rate: {learning_rate} | Epochs: {epochs}')

    # simulasi rumus perhitungan akurasi sederhana
    akurasi_akhir = 100 - (learning_rate * epochs)
    return akurasi_akhir
    # print(f'Hasil akuraso: {akurasi_akhir}')

# memanggil function dengan default parameter
skor1 = train_model("Titut-A1")
print(f'Hasil Akurasi: {skor1}')

# memanggil function dengan custom parameter
skor2 = train_model("Titut-A1", learning_rate=0.63, epochs=85)
print(f'Hasil Akurasi: {skor2}')

# fungsi dengan *args (arguments, menerima banyak data tanpa batas)
# Kadang kita tidak tahu berapa banyak data atau parameter yang akan dimasukkan oleh user ke dalam fungsi kita.
# Kita bisa pakai *args (Arguments) yang akan otomatis mengubah semua input menjadi sebuah tuple (list yang tidak bisa diubah nilainya).
def cek_fitur_dataset(*fitur):
    print(f'Tipe data dari *fitur adalah: {type(fitur)}')
    print(f'Daftar fitur yang akan dimasukkan kedalam model AI')
    for item in fitur:
        print(f'f - {item}')

cek_fitur_dataset("Ukuran_Rumah", "Jumlah_Kamar", "Lokasi", "Tahun_Dibangun")
