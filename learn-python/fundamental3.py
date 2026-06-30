dataset_gambar = ['kucing.jpg', 'anjing.jpg']

# tambah 1 data di akhir .append()
dataset_gambar.append('ular.jpg')
print(dataset_gambar)

# gabungkan dengan list lain .extend()
dataset_gambar_2 = ['harimau.jpg', 'singa.jpg']
dataset_gambar.extend(dataset_gambar_2)
print(dataset_gambar)

# hapus data terakhir .pop()
# dataset_gambar.pop() # dicomment untuk testing
print(dataset_gambar) 

# looping dengan enumerate, mendapatkan data + indexnya
for index, nama_file in enumerate(dataset_gambar):
    print(f'{index}-{nama_file}') 

# lopping dua list bersamaan .zip()
# Bayangkan kamu punya satu list berisi Data Gambar dan satu list lagi berisi Label/Kategori dari gambar tersebut.
# Kamu ingin mengecek keduanya secara bersamaan dalam satu loop. Caranya adalah digabung pakai zip()
# 0 = berkaki 4, 1 = berkaki 2, 2 = tidak berkaki
label_target = [0,0,2,0,0]

for dataset, label in zip(dataset_gambar, label_target):
    print(f'Label: {label} | Dataset: {dataset}')
