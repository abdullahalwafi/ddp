# Input nilai X, Y, dan Z
nilaiX = int(input("Berapa Nilai X nya? "))
nilaiY = int(input("Berapa Nilai Y nya? "))
nilaiZ = int(input("Berapa Nilai Z nya? "))

# Buat Function
def persamaanLineear(x, y, z) :
    print("Hasil dari persamaan linear x^2 + 7y - z adalah")
    return print( (x**2) + (7 * y) - z )
persamaanLineear(nilaiX, nilaiY, nilaiZ)