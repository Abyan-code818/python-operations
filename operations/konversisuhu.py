def konversi_suhu():
    while True:
        try:
            suhuawal = int(input("\nsilahkan masukkan suhu awal yang anda inginkan\n1.celcius\n2.fahrenheit\n3.reamur\n4.kelvin\nPilihan dalam angka : ").lower())
            match suhuawal:
                case 1:
                    print("Suhu awal yang anda pilih celcius")
                case 2:
                    print("Suhu awal yang anda pilih fahrenheit")
                case 3:
                    print("Suhu awal yang anda pilih reamur")
                case 4:
                    print("Suhu awal yang anda pilih kelvin")
            break
        except ValueError:
            print("tolong masukkan metode yang valid!")

    while True:
            try:
                suhuakhir = int(input("\nsilahkan masukkan suhu akhir yang anda inginkan\n1.celcius\n2.fahrenheit\n3.reamur\n4.kelvin\nPilihan dalam angka : ").lower())
                match suhuakhir:
                    case 1:
                        print("Suhu akhir yang anda pilih celcius")
                    case 2:
                        print("Suhu akhir yang anda pilih fahrenheit")
                    case 3:
                        print("Suhu akhir yang anda pilih reamur")
                    case 4:
                        print("Suhu akhir yang anda pilih kelvin")
                break
            except ValueError:
                print("tolong masukkan angka yang valid!")

    while True:
        try:
            angka = float(input("masukkan angka suhu : "))
            break
        except ValueError:
            print("tolong masukkan angka yang valid!")

    if suhuawal == 1 and suhuakhir == 2:
        hasil = (angka * 1.8) + 32
        print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 1 and suhuakhir == 3:
            hasil = (4.0 / 5.0) * angka
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 1 and suhuakhir == 4:
            hasil = angka + 273
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 2 and suhuakhir == 1:
            hasil = (angka - 32) * (5 / 9)
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 2 and suhuakhir == 3:
            hasil = 0.4 * (angka - 32)
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 2 and suhuakhir == 4:
            hasil = (angka - 32) * (5 / 9) + 273.15
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 3 and suhuakhir == 1:
            hasil = 1.25 * angka
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 3 and suhuakhir == 2:
            hasil = (angka * 2.25) + 32
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 3 and suhuakhir == 4:
            hasil = (angka * 1.25) + 273
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 4 and suhuakhir == 1:
            hasil = angka - 273
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 4 and suhuakhir == 2:
            hasil = (angka - 273) * 1.8 + 32
            print("Hasil akhirnya adalah :", hasil)
    elif suhuawal == 4 and suhuakhir == 3:
            hasil = 0.8 * (angka - 273)
            print("Hasil akhirnya adalah :", hasil)
    else:
            print("\nanda tidak bisa memasukkan 2 suhu yang sama, silahkan ulangi program")

while True:
    print("\n\n=====================================")
    print(" PYTHON SIMPLE TEMPERTURE CONVERSION")
    print("=====================================")
    konversi_suhu()

    while True:
            mengulang = str(input("\napakah anda ingin mengulang program ini? \n(y/n): "))

            if mengulang == 'y':
                break
            elif mengulang == 'n':
                print("\nterima kasih telah menggunakan program ini\nsemoga harimu menyenangkan!")
                exit()
            else:
                print("mohon masukkan input yang benar!")