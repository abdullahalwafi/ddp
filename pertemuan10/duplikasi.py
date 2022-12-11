# Soal 3 Duplikat isi array
def duplikasi(array) :
    hasil = []
    for i in array :
        hasil.append(i)
        hasil.append(i)
    print(hasil)
duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])