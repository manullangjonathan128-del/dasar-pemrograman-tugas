# Masukkan
nama = input('Masukkan nama karyawan : ')
golongan = int(input('Masukkan Golongan Jabatan (1/2/3) : '))
pendidikan = input('Masukkan pendidikan terakhir : ').upper()
jam_kerja = int(input('Masukkan jumlah jam kerja : '))
gaji_pokok = 300000

# Tunjangan Jabatan
if golongan == 1:
    tunjangan_jabatan = gaji_pokok * 0.05
elif golongan == 2:
    tunjangan_jabatan = gaji_pokok * 0.1
else:
    tunjangan_jabatan = gaji_pokok * 0.15

# Tunjangan pendidikan
if pendidikan == 'SMA':
    tunjangan_pendidikan = gaji_pokok * 0.025
elif pendidikan == 'D1':
    tunjangan_pendidikan = gaji_pokok * 0.05
elif pendidikan == 'D3':
    tunjangan_pendidikan = gaji_pokok * 0.20
else :
    tunjangan_pendidikan = gaji_pokok * 0.3

# Honor
if jam_kerja >= 8:
    honor = (jam_kerja - 8) * 3500
else :
    honor = 0

# Total Tunjangan
tunjangan = tunjangan_jabatan + tunjangan_pendidikan

# Total Gaji
total_gaji = gaji_pokok + tunjangan + honor

# Hasil
print("\n==============================================")
print("      SLIP GAJI KARYAWAN PT. DINGIN DAMAI")    
print("==============================================")
print("Nama Karyawan        : " +nama)
print("Golongan             : " +str(golongan))
print("Pendidikan           : " +pendidikan)
print("Jumlah Jam Kerja     : " +str(jam_kerja))
print("----------------------------------------------")
print("Gaji Pokok           : Rp " +str(gaji_pokok))
print("Tunjangan Jabatan    : Rp " +str(tunjangan_jabatan))
print("Tunjangan Pendidikan : Rp " +str(tunjangan_pendidikan))
print("Honor Lembur         : Rp " +str(honor))
print("----------------------------------------------")
print("Total Gaji           : Rp " +str(total_gaji))
print("==============================================")