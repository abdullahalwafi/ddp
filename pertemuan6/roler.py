nama = input("Siapa namamu? ")
print("Hallo", nama, "Selamat datang diprogram kami")
pilihan = input("""Mau pilih tools mana?
1. Roler Coster
2. Menghitung Nilai
3. Praktikum

Silahkan pilih menggunakan angka contohnya 1
pilihanmu : """)

# Roler Coster
if pilihan == "1" :
    print ("Hai", nama, ", Selamat datang di Wahana Roler Coster\nSebelum Mulai kita ukur terlebih dahulu tinggi mu ya")
    tinggi = int(input ("Berapa Tinggi mu? (cm) "))
    umur = int(input ("dan berapa umurmu? (tahun) "))

    if tinggi >= 90 and umur >= 10:
        ket = "kamu boleh bermain ke wahana ini"
    else :
        ket = "mohon maaf kamu belum boleh bermain ke wahana ini"

    print("Hallo", nama, "Karena tinggi mu", tinggi, "cm dan umur mu", umur, "tahun. Maka", ket)

# Menghitung Nilai
elif pilihan == "2" :
    print ("Hai", nama, ", Selamat datang di program menghitung nilai")
    kelas = input ("Kamu itu kelas berapa? ")
    print("oke kamu kelas", kelas)
    nilai = int(input ("Berapa nilaimu? "))
    if nilai < 60 :
        ket = "Gagal"
    elif nilai <= 69 :
        ket = "cukup"
    elif nilai <= 89 :
        ket = "Sangat Bagus"
    elif nilai <= 100 :
        ket = "Istimewa"
    else :
        ket = "tidak terdefinisikan"    
    print("Nilai Kamu", nilai, "yang berarti keterangan dari nilai kamu adalah", ket)
#Praktikum 
elif pilihan == "3" :
    print ("Hai", nama, ", Selamat datang di program Praktikum")
    kelas = input ("Kamu itu kelas berapa? ")
    print("oke kamu kelas", kelas)
    status = input ("Bagaimana dengan labnya? tersedia/penuh/tidak ada\nJawabanmu? ")
    if status == "tersedia" :
        print("Silahkan praktikum")
    elif status == "penuh" :
        print("Mohon maaf silahkan pindah jadwal")
    elif status == "tidak ada" :
        print("Mohon maaf tidak jadi praktikum")
    else :
        print("Jawaban tidak terdefinisikan")