# pembukaan pemilihan tools
nama = input("Siapa namamu? ")
print("Hallo", nama, "Selamat datang ditools kami")
tools = input("""Mau Hitung apa?
1. Luas layang - layang
2. Keliling layang - layang?

Silahkan pilih menggunakan angka contohnya 1
pilihanmu : """)

# Luas layang layang
if tools == "1":
    print("Oke tools yang", nama, "pilih adalah hitung luas layang - layang")
    d1 = input("Berapa diagonal kesatunya? (cm) " )
    d2 = input("dan diagonal keduanya?? (cm) ")
    l = 1/2 * (int(d1) * int(d2))

    print("hasil dari luas layang - layang dengan diagonal satunya ",
          d1, "dan diagonal duanya", d2, "adalah", int(l), "cm")
    print("Terima kasih", nama, "telah menggunakan tools kami")

# keliling layang layang
elif tools == "2":
    print("Oke tools yang", nama, "pilih adalah hitung keliling layang - layang")
    ps1 = input("Berapa nilai pasangan sisi pertama? (cm) ")
    ps2 = input("dan Berapa nilai pasangan sisi pertama? (cm) ")
    k = 2* (int(ps1) + int(ps2))

    print("hasil dari keliling layang - layang dengan \n nilai pasangan sisi pertama",
          ps1, "dan nilai pasangan kedua", ps2, "adalah", int(k), "cm")
    print("Terima kasih", nama, "telah menggunakan tools kami")

# Tidak ada dalam pilihan
else:
    print("Pilihan tidak tersedia")
