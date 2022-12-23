# Meminta pengguna memasukkan jumlah bilangan yang akan dihitung rata-ratanya
bilangan = int(input("Masukkan banyaknya angka: "))

# Inisialisasi variabel total dengan nilai 0
total = 0

# Meminta pengguna memasukkan angka secara berulang sebanyak bilangan kali
for i in range(bilangan):
  angka = float(input("Masukkan angka: "))
  total += angka

# Menghitung rata-rata dengan rumus total / bilangan
ratarata = total / bilangan

# Mencetak nilai rata-rata ke layar
print("Rata-rata =", ratarata)