#print('Silahkan masukan nama')
#nama = input()

#print(f'hello {nama}, Selamat datang ditoko kami')
order = ""

while order == "":
    print("-"*32)
    print("Masukan Order")
    order = input("nama barang: ")
    
harga_barang = int()
while harga_barang == 0:
    print("-"*32)
    print("masukan harga barang")
    harga_barang = int(input("Harga Barang: "))
    
jumlah_pesanan = int()
while jumlah_pesanan == 0:
    print("-"*32)
    print("masukan jumlah pesanan")
    jumlah_pesanan = int(input("Kuantitas: "))

total_belanja = (jumlah_pesanan)*(harga_barang)
print(f'Total Belanja: {total_belanja}')

print("-"*32)
nominal_cash = int(input('Nominal Cash: '))
if nominal_cash < total_belanja:
    print("Uang kurang")
    
kembalian = (nominal_cash)-(total_belanja)

print("="*32)
print("RINCIAN PESANAN")
print(f'Nama Barang: {order}')
print(f'Harga Barang: {harga_barang}')
print(f'Quantity: {jumlah_pesanan}')
print(f'Grand Total: {total_belanja}')
print(f'Kembalian: {kembalian}')
print('='*32)