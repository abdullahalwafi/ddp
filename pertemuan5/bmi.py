# pembukaan pemilihan tools
nama = input("Siapa namamu? ")
print("Hallo", nama, "Selamat datang ditools kami")
tools = input("""Mau pilih tools mana?
1. BMI Calculator
2. Hitung Keliling Jajar Genjar
3. Hitung Luas Jajar Genjar
4. Merubah Suhu dari Fahreinheit ke celcuis dan reamur

Silahkan pilih menggunakan angka contohnya 1
pilihanmu : """)

# BMI Calculator
if tools == "1":
    print("Oke tools yang", nama, "pilih adalah BMI Calculator")
    bb = input("Silahkan masukan berat badanmu (kg) : ")
    print("Oke berat badanmu adalah", bb, "kg")
    tb = input("Sekarang silahkan masukan tinggi badan mu (cm) : ")
    print("Baik, bb = ", bb, "kg dan tb =", tb, "cm mari kita hitung BMI kamu")
    bmi = int(bb) / (int(tb)/100)**2

    print("Nilai BMI kamu adalah ", bmi)
    if (bmi < 18.5):
        status = "Kekurangan Berat Badan"
    elif (bmi < 24.9):
        status = "Normal (Ideal)"
    elif (bmi < 29.9):
        status = "Kelebihan berat badan"
    elif (bmi > 30):
        status = "Kegemukan (Obesitas)"
    print("dan status Berat Badan mu adalah : ", status)
    print("Terima kasih", nama, "telah menggunakan tools kami")

# Keliling Jajar Genjar
elif tools == "2":
    print("Oke tools yang", nama, "pilih adalah hitung keliling jajar genjar")
    a = input("Berapa alasnya? ")
    b = input("dan berapa sisi miringnya? ")
    k = 2 * (int(a) + int(b))

    print("hasil dari keliling jajar genjar dengan alas",
          a, "dan sisi miring", b, "adalah", k, "cm")
    print("Terima kasih", nama, "telah menggunakan tools kami")

# Luas jajar Genjar
elif tools == "3":
    print("Oke tools yang", nama, "pilih adalah hitung luas jajar genjar")
    a = input("Berapa alasnya? ")
    b = input("dan berapa tingginya? ")
    l = int(a) * int(b)

    print("hasil dari luas jajar genjar dengan alas",
          a, "dan tinggi", b, "adalah", l, "cm")
    print("Terima kasih", nama, "telah menggunakan tools kami")

#Fahreinheit
elif tools == "4":
    print("Oke tools yang", nama,
          "pilih adalah Merubah Suhu dari Fahreinheit ke celcuis dan reamur")
    f = input("Berapa Fahreinheit? ")
    c = 5/9 * (int(f) - 32)
    r = 4/9 * (int(f) - 32)

    print("hasil dari ubah Fahreinheit ke celcius adalah", c)
    print("hasil dari ubah Fahreinheit ke reamurA adalah", c)
    print("Terima kasih", nama, "telah menggunakan tools kami")

# Tidak ada dalam pilihan
else:
    print("Pilihan tidak tersedia")
