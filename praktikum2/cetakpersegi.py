# Meminta masukan bilangan bulat dari pengguna
size = int(input("Masukkan sebuah bilangan bulat: "))

# Mencetak persegi dengan ukuran sesuai dengan masukan pengguna
for i in range(size):
  for j in range(size):
    # Mencetak '#' dipisahkan spasi
    print('#', end=' ')
  # Mencetak pindah baris setelah setiap baris selesai dicetak
  print()