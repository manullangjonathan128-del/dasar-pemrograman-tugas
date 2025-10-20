# input
pembeli = input("Masukkan nama pembeli : ")
no_hp = input('Input No. Handphone : ')
jurusan = input('Input jurusan [SBY/BL/LMP] : ')

# proses
if jurusan == "SBY":
    nama_jurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL":
    nama_jurusan = "Bali"
    harga = 350000
else :
    nama_jurusan = "Lampung"
    harga = 500000

# Input Jumlah Beli
jumlah = int(input("Masukkan jumlah pembeli : "))

# proses potongan
if jumlah>=3 :
    potongan = (jumlah * harga) * 0.1
else:
    potongan = 0

total = (jumlah * harga) - potongan

# Keluaran
print("------------------------------------")
print("       PENJUALAN TIKET BUS          ")
print("               XYZ                  ")
print("------------------------------------")
print("Nama Pembeli : "+str(pembeli))
print("No. Handphone : "+str(no_hp))
print("Kode Jurusan yang dipilih : "+str(jurusan))
print("Nama Kota Tujuan : "+str(nama_jurusan))
print("Harga : ",+(harga))
print("Jumlah Beli : ",+(jumlah))
print("------------------------------------")
print("potongan yang didapat : ",+(potongan))
print("Total Bayar : ",+(total))
ubay=int(input("Masukkan Uang Bayar : "))
uangkembali = ubay - total
print("Uang Kembali : ",+uangkembali)