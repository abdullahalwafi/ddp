VarNamaDepan = "Abdullah"
varNamaBelakang = "Al Wafi"
var_nama_lengkap = VarNamaDepan + " " + varNamaBelakang
var_tanggal_lahir = "Bogor, 05 Agustus 2001"
varumur = 21
varnomor = 628558888318
varEmail = "abdullahalwafi16@gmail.com"
VarAlamat = '''Jln Mohnoh Nur Kp Banyusari RT.001/008 No. 37 
DS Leuwimekar KC Leuwiliang Kab Bogor Jawa barat 16640'''
# Kriteria umur
kanakkanak = 11; remaja = 25; dewasa = 46; lansia = 47

print("Profile Pribadi")
print("Nama Lengkap ", type(var_nama_lengkap), ":" , var_nama_lengkap)
print("TTL ", type(var_tanggal_lahir), ":", var_tanggal_lahir)
print("Umur ", type(varumur), ":", varumur, "tahun")
if varumur < kanakkanak:
    kriteria = "Kanak - kanak"
elif varumur < remaja:
    kriteria = "Remaja"
elif varumur < dewasa:
    kriteria = "Dewasa"
elif varumur > lansia:
    kriteria = "Lansia"
else:
    kriteria ="Tidak ada yang cocok"
print("Kriteria Umur ", type(kriteria), ":", kriteria)
print("Nomor WA", type(varnomor), ":", varnomor)
print("Email", type(varEmail), ":", varEmail)
print("Alamat ", type(VarAlamat), ":", VarAlamat)

