# cara biasa
angka = [1,2,3,4,5]
kuadrat_biasa = []
for x in angka:
    kuadrat_biasa.append(x ** 2)
    
print(kuadrat_biasa)

# cara AI Engineer (List Comprehension)
kuadrat_fast = [x ** 2 for x in angka]
print(kuadrat_fast)

# Slicing
# dalam machine learning biasanya slicing digunakan untuk memotong data
dataset = ['data1','data2','data3','data4','data5','data6','data7','data8','data9','data10']
data_train = dataset[:8] # mengambil index 0 sampai 8 - 80% data pertama
data_test = dataset[8:] # mengambil index 8 sampai terakhir - 20% data terakhir

print("Data train:", data_train)
print("Data test:", data_test)

# lambda
# pada machine learning terutama pada saat menggunakan library pandas untuk data cleansing kita perlu fungsi matematika sederhana yang dipakai sekali,
# jadi tidak perlu pakai def function() melainkan lambda
# membuat func sementara dengan lambda
rumus_sederhana = lambda x: x * 3 + 2

print('lambda result', rumus_sederhana(20))

# pada saat melatih model biasanya perlu mengatur konfigurasi model tersebut menggunakan struktur data dictionary (key: value)
# konfigurasi atau hyperparameter model ML
model_config = {
    "learning_rate": 0.01,
    "epochs": 100,
    "optimizer": "Adam",
    "layers": [64, 32, 16] 
}

print(f"model ini akan ditraining dengan optimizer {model_config["optimizer"]} selama {model_config["epochs"]} kali.")