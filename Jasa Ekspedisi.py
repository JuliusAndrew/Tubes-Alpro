import json
from datetime import datetime

filejson = 'Jasa Ekspedisi.json'

listBarang = []
Tanggal = datetime.now().strftime('%x')

nomorPengiriman = 0

fasilitas = [
    {'Kendaraan':'Motor','Harga jasa': 5000,'kapasitas maks': 30},
    {'Kendaraan':'Mobil','Harga jasa': 10000, 'kapasitas maks': 500}
    ]

while True:
    ask = input('Transportasi untuk penyortiran barang? [Mobil/Motor] ' )
    
    if ask == 'Mobil' or ask == 'mobil':
        kapasitasMaks = fasilitas[1]['kapasitas maks']
        break
    elif ask == 'Motor' or ask == 'motor':
        kapasitasMaks = fasilitas[0]['kapasitas maks']
        break
    else:
        continue
convJarak = 4000 # per 1 km

def newFile ():
    data = {"JSON" : [{"Data Pengiriman": []}]}
    with open(filejson, 'w') as file :
        json.dump(data, file, indent = 3)
        
def bacaData() :
    with open(filejson) as file :
        cetak = json.load(file)
    return cetak
    
def tambahData():
    global barang
    global jenisBarang
    global berat
    global lebar
    global harga
    global value
    global dictBarang
    global jarak
    global nomorPengiriman
    global layanan
    
    nomorPengiriman += 1
    barang = input('Masukan nama barang: ')
    jenisBarang = input('Masukan jenis barang: ')
    berat = int(float(input('Masukan berat barang (Kg): ')))
    while True:
        lebar = int(input("Masukan lebar (Cm): "))
        if lebar > 30:
            if ask == 'mobil':
                break
            elif ask == 'motor':
                print('Lebar kendaraan tidak boleh lebih dari 30 cm')
                continue
        elif lebar <= 30:
            if ask == 'mobil':
                print('Lebar barang tidak boleh kurang dari 30 cm')
                continue
            elif ask == 'motor':
                break
            
    jarak = int(input("Masukan jarak (Km): "))
    layanan = input('Masukan jenis layanan (Reguler/Cepat/Kilat): ')
    pilLayanan()
    value = harga // berat
    
    dictBarang = {
        'Nomor pengiriman' : nomorPengiriman,
        'Tanggal': Tanggal,
        'Nama barang' : barang,
        'Jenis barang': jenisBarang,
        'Jarak': jarak,
        'Berat barang': berat,
        'Lebar': lebar,
        'Harga': harga,
        'Value' : value
       }
    
    tambah = bacaData()
    tambah['JSON'][0]['Data Pengiriman'].append(dictBarang)
    with open(filejson, 'w') as file :
        json.dump(tambah, file, indent = 3)
    print('\nBARANG BERHASIL DITAMBAHKAN!')

def pilLayanan():
    global pelayanan
    global kapasitasMaks
    global jarak
    global transportasi
    global harga
    global layanan
    global hargaLayanan
    
    if layanan == 'Reguler' or layanan == 'reguler' :
        hargaLayanan = 5000
    elif layanan == 'Cepat' or layanan == 'cepat':
        hargaLayanan = 10000
    elif layanan == 'Kilat' or layanan == 'kilat':
        hargaLayanan = 20000
        
    if ask == 'mobil':
        if jarak > 3:
            harga = (jarak * convJarak) + fasilitas[0]['Harga jasa'] + hargaLayanan
        else:
            harga = fasilitas[0]['Harga jasa'] + hargaLayanan
    else:
        if jarak > 4:
            harga = (jarak * convJarak) + fasilitas[0]['Harga jasa'] + hargaLayanan
        else:
            harga = fasilitas[0]['Harga jasa'] + hargaLayanan
            
def hapusData():
    list_ = []
    baru = {"JSON" : [{"Data Pengiriman": list_}]}
    for i in bacaData()["JSON"][0]["Data Pengiriman"]:
        print(i)
    askHapus = input("\nMasukan nama barang yang ingin di hapus : ")
    with open(filejson) as file:
        baca = json.load(file)["JSON"][0]["Data Pengiriman"]
        for data_ in baca:
            if data_['Nama barang'] == askHapus:
                continue
            else:
                list_.append(data_)
    with open(filejson, 'w') as file:
        json.dump(baru, file, indent = 3)
    print('Sukses Menghapus Data Barang : {}'.format(askHapus))
    print('\n\t\t\t~DATA TELAH DIPERBARUI~\n\t\t\t=======================')
    for i in bacaData()["JSON"][0]["Data Pengiriman"]:
        print(i)
        
        
 
def knapsackBruteForce(kapasitasMaks, berat, value, n):

    if n == 0:
        tampung = [0,[]]
        return tampung 
    
    elif kapasitasMaks == 0:
        tampung
        return tampung  
      
    elif berat[n-1] > kapasitasMaks:
        return knapsackBruteForce(kapasitasMaks, berat, value, n-1)
    
    tampung1 = knapsackBruteForce(kapasitasMaks-berat[n-1], berat, value, n-1)
    tampung2 = knapsackBruteForce(kapasitasMaks, berat, value, n-1)
    
    nilai1 = value[n-1] + tampung1[0]
    nilai2 = tampung2[0]
    
    nilaiMax = max(nilai1,nilai2)
    
    if nilaiMax == nilai1:
        tampung1[0] = nilaiMax
        indeksBarang = [n-1]
        tampung1[1].extend(indeksBarang) 
        return tampung1
    else:
        return tampung2
    
    
def menuUtama():
    print('\n---------------------------------------------')
    print('Selamat Datang Di Jasa Ekspedisi Timetraveler')
    print('---------------------------------------------')
    print('Menu :',
          '\n 1. Membuat file baru'
          '\n 2. Tambahkan data barang',
          '\n 3. Lihat data barang',
          '\n 4. Hapus data barang',
          '\n 5. List pengriman barang',
          )
    print('=============================================')
    
while True:
    menuUtama()
    pilih = input('Ingin menu nomor berapa? ')
    if pilih == '1':
        newFile()
        continue
    elif pilih == '2':
        tambahData()
        continue
    elif pilih == '3':
        for i in bacaData()["JSON"][0]["Data Pengiriman"]:
            print(i) 
        continue
    elif pilih == '4':
        hapusData()
        continue
    elif pilih == '5':
        nama, berat, value = [],[],[]
        n=len(bacaData()["JSON"][0]["Data Pengiriman"])
        for i in range(n):
            berat.append(bacaData()["JSON"][0]["Data Pengiriman"][i]['Berat barang'])
            value.append(bacaData()["JSON"][0]["Data Pengiriman"][i]['Value'])
        hasil = knapsackBruteForce(kapasitasMaks, berat, value, n)
        hasilFix = hasil[1]
        panggil = bacaData()["JSON"][0]["Data Pengiriman"]
        
        print('{0:^97}'.format('T I M E  T R A V E L E R'))
        print('='*99)
        print('+' + '-'*97 + '+')
        print('{6} {0:^10} {6} {1:^15} {6} {2:^15} {6} {3:^15} {6} {4:^10} {6} {5:^7} {6}'.format('Nomor pengiriman', 'Tanggal', 'Nama barang', 'Jenis barang', 'Berat barang', 'Value', '|'))
        print('+' + '-'*97 + '+')
        for i in range(len(panggil)):
            if i in hasilFix:
                print('{6} {0:^16} {6} {1:^15} {6} {2:>15} {6} {3:>15} {6} {4:>13} {6} {5:>6} {6}'.format(panggil[i]['Nomor pengiriman'], panggil[i]['Tanggal'], panggil[i]['Nama barang'], panggil[i]['Jenis barang'], panggil[i]['Berat barang'], panggil[i]['Value'], '|'))
                print('+' + '-'*97 + '+')
        print('='*99)
        print('{0:^99}'.format('    T E R I M A  K A S I H  T E L A H  M E N G G U N A K A N'))
        print('{0:^99}'.format('    J A S A  E K S P E D I S I  K A M I'))
        break