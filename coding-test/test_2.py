# Tugas: Buat program interaktif yang mensimulasikan pemantauan status server Linux.
# Spesifikasi:
# - Buat sebuah dictionary bernama status_server yang berisi data awal: status_server = {"cpu": "NORMAL", "ram": "NORMAL", "storage": "NORMAL"}
# - Gunakan while loop agar program terus berjalan meminta input dari user: "Pilih komponen yang mau diubah statusnya (CPU / RAM / STORAGE / EXIT): ".
# - Jika user mengetik selain 4 pilihan di atas, tampilkan pesan error dan minta input lagi (validasi input).
# - Jika user memilih salah satu komponen (misal: CPU), minta input status baru: "Masukkan status baru (NORMAL / WARNING / CRITICAL): ". Lalu ubah nilai di dalam dictionary tersebut.
# - Tampilkan isi dictionary yang sudah terupdate ke terminal.
# - Jika user mengetik EXIT, perulangan berhenti dan program selesai.

status_server = {
    "cpu":"NORMAL",
    "ram":"NORMAL",
    "storage":"NORMAL"
}

def show_status_server():
    print('Status server:')
    for key, value in status_server.items():
        print(f'{key} - {value}')

show_status_server()
pilihan_user = input("Pilih komponen yang mau diubah statusnya:\n[1]CPU\n[2]RAM\n[3]STORAGE\n[4]EXIT\nPilihanmu: ")

while pilihan_user != "1" and pilihan_user != "2" and pilihan_user != "3" and pilihan_user != "4":
    print("Pastikan kamu memilih dengan benar")
    pilihan_user = input("Pilih komponen yang mau diubah statusnya:\n[1]CPU\n[2]RAM\n[3]STORAGE\n[4]EXIT\nPilihanmu: ")


if pilihan_user == "1":
    status_baru = input("Masukkan status CPU baru:\n[1]NORMAL\n[2]WARNING\n[3]CRITICAL\nPilihanmu: ")
    if status_baru == "1":
        status_server["cpu"] = "NORMAL"
        show_status_server()
    elif status_baru == "2":
        status_server["cpu"] = "WARNING"
        show_status_server()
    elif status_baru == "3":
        status_server["cpu"] = "CRITICAL"
        show_status_server()
    else:
        print("Error, pilih yg benar")
        show_status_server()
elif pilihan_user == "2":
    status_baru = input("Masukkan status RAM baru:\n[1]NORMAL\n[2]WARNING\n[3]CRITICAL\nPilihanmu: ")
    if status_baru == "1":
        status_server["ram"] = "NORMAL"
        show_status_server()
    elif status_baru == "2":
        status_server["ram"] = "WARNING"
        show_status_server()
    elif status_baru == "3":
        status_server["ram"] = "CRITICAL"
        show_status_server()
    else:
        print("Error, pilih yg benar")
        show_status_server()
elif pilihan_user == "3":
    status_baru = input("Masukkan status RAM baru:\n[1]NORMAL\n[2]WARNING\n[3]CRITICAL\nPilihanmu: ")
    if status_baru == "1":
        status_server["storage"] = "NORMAL"
        show_status_server()
    elif status_baru == "2":
        status_server["storage"] = "WARNING"
        show_status_server()
    elif status_baru == "3":
        status_server["storage"] = "CRITICAL"
        show_status_server()
    else:
        print("Error, pilih yg benar")
        show_status_server()
elif pilihan_user == "4":
    print("Exit...")