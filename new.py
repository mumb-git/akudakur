#Program Ojekonline syariah
penjemputan = {
  'lokasi': ['Sentosa', 'Gajah Mada', 'Pramuka', 'Perjuangan', 'Bengkuring', 'Palaran', 'Juanda', 'Cendana', 'Alaya', 'Lempake', 'Remaja', 'Pahlawan', 'Makroman', 'Kebaktian', 'Awang Long', 'Pemuda',]
}

tujuan = {
  'lokasi': ['Sentosa', 'Gajah Mada', 'Pramuka', 'Perjuangan', 'Bengkuring', 'Palaran', 'Juanda', 'Cendana', 'Alaya', 'Lempake', 'Remaja', 'Pahlawan', 'Makroman', 'Kebaktian', 'Awang Long', 'Pemuda',]
}

harga_km = 0

def list_jalanan_penjemputan():
    penjemputan
    for key, value in penjemputan.items():
      print(key, value)


def tambah():
    tambahjalan = input('masukan nama jalan: ')
    penjemputan['lokasi'].append(tambahjalan)

def update():
    updatejalan = input('update nama jalan: ')
    if updatejalan in penjemputan['lokasi']:
      index = penjemputan['lokasi'].index(updatejalan)
      penjemputan['lokasi'][index] = input(" masukkan nama jalan :")
      print(" Jalan "+str(updatejalan)+"Berhasil Update ")
    else:# No user prompt was found 
      print(" Gagal Update !")

def hapus():
    hapusjalan = input('update nama jalan: ')
    if hapusjalan in penjemputan['lokasi']:
      index = penjemputan['lokasi'].index(hapusjalan)
      penjemputan['lokasi'].pop(index)
      print("Jalan "+str(hapusjalan)+" Berhasil Dihapus ")
    else:# No user prompt was found 
      print("Gagal Hapus !")

def list_jalanan_tujuan():
    tujuan
    for key, value in tujuan.items():
      print(key, value)

def tambah_tujuan():
    input_baru = input('masukan nama jalan: ')
    tujuan[input_baru]

def update_tujuan():
    input_baru = input('update nama jalan: ')
    tujuan[input_baru]

def hapus_tujuan():
    del tujuan [input('menghapus jalan: ')]

def login():
  print('login Pejuang PA')
  while True:
    username = input('username : ')
    passw = input('password : ')
    if username == 'Luthfi' and passw == '082' or username == 'Adit' and passw == 'unsend' or username == 'puput' and passw == 'sibukmc' :
        print('---------------------------------')
        print('-------Ojek Online Syariah-------')
        print('--Membantu Antum dalam Berpergian--')
        print('------Aman,Nyaman,Terpercaya------')
        print('---------------------------------')
        break
    else:
        print('silahkan antum memasukkan password/username dengan benar!')
        continue

def menu():
  while True:
    print('Menu')
    print('1. OjekS')
    print('0. Keluar')
    inmenu = input('masukkan pilihan : ')
    if inmenu == '1' :
      break
    elif inmenu == '6' :
      print('Antum telah logout')
      print('Jazakallah khair telah menggunakan program kami')
    else:
      continue
  
  while True:
    print('Kendaraan')
    print('1. Motor\n2. Mobil')
    kendaraan = input('masukan pilihan: ')
    if kendaraan == '1':
        harga_km = 5000
        print('\nAntum memilih motor')
        break
    elif kendaraan == '2':
        harga_km = 12000
        print('\nAntum memilih mobil')
        break
    else :
      continue

  while True:
    print('Driver')
    print('1. Ikhwan\n2. Akhwat')
    driver = input('masukan pilihan: ')
    if driver == '1':
      print('\nAntum memilih pengemudi Ikhwan')
      break
    elif driver == '2':
      print('\nAntum memilih pengemudi Akhwat')
      break
    else:
      continue

  while True:
    print('Lokasi Penjemputan')
    list_jalanan_penjemputan()
    print('==============')
    print('1. Masukkan Lokasi Penjemputan')
    print('2. Menambahkan lokasi penjemputan')
    print('3. Mengupdate lokasi penjemputan')
    print('4. Menghapus lokasi penjemputan')
    inputjemput = input('masukan pilihan: ')
    if inputjemput == '1':
      break
    elif inputjemput == '2':
      tambah()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputjemput == '3':
      update()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputjemput == '4':
      hapus()
      print("\n")
      input("Tekan Enter untuk kembali...")
    else:
      continue

  while True:
    jemput = input('Masukkan Lokasi Penjemputan: ')
    if jemput in penjemputan['lokasi']:
      break
    else:# No user prompt was found 
      print("Tidak ada lokasi")
      continue

  while True:
    print('Lokasi Tujuan')
    list_jalanan_tujuan()
    print('==============')
    print('1. Masukkan Lokasi Tujuan')
    print('2. Menambahkan lokasi Tujuan')
    print('3. Mengupdate lokasi Tujuan')
    print('4. Menghapus lokasi Tujuan')
    inputtujuan = input('masukan pilihan: ')
    if inputtujuan == '1':
      break
    elif inputtujuan == '2':
      tambah_tujuan()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputtujuan == '3':
      update_tujuan()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputtujuan == '4':
      hapus_tujuan()
      print("\n")
      input("Tekan Enter untuk kembali...")
    else:
      continue

  while True:
    intujuan = input('Masukkan Lokasi Tujuan: ')
    if intujuan in tujuan['lokasi']:
      if jemput == 'Sentosa' and intujuan == 'Alaya' or jemput == 'Alaya' and intujuan == 'Sentosa':
        jarak = 1
        break
      elif jemput == 'Pramuka' and intujuan == 'Palaran' or jemput == 'Palaran' and intujuan == 'Pramuka':
        jarak = 17
        break
      elif jemput == 'Bengkuring' and intujuan == 'Cendana' or jemput == 'Cendana' and intujuan == 'Bengkuring':
        jarak = 9
        break
      elif jemput == 'Remaja' and intujuan == 'Perjuangan' or jemput == 'Perjuangan' and intujuan == 'Remaja':
        jarak = 2
        break
      elif jemput == 'Kebaktian' and intujuan == 'Pahlawan' or jemput == 'Pahlawan' and intujuan == 'Kebaktian':
        jarak = 3
        break
      elif jemput == 'Gajah Mada' and intujuan == 'Pemuda' or jemput == 'Pemuda' and intujuan == 'Gajah Mada':
        jarak = 9
        break
      elif jemput == 'Lempake' and intujuan == 'Awang Long' or jemput == 'Awang Long' and intujuan == 'Lempake':
        jarak = 15
        break
      elif jemput == 'Juanda' and intujuan == 'Makroman' or jemput == 'Makroman' and intujuan == 'Juanda':
        jarak = 20
        break
      else:
        print('Silahkan memilih dengan benar')
    else:# No user prompt was found 
      print("Tidak ada lokasi")
      continue

  total = jarak * harga_km
  print("Titik Penjemputan : "+str(jemput))
  print("Titik Tujuan : "+str((intujuan)))
  print('Total Pembayaran '+str(total))
  

  # while True:
  #   print('mau bayar pakai apa: ')
  #   print('1. Gopay\n2. Tunai')
  #   pilihan = input('masukan pilihan: ')
  #   if pilihan == '1':
  #     gopay()
  #     print('\nAntum memilih membayar dengan gopay')
  #     input()
  #   elif pilihan == '2':
  #     tunai()
  #     print('\nAntum memilih membayar dengan tunai')
  #     input()
  #     break

  while True:
    bayar=int(input('jumlah nominal uang = Rp '))
    if total <= bayar:
      kembalian = (bayar-total)
      print('Uang kembalian = ', 'Rp',kembalian)
      break
    else:
      print('Afwan uang antum kurang')
      continue

 


login()
menu()