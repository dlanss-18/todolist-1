# =========================
#      TO DO LIST APP
# =========================

todo_list = []

while True:
    print("\n===== TO DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Tandai Tugas Selesai")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    # Tambah tugas
    if pilihan == "1":
        tugas = input("Masukkan tugas: ")
        todo_list.append({"tugas": tugas, "selesai": False})
        print("Tugas berhasil ditambahkan.")

    # Lihat tugas
    elif pilihan == "2":
        if len(todo_list) == 0:
            print("Belum ada tugas. Hidup lu kosong juga ternyata.")
        else:
            print("\n===== DAFTAR TUGAS =====")
            for i, item in enumerate(todo_list, start=1):
                status = "✓" if item["selesai"] else "✗"
                print(f"{i}. {item['tugas']} [{status}]")

    # Hapus tugas
    elif pilihan == "3":
        if len(todo_list) == 0:
            print("Tidak ada tugas yang bisa dihapus.")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item['tugas']}")

            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))

            if 1 <= nomor <= len(todo_list):
                hapus = todo_list.pop(nomor - 1)
                print(f"Tugas '{hapus['tugas']}' berhasil dihapus.")
            else:
                print("Nomor tugas tidak valid.")

    # Tandai selesai
    elif pilihan == "4":
        if len(todo_list) == 0:
            print("Belum ada tugas.")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item['tugas']}")

            nomor = int(input("Masukkan nomor tugas yang selesai: "))

            if 1 <= nomor <= len(todo_list):
                todo_list[nomor - 1]["selesai"] = True
                print("Tugas ditandai selesai.")
            else:
                print("Nomor tugas tidak valid.")

    # Keluar
    elif pilihan == "5":
        print("Program selesai. Akhirnya manusia berhenti nambah kerjaan.")
        break

    else:
        print("Pilihan tidak valid. Mata dipake, jangan pajangan")