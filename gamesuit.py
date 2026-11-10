import random

seri = 0
kalah = 0
menang = 0
while True:
    print("\n===============")
    print("  PYTHON SUIT")
    print("===============")
    while True:
        try:
            pemain = int(input("\nAda 3 pilihan:\n1.Gunting\n2.Batu\n3.Kertas\nPilihan anda dalam angka : "))
            if pemain == 1 or pemain == 2 or pemain == 3:
                break
            else:
                print("tolong masukkan angka 1-3 saja!")

            match pemain:
                case 1:
                    print("\nAnda memilih gunting")
                case 2:
                    print("\nAnda memilih batu")
                case 3:
                    print("\nAnda memilih kertas")
        except ValueError:
            print("tolong masukkan input yang valid!")

    komputer = random.randint(1, 3)
    match komputer:
        case 1:
            print("Komputer memilih gunting")
        case 2:
            print("Komputer memilih batu")
        case 3:
            print("Komputer memilih kertas")

    if pemain == komputer:
        print("Pertandingan seri!!")
        seri += 1
    elif (pemain == 1 and komputer == 3) or (pemain == 2 and komputer == 1) or (pemain == 3 and komputer == 2):
        print("kamu menang!!")
        menang += 1    
    else:
        print("kamu kalah!!")
        kalah += 1

    print("\n======================================")
    print("      HASIL PERTANDINGAN SEMENTARA")
    print("======================================")
    print(f"seri sebanyak {seri} ronde")
    print(f"kalah sebanyak {kalah} ronde")
    print(f"menang sebanyak {menang} ronde")
    print("======================================")


    while True:
        ulang = str(input("\nApakah anda ingin bermain lagi?\n(y/n) : ").lower())

        if ulang == 'y':
            break
        elif ulang == 'n':
            print("\n======================================")
            print("      HASIL AKHIR PERTANDINGAN ")
            print("======================================")
            print(f"pertandingan seri sebanyak {seri} ronde")
            print(f"pertandingan kalah sebanyak {kalah} ronde")
            print(f"pertandingan menang sebanyak {menang} ronde")
            print(f"kamu telah bermain sebanyak {seri + kalah + menang} ronde")
            print("======================================")
            print("\nTerima kasih telah bermain!!")
            exit()
        else:
            print("Tolong masukkan input yang benar!!")