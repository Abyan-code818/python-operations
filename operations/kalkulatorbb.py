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
        print("kategori: anda kekurangan berat badan")

while True:
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