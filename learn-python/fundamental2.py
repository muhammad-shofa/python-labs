# function
def sapa(nama):
    return f'Halo {nama}'

# call function dan simpan kedalam variable
sapa1 = sapa('Budi')
print(sapa1)

# pengondisian if-elif-else & operator logika
nilai_ujian = 90
absensi_full = True
hasil_kelulusan = ''
pesan_kelulusan = ''

if nilai_ujian >= 80:
    hasil_kelulusan = 'Lulus' 
    pesan_kelulusan = f"Selamat kamu dinyatakan lulus. nilai kamu: {nilai_ujian}. Terus tingkatkan kemampuan kamu ya!"

elif nilai_ujian >= 60:
    hasil_kelulusan = 'Remidial'
    pesan_kelulusan = f'Maaf kamu belum lulus. nilai kamu: {nilai_ujian}. Manfaatkan kesempatan ini dengan baik ya!'

else:
    hasil_kelulusan = 'Tidak Lulus'
    pesan_kelulusan = f'Maaf kamu belum lulus. nilai kamu: {nilai_ujian}. Tetap semangat dan jangan menyerah!'

print(f'Status Kelulusan: {hasil_kelulusan}\nPesan Kelulusan: {pesan_kelulusan}')

# Struktur data list (array di python) dan slicing
bahasa_pemrograman = ['PHP', 'Python', 'Javascript', 'C++', 'Java']
print(bahasa_pemrograman[2])
print(bahasa_pemrograman[2:])
print(bahasa_pemrograman[:3])
print(bahasa_pemrograman[1:3])
print(f'ambil 3 index terakhir: {bahasa_pemrograman[-3:]}')


# looping for & while
# looping for biasanya digunakan untuk looping list, dictionary dll yang jumlah datanya sudah diketahui serta minim infinit loop
# sedangkan lopping while biasanya digunakan untuk looping yang datanya dinamis dan akan berhenti ketika kondisi sudah tidak terpenuhi lagi atau false, agak rawan infinit loop
number = 1
for bahasa in bahasa_pemrograman:
    print(f"bahasa {number}: {bahasa}")
    number += 1

jumlah_bahasa = len(bahasa_pemrograman)
print(jumlah_bahasa)
while jumlah_bahasa > 4:
    print('kamu keren')
    jumlah_bahasa -= 1

# Dictionary
# dictionary adalah struktur data yang menyimpan data dalam pasangan "key" dan "value"
person1 = {
    'nama':'Budi',
    'alamat':'Surabaya',
    'skill':bahasa_pemrograman
}
print(person1)
print(person1['skill'][1])

# object & class
# class merupakan blueprint sedanhkan objek adalah hasilnya
class ModelAI:
    def __init__(self, nama_model, akurasi):
        # atribut
        self.nama = nama_model
        self.akurasi = akurasi

    # method atau function di dalam class
    def prediksi(self, data):
        return f'Model {self.nama} memprefiksi {data} dengan tingkat akurasi {self.akurasi}'
        
# mmebuat object dari class
model_klasifikasi = ModelAI(nama_model="NeuralNetwork-v1", akurasi=94.3)

# akses method yang ada di object
hasil_klasifikasi = model_klasifikasi.prediksi("kucing")
print(hasil_klasifikasi)