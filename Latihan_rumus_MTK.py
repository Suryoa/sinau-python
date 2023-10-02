import os

def rumus_kecepatan ():
    print("Hitung Kecepatan Mobil")
    jarak = int(input("Masukan Jarak: "))
    waktu = int(input("Masukan waktu: "))
    kecepatan = jarak * waktu
    print('Kecepatanya adalah: ', kecepatan,'\n')

def luas_segitiga():
    print("Hitung Luas Segitia")
    a = float(input("Luas alas: "))
    t = float(input("Tinggi segitiga: "))
    segitiga = 1/2 * a * t
    print(f"Luas segitga: {segitiga}\n")

while True:
    pilihan_opsi = int(input("Pilih rumus yang mau dipakai:\n\n1. Hitung kecepatan\n2. Luas Segitiga\n\nPilih Nomer berapa?:"))
    os.system ("clear")
    if pilihan_opsi == 1:
        rumus_kecepatan()
    
    elif pilihan_opsi == 2:
        luas_segitiga()
        
    else:
        break
        
