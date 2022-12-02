nama = input("Siapa namamu? "); alamat = input("Dimana alamatmu? "); gender = input("Apa jenis kelaminmu? (pria/wanita) "); tanggal = input("Kapan tanggal lahirmu? "); umur = input("Berapa umurmu? "); tb = int(input("Berapa tinggi badanmu? (cm) "))

def biodata(nama, alamat, gender, tanggal, umur, tb) :
    if gender == "pria":
        ideal = (tb - 100) - ((tb - 100) * (10 / 100))
    elif gender == "wanita":
        ideal = (tb - 100) - ((tb - 100) * (15 / 100))
    else :
        print("maaf jenis kelamin tidak terdefinisikan")
        exit()
    print()
    print("Nama Kamu adalah", nama)
    print("kamu tinggal di", alamat)
    print("Jenis Kelaminmu adalah", gender)
    print("Kamu lahir pada tanggal", tanggal)
    print("Sekarang umur mu adalah ", umur)
    print("dengan tinggi badanmu", tb, "cm")
    print("Maka berat badan idealmu adalah", ideal, "kg")
biodata(nama, alamat, gender, tanggal, umur, tb)