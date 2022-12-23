# Soal 4 Menampilkan Hanya Konsonannya
def fungsi(string) :
    vokal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
    hasil = ""
    for i in range(len(string)):
        if string[i] not in vokal:
            hasil = hasil + string[i]
    print(hasil)

fungsi("Nurul Fikri")