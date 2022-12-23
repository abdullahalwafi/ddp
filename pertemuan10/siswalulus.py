# Soal 1 Menampilkan Siswa Lulus
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def lulus_saja(students) :
    lulus = []
    for stundent in students :
        if stundent['nilai'] > 65 :
            lulus.append(stundent['nama'])
    print(lulus)

lulus_saja(hasil_akhir)