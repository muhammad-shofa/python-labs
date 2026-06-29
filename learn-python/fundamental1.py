import time

# System
system_nickname = "\033[32m[ --SYSTEM-- ]\033[0m"
mc_nickname = "\033[33m[ --ANDREAS-- ]\033[0m"
print(system_nickname, "Hello World")
print(system_nickname, "Muhammad Shofa sedang belajar fundamental python pada proyek ini")

# Andreas
mc_name = "Andreas"
age = 20
height = 175.8  
weight = 74.2

friendship_request = ""

print(mc_nickname, "halo nama saya", mc_name)
print(mc_nickname, "saya berusia", age, "tahun")
print(mc_nickname, "saya memiliki tinggi", height, "dan berat ", weight, "Kg")
print(system_nickname, mc_name, "adalah tokoh utama di repositori ini, kamu mungkin akan sering melihatnya nanti!")

nama_user = input(system_nickname + " siapa namamu? ")
print(system_nickname, "halo", nama_user)

while friendship_request != "Y" and friendship_request != "N":
    friendship_request = input("maukah kamu berteman dengannya? (Y/N): ").upper()
    
    if friendship_request == "N":
        for i in range(10, 0, -1):
            print(system_nickname, "ok. semua file pada komputer kamu akan terhapus pada hitungan", {i}, end="\r")
            time.sleep(1)
    else:
        print(system_nickname, "terimakasih, Andreas akan senang sekali berteman denganmu")
        time.sleep(0.5)
        print(mc_nickname, "biasa aja sih")

print("\033[31mTeks Merah\033[0m")
print("\033[32mTeks Hijau\033[0m")
print("\033[33mTeks Kuning\033[0m")
print("\033[34mTeks Biru\033[0m")

