nilai = int(input('masukkan nilai mu : '))

while nilai >100 or nilai <0:
    print('Silahkan masukkan nilai yang benar :(')
    nilai = int(input('masukkan nilai mu kembali : '))

if nilai <=80 and nilai >=100:
    print('Nilai anda adalah A')
    print('Anda lulus')
elif nilai <=70 and nilai >=79:
    print('Nilai anda B')
    print('Anda lulus')
elif nilai <=60 and nilai >=69:
    print('Nilai anda C')
    print('Remedial')
elif nilai <=31 and nilai >=59:
    print('Nilai anda D')
    print('Lah kok bisa ?')
else:
    print('Nilai anda E')
    print('Selamat anda gagal')

