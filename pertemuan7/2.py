print('''
Selamat datang di restoran kami
==============++++=============''')
nama = input("Silahkan Masukan Nama Pembeli? ")
noHP = input("Silahkan Masukan No Hp Pembeli? ")
menu = input("Mau pesan apa kak? (makanan/minuman) ")

if menu.lower() == "makanan" :
    print('''
        Menu Makanan
===============================
    Nama Menu   |   Harga Menu
===============================
1. Nasi Goreng  | Rp. 15.000,00
2. Mie Goreng   | Rp. 12.000,00
3. Ayam Geprek  | Rp. 18.000,00

Silahkan pilih menu dengan mengetik nomornya. Co : 1
''')
    pesanan = input("pesananmu? ")
    if pesanan == "1" :
        menuPesan = "Nasi Goreng"
        harga = 15000
    elif pesanan == "2" :
        menuPesan = "Mie Goreng"
        harga = 12000
    elif pesanan == "3" :
        menuPesan = "Ayan geprek"
        harga = 18000
    else :
        print("Menu tidak tersedia")
        exit()
elif menu.lower() == "minuman":
    print('''
        Menu Minuman
===============================
    Nama Menu   |   Harga Menu
===============================
1. Aneka Jus    | Rp. 15.000,00
2. Soft Drink   | Rp. 10.000,00
3. Sweet Ice Tea| Rp. 5.000,00

Silahkan pilih menu dengan mengetik nomornya. Co : 1
''')
    pesanan = input("pesananmu? ")
    if pesanan == "1" :
        menuPesan = "Aneka Jus"
        harga = 15000
    elif pesanan == "2" :
        menuPesan = "Soft Drink"
        harga = 10000
    elif pesanan == "3" :
        menuPesan = "Sweet Ice Tea"
        harga = 5000
    else :
        print("Menu tidak tersedia")
        exit()
else :
    print("Menu tidak tersedia")
    exit()

jumlahPesan = int(input("Mau pesen berapa? "))
bayarPesanan = harga * jumlahPesan
print('''
Invoice Pesanan
====================================''')
print ("Hallo", nama, "Terima kasih telah order\nberikut list pesananmu:")
print("Nama Pembeli     :", nama,)
print("No Handphone     :", noHP,)
print("Menu yang dipesan:", menuPesan,)
print("jumlah Pesanan   :", jumlahPesan,)
print("Total Pembayaran :", bayarPesanan,)