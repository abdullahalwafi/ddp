cuaca = input("gimana Cuaca sekarang? (hujan/adem) ")

def berangkatKuliah(cuaca) :
    if cuaca.lower() == "hujan" :
        print("OTW kuliah naik Gocar")
    elif cuaca.lower() == "adem" :
        print("OTW kuliah naik motor")
    else :
        print("Gak jadi OTW")
berangkatKuliah(cuaca)