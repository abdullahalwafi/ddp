def tambah(*angka):
    hasil = 0
    for i in angka:
        hasil += i
    print(hasil) 

def kurang(*angka):
    hasil = 0
    for i in angka:
        hasil -= i
    print(hasil)

def kali(*angka):
    hasil = 1
    for i in angka:
        hasil *= i
    print(hasil)