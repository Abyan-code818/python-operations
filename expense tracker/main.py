import json
import os

FILE_DATA = "pengeluaran.json"

def baca_data():
    if not os.path.exists(FILE_DATA):
        return []

    with open(FILE_DATA, "r") as file:
        return json.load(file)


def simpan_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)


def tambah_pengeluaran(data):
    keterangan = input("Masukkan keterangan: ")

    try:
        nominal = int(input("Masukkan nominal: Rp"))

        if nominal <= 0:
            print("Nominal harus lebih dari 0!")
            return

    except ValueError:
        print("Nominal harus berupa angka!")
        return

    pengeluaran = {
        "keterangan": keterangan,
        "nominal": nominal
    }

    data.append(pengeluaran)
    simpan_data(data)

    print("Pengeluaran berhasil disimpan!")


def tampilkan_pengeluaran(data):
    if not data:
        print("Belum ada data pengeluaran.")
        return

    print("\n===== RIWAYAT PENGELUARAN =====")

    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['keterangan']} - Rp{item['nominal']:,}")


def hitung_total(data):
    total = 0

    for item in data:
        total += item["nominal"]

    print(f"\nTotal pengeluaran: Rp{total:,}")


def main():
    data = baca_data()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Tambah Pengeluaran")
        print("2. Riwayat Pengeluaran")
        print("3. Total Pengeluaran")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pengeluaran(data)

        elif pilihan == "2":
            tampilkan_pengeluaran(data)

        elif pilihan == "3":
            hitung_total(data)

        elif pilihan == "4":
            print("Terima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
