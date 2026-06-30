# Tugas: buat ouput seperti di bawah ini berdasarkan dataset yang ada
# No. 1 -> Model_A mendapatkan skor akurasi: 92.5% [LOLOS]
# No. 2 -> Model_B mendapatkan skor akurasi: 78.2% [GAGAL]
# No. 3 -> Model_C mendapatkan skor akurasi: 88.0% [LOLOS]

# Dataset:
# nama_model = ["Model_A", "Model_B", "Model_C"]
# skor_akurasi = [92.5, 78.2, 88.0]

# Gunakan zip() dan enumerate() (bisa dikombinasikan atau dipakai bergantian) untuk menampilkan output terstruktur di terminal.
# Catatan: Status [LOLOS] diberikan jika akurasi di atas 80%, jika di bawah itu maka [GAGAL].

nama_model = ["Model_A", "Model_B", "Model_C"]
skor_akurasi = [92.5, 78.2, 88.0]

# for index, (model, akurasi) in zip(enumerate(nama_model), enumerate(skor_akurasi)):
for index, (model, akurasi) in enumerate(zip(nama_model, skor_akurasi)):
    if akurasi > 80:
        status = "[LOLOS]"
    else:
        status = "[GAGAL]"
    print(f'No. {index + 1} -> {model} mendapatkan skor akurasi: {akurasi} {status}')


