tampungan_sepatu = []

# Garis
def garis():
    print('-'*44)

# Tambah barang
def tambah():
    
    print(' TAMBAH BARANG '.center(44,'='))
    garis()
    while True :
        sepatu = input('Masukkan nama sepatu :')
        if sepatu in tampungan_sepatu:
            print('Barang sudah tersedia')
            pass
        elif sepatu not in tampungan_sepatu:
            tampungan_sepatu.append(sepatu)
            pilihan = input("Tambahkan barang lagi? (y/n) : ")
            garis()
            print("LIST BARANG".center(44,'='))
            garis()
            if pilihan == 'y' :
                print("|","Kode".center(12, ' '),"|", "Nama Barang".center(15, ' '),"|","\n")
                for i in tampungan_sepatu :
                    print("+     ",(tampungan_sepatu.index(i)+1) ,"      |", (i).center(16, ' '),"+")        
            else : 
                break
                        
# Menghapus barang
def hapus_barang():
    garis()
    print('Hapus barang'.center(44,'='))
    garis()    
    while True :
        hapus = input('Masukkan nama sepatu yang akan dihapus : ')
        if hapus in tampungan_sepatu :
            tampungan_sepatu.remove(hapus)
            lanjut = input('tekan y jika lanjut : ').upper()
            if lanjut == "Y" :
                pass
            else :
                break
      
        else :
            print('Barang tidak tersedia')
            break

# mengedit barang :
def edit_barang() :
    garis()
    print("LIST BARANG".center(44,'='))
    garis()
    for i in tampungan_sepatu :
        print("+ Kode Barang ",(tampungan_sepatu.index(i)+1) ,"|", (i).center(15, ' '),"+")
    while True :
        print('MENU EDIT BARANG'.center(44,'='))
        caribarang = str(input('Masukkan nama barang yang mau di edit : '))
        if caribarang in tampungan_sepatu :
            ubah_ke = input('Ubah ke : ')
            tampungan_sepatu[tampungan_sepatu.index(caribarang)] = ubah_ke
            for i in tampungan_sepatu :
                print("+ Kode Barang ".center(28," "),(tampungan_sepatu.index(i)+1) ,"|", (i).center(15, ' '),"+")
            print("\n",'-'*50)
            break
        else :
            print('barang tidak ditemukan!')
            break

        
# lanjut
def lanjut():
    lanjut = input('Lanjut (y/n) : ')
    if lanjut == 'y' :
        pass
    else :
        menu()

# Tampilkan barang
def tampilkan_barang():
    garis()
    print("LIST BARANG".center(44,'='))
    garis()
    for i in tampungan_sepatu :
        print("+ Kode Barang ",(tampungan_sepatu.index(i)+1) ,"|", (i).center(15, ' '),"+")
    exit = input('Enter untuk keluar : ')
    if exit == ' ':
        menu()
    else :
        menu()

# menu
def menu():
    A = True
    while A == True :
        print('-'*44)
        print("PROGRAM BARANG".center(44,'='))
        print('-'*44)
        print("|",'1. Tambah Barang'.center(40, ' '),"|")
        print("|",'2. Hapus Barang'.center(40, ' '),"|")
        print("|",'3. Edit Barang'.center(40, ' '),"|")
        print("|",'4. Cek Barang'.center(40, ' '),"|")
        print("|",'5. Keluar'.center(40, ' '),"|\n")
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
            tampilkan_barang()
        elif pilihan == '6':
            garis()
            print(' TERIMAKASIH '.center(44,"+"))
            garis()
            A = False
            exit = input('Enter untuk keluar : ')
            if exit == ' ':
                break
            else :
                break
        else :
            garis()
            print(' TERIMAKASIH '.center(44,"+"))
            garis()
            break
       
menu()