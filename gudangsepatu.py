tampungan_sepatu = []

# Tambah barang
def tambah() :
    import os
    os.system("CLS")
    print("\n   - Tambah Sepatu -")
    print("\nMasukkan data sepatu baru")
    sepatu = input("Masukkan Nama Sepatu : ")
    ukuran = input("Masukkan Ukuran : ")
    stok = input("Masukkan Jumlah Stok : ")
    data = open("datasepatu.txt","a")
    data.writelines([sepatu+","+ukuran+","+stok+ "\n"])
    print("/n[Data Sepatu Berhasil Ditambahkan]")
    data.close()

    print("\nIngin menambahkan sepatu lagi? (Ya/Tidak) ", end=" ")
    tambahdata = input (" : ")
    if tambahdata == "y"or tambahdata == "Y":
        tambah()
    else :
        print("\nTekan [ENTER] untuk kembali ke menu.")
        input()
        menu()

# Menghapus barang
def hapus_barang() :
	import os
	os.system("CLS")
	print("\n        - Hapus Data Sepatu -")
	data = open("datasepatu.txt")
	output = []
	str = input("\nMasukkan nama sepatu yang ingin dihapus : ")
	for hapus in data:
		if not hapus.startswith(str):
			output.append(hapus)
			
	data = open("datasepatu.txt.","w")
	data.writelines(output)
	print("\n[Data Sepatu Telah Terhapus]")
	data.close()
	print("\nIngin menghapus data sepatu lagi? (Ya/Tidak)", end=" ")
	hapusdata = input(" : ")
	if hapusdata == "y" or hapusdata == "Y":
		hapusdata()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()

# mengedit barang :
def edit_barang() :
    print("LIST BARANG".center(44,'='))
    for i in "" :
        print("+ Kode Barang ",(tampungan_sepatu.index(i)+1) ,"|", (i).center(15, ' '),"+")
    while True :
        print('MENU EDIT BARANG'.center(44,'='))
        caribarang = str(input('Masukkan nama barang yang mau di edit : '))
        if caribarang in tampungan_sepatu :
            ubah_ke = input('Ubah ke : ')
            (indexcaribarang) = ubah_ke
            for i in tampungan_sepatu :
                print("+ Kode Barang ".center(28," "),(tampungan_sepatu.index(i)+1) ,"|", (i).center(15, ' '),"+")
            print("\n",'-'*50)
            break
        else :
            print('barang tidak ditemukan!')
            break

# Tampilkan barang
def tampilkan_barang():
    import os
    os.system("CLS")
    print("LIST BARANG".center(44,'='))
    data = open("datasepatu.txt","r")
    isi = data.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\n[Data Tidak Ditemukan]")
    else :
        i = 1
        for datasepatu in isi:
           content = datasepatu.split(",")
           print("\n" + str(i) + ",",end=" ")
           print(content[0]+"|"+ content[1]+"|"+ content[2])
           i += 1
    print("\nTekan [ENTER] untuk kembali ke menu.")
    data.close()
    input()
    menu()
    

# cek barang
def cek_barang():
	import os
	os.system("CLS")
	print("\n          - Pencarian Barang -")
	cari = input("\nMasukkan nama barang yang ingin dicari : ")
	data = open("datasepatu.txt","r")
	isi = data.readlines()
	isi.sort()
	
	for data_sepatu in isi:
			content = data_sepatu.split(",")
			if pecah[0] == cari:
				print("\nNama Barang	: "+content[0])
				print("Ukuran		: "+content[1])
				print("Jumlah Stok	: "+content[2])
				
			
	print("\n\nTekan [ENTER] untuk kembali ke menu")
	data.close()
	input()
	menu()

# menu
def menu():
    print('-'*44)
    print("PROGRAM BARANG".center(44,'='))
    print('-'*44)
    print("|",'1. Tambah Barang'.center(40, ' '),"|")
    print("|",'2. Hapus Barang'.center(40, ' '),"|")
    print("|",'3. Edit Barang'.center(40, ' '),"|")
    print("|",'4. Cek Barang'.center(40, ' '),"|")
    print("|",'5. Cek nama barang'.center(40, ' '),"|")
    print("|",'6. Keluar'.center(40, ' '),"|\n")
    print('-'*44)
    pilihan = input("Pilih menu \t: ").upper()
    print('-'*44)
    if pilihan == "1" or pilihan == "TAMBAH BARANG":
        tambah()
    elif pilihan == "2" or pilihan == "HAPUS BARANG":
        hapus_barang()
    elif pilihan == "3" or pilihan == "EDIT BARANG":
        edit_barang()
    elif pilihan == "4" or pilihan == "CEK BARANG":
         tampilkan_barang