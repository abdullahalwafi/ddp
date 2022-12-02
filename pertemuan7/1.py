kendaraan = input ('''Nama kendaraan? (mobil/motor)  
jawabanmu = ''')
bensin = input ('''Jenis Bensin? (pertalite/pertamax/turbo)  
jawabanmu = ''')

if bensin.lower() == "pertalite"  :
    hargaBensin = 10000
    jarakBensin = 12
elif bensin.lower() == "pertamax"  :
    hargaBensin = 14000
    jarakBensin = 13
elif bensin.lower() == "turbo"  :
    hargaBensin = 17000
    jarakBensin = 13.5
else :
    print('Data bensin tidak ada')
    exit()

kota = input ('''Kota tujuan? (jakarta/bekasi/depok/tanggerang/bogor)  
jawabanmu = ''')

if kota.lower() == "jakarta"  :
    jarakKota = 20
elif kota.lower() == "bekasi"  :
    jarakKota = 35.7
elif kota.lower() == "depok"  :
    jarakKota = 5
elif kota.lower() == "tanggerang"  :
    jarakKota = 99
elif kota.lower() == "bogor"  :
    jarakKota = 120.6
else :
    print('Data kota tidak ada')
    exit()

pemakaianBensin = jarakKota / jarakBensin
pemakaianPerliter = pemakaianBensin * hargaBensin
print("Nama Kendaraaan anda", kendaraan.upper())
print("Jenis bensin anda", bensin.upper())
print("Kota yang anda dituju", kota.upper())
print("Pemakaian bensin?", "{:.2f}".format(pemakaianBensin), "Liter")
print("Total harga dari bensin yang dikeluarkan? Rp.", int(pemakaianPerliter))
    
