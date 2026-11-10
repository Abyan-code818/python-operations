import random


def pilih_level():
    print("\n========== PILIH LEVEL ==========")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Expert")

    while True:
        pilihan = input("\nPilih tingkat kesulitan: ")

        if pilihan == "1":
            return 20, 7, "Beginner"

        elif pilihan == "2":
            return 50, 7, "Intermediate"

        elif pilihan == "3":
            return 100, 5, "Expert"

        else:
            print("Pilihan tidak valid!")


def mulai_permainan(maksimal, percobaan, level):
    angka_rahasia = random.randint(1, maksimal)
    sisa_percobaan = percobaan

    print("\n================================")
    print("         GAME TEBAK ANGKA")
    print("================================")
    print(f"Level       : {level}")
    print(f"Rentang     : 1 - {maksimal}")
    print(f"Kesempatan  : {percobaan}")

    while sisa_percobaan > 0:
        try:
            tebakan = int(input("\nTebak angka: "))

            if tebakan < 1 or tebakan > maksimal:
                print(f"Masukkan angka antara 1-{maksimal}!")
                continue

        except ValueError:
            print("Masukkan bilangan bulat!")
            continue

        sisa_percobaan -= 1

        if tebakan == angka_rahasia:
            skor = sisa_percobaan * 10

            print("\nSELAMAT! TEBAKAN KAMU BENAR!")
            print(f"Angka rahasia: {angka_rahasia}")
            print(f"Sisa percobaan: {sisa_percobaan}")
            print(f"Skor kamu: {skor}")

            return

        elif tebakan < angka_rahasia:
            print("Terlalu kecil!")

        else:
            print("Terlalu besar!")

        print(f"Sisa percobaan: {sisa_percobaan}")

    print("\nGAME OVER!")
    print(f"Angka yang benar adalah: {angka_rahasia}")


def main():
    while True:
        maksimal, percobaan, level = pilih_level()

        mulai_permainan(maksimal, percobaan, level)

        ulang = input("\nMain lagi? (y/n): ").lower()

        if ulang != "y":
            print("\nTerima kasih sudah bermain!")
            break

main()