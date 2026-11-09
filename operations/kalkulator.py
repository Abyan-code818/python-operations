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

while True:
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

    while True:
        mengulang = str(input("\napakah anda ingin mengulang program ini? \n(y/n): "))

        if mengulang == 'y':
            break
        elif mengulang == 'n':
            print("\nterima kasih telah menggunakan program ini\nsemoga harimu menyenangkan!")
            exit()
        else:
            print("mohon masukkan input yang benar!")