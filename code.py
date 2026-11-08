def kalkulator(operasi):
    while True:
        try:
            angka1 = float(input("\nsilahkan masukkan angka pertama : "))
            break
        except ValueError:
            print("tolong masukkan angka yang valid!")
            
    while True:
        try:
            angka2 = float(input("\nsilahkan masukkan angka kedua : "))
            break
        except ValueError:
            print("tolong masukkan angka yang valid!")

    if operasi == "+":
        hasil = angka1 + angka2

    elif operasi == "-":
        hasil = angka1 - angka2

    elif operasi == "*":
        hasil = angka1 * angka2

    elif operasi == "/":
        if angka2 == 0:
            print("tidak bisa dibagi oleh 0!")
            return
        hasil = angka1 / angka2
            
    elif operasi == "%":
        hasil = angka1 % angka2

    elif operasi == "**":
        hasil = angka1 ** angka2

    print("\nhasilnya adalah:", hasil)

def konversi_suhu():
    while True:
        try:
            suhuawal = int(input("\nsilahkan masukkan suhu awal yang anda inginkan\n1.celcius\n2.fahrenheit\n3.reamur\n4.kelvin\nPilihan anda : ").lower())
            break
        except ValueError:
            print("tolong masukkan metode yang valid!")

    while True:
            try:
                suhuakhir = int(input("\nsilahkan masukkan suhu akhir yang anda inginkan\n1.celcius\n2.fahrenheit\n3.reamur\n4.kelvin\nPilihan anda : ").lower())
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


def kalkulator_bb_ideal(inputtb, inputbb):
    hasil = inputbb / (inputtb * inputtb)

    print(f"\nhasil perhitungan IMT adalah : {hasil:.2f}")
    if hasil >= 30:
        print("kategori: anda obesitas")
    elif hasil >= 23 and hasil < 30:
        print("kategori: anda kelebihan berat badan")
    elif hasil >= 18.5 and hasil < 23:
        print("kategori: berat badan anda ideal")
    else:
        print("kategori: anda obesitas")

while True:
    print("\n=================================")
    print("        PYTHON OPERATIONS")
    print("=================================")
    print("1. Simple calculator")
    print("2. Simple temperature conversion")
    print("3. Simple weight calculation")
    print("=================================")

    while True:
        try:
            pilihan = int(input("\nSilahkan pilih program yang ingin dijalankan : "))
            if pilihan == 1 or pilihan == 2 or pilihan == 3:
                break
            else:
                print("\nTolong masukkan input program yang benar!")
        except ValueError:
            print("\nMohon untuk tidak memasukkan input selain angka!")

    if pilihan == 1:
        print("\n\n==========================")
        print(" PYTHON SIMPLE CALCULATOR")
        print("==========================")
        while True:
            pilihan_operasi = str(input("\nAnda ingin memilih operasi apa?\n(+,-,*,/,**,%): "))
            if pilihan_operasi == '+' or pilihan_operasi == '-' or pilihan_operasi == '*' or pilihan_operasi == '/' or pilihan_operasi == '%' or pilihan_operasi == '**':
                break
            else:
                print(pilihan_operasi, "bukan operator yang valid")
                print("\nMohon untuk memasukkan operasi yang benar!\nSilahkan masukkan ulang operator")
        
        kalkulator(pilihan_operasi)
    elif pilihan == 2:
        print("\n\n=====================================")
        print(" PYTHON SIMPLE TEMPERTURE CONVERSION")
        print("=====================================")
        konversi_suhu()
    elif pilihan == 3:
        print("\n\n===================================")
        print(" PYTHON SIMPLE WEIGHT CALCULATION")
        print("===================================")
        while True:
            try:
                berat_badan = float(input("\nberat badan : "))
                break

            except ValueError:
                print("mohon untuk memasukkan angka yang valid!")

        while True:
            try:
                tinggi_badan = float(input("\ntinggi badan (dalam meter) : "))
                break
            except ValueError:
                print("mohon untuk memasukkan angka yang valid!")
                
        kalkulator_bb_ideal(tinggi_badan, berat_badan)

    while True:
        mengulang = str(input("\napakah anda ingin mengulang program ini? \n(y/n): "))

        if mengulang == 'y':
            break
        elif mengulang == 'n':
            print("\nterima kasih telah menggunakan program ini\nsemoga harimu menyenangkan!")
            exit()
        else:
            print("mohon masukkan input yang benar!")