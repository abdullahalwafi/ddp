# pembukaan pemilihan tools
nama = input("Siapa namamu? ")
print("Hallo", nama, "Selamat datang ditools kami")
tools = input("""Mau Hitung apa?
1. Perjumlah (tambah)
2. Pengurangan (kurang)
3. Pembagian (bagi)
4. Pengalian (kali)
5. Pangkat (pangkat)

Silahkan pilih menggunakan yang didalam kurung co:kali
pilihanmu : """)

#tambah
if tools == "tambah":
    print("Oke tools yang", nama, "pilih adalah perjumlahan")
    
    angka1 = int(input("Masukan angka pertama? "))
    angka2 = int(input("Masukan angka kedua? "))
    hasil = angka1 + angka2
    
    print("Hasil dari penjumlahan", angka1," + ", angka2, "adalah", hasil)
    print("Terima kasih", nama, "telah menggunakan tools kami")
# Pengurangan
elif tools == "kurang":
    print("Oke tools yang", nama, "pilih adalah perjumlahan")
    
    angka1 = int(input("Masukan angka pertama? "))
    angka2 = int(input("Masukan angka kedua? "))
    hasil = angka1 - angka2
    
    print("Hasil dari pengurangan", angka1," - ", angka2, "adalah", hasil)
    print("Terima kasih", nama, "telah menggunakan tools kami")

# pembagian
elif tools == "bagi":
    print("Oke tools yang", nama, "pilih adalah pembagian")
    
    angka1 = int(input("Masukan angka pertama? "))
    angka2 = int(input("Masukan angka kedua? "))
    hasil = angka1 / angka2
    
    print("Hasil dari pembagian", angka1," / ", angka2, "adalah", hasil)
    print("Terima kasih", nama, "telah menggunakan tools kami")

# perkalian
elif tools == "kali":
    print("Oke tools yang", nama, "pilih adalah perkalian")
    
    angka1 = int(input("Masukan angka pertama? "))
    angka2 = int(input("Masukan angka kedua? "))
    hasil = angka1 * angka2
    
    print("Hasil dari perkalian", angka1," * ", angka2, "adalah", hasil)
    print("Terima kasih", nama, "telah menggunakan tools kami")

# pangkat
elif tools == "pangkat":
    print("Oke tools yang", nama, "pilih adalah pangkat")
    
    angka1 = int(input("Masukan angka pertama? "))
    pangkat = int(input("Masukan pangkatnya? "))
    hasil = angka1 ** pangkat
    
    print("Hasil dari ", angka1," ^ ", pangkat, "adalah", hasil)
    print("Terima kasih", nama, "telah menggunakan tools kami")

# Tidak ada dalam pilihan
else:
    print("Pilihan tidak tersedia")
