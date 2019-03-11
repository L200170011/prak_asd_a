##Nama: Gilang Anggi Wisnu Brata
##Kelas: A
##NIM:L200170011

#####=====No.1==============######
class Pesan(object):
    """hai"""
    def __init__(self,sebuahString):
        self.teks= sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("kalimat mempunyai",len(self.teks),"karakter.")
    def perbarui(self,stringBaru):
        self.teks=stringBaru
        
#####=====No.1(a)==============######
    def apakahTerkandung(self,kata):
        self.kata=kata
        if self.kata in self.teks:
            return True
        else:
            return False
        
#####=====No.1(b)==============######
    def hitungKonsonan(self):
        x=self.teks
        vokal="AUIEOauieo"
        jml=0
        for a in x:
            if a.lower() not in vokal:
                jml +=1
        return jml
#####=====No.1(c)==============######
    def hitungVokal(self):
        x=self.teks
        vokal="AUIEOauieo"
        jml=0
        for a in x:
            if a.lower() in vokal:
                jml +=1
        return jml


#####====No.2=====#########
class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keaddan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

p1=Manusia("Fatimah")
p1.ucapkanSalam
        
class Mahasiswa(Manusia):
    
    
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.nama=nama
        self.NIM=NIM
        self.kotaTinggal=kota
        self.uangsaku=us
    def __str__(self):
        s=self.nama+", NIM"+str(self.NIM)\
           +". Tinggal di" +self.kotaTinggal \
           +". Uang saku Rp."+str(self.uangsaku)\
           +" tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangsaku
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"

#####======No.2(a)===================
    def ambilKotaTinggal(self):
        return self.kotaTinggal

    
#####======No.2(b)===================
    def perbaruiKotaTinggal(self,x):
        self.kotaTinggal=x

#####======No.2(c)===================
    def tambahUangSaku(self,y):
        self.y=y
        self.uangsaku=self.uangsaku+self.y
        

#####======No.3 ada dibawah setelah no.7===================

        

#####======No.4===================
    listKuliah=[]
    def ambilKuliah(self,mk):
        self.mk_baru = mk
        self.listKuliah.append(self.mk_baru)

#####======No.5 =================== 
    def hapuskuliah(self,hapus):
        self.hapus= hapus
        self.listKuliah.remove(self.hapus)



#####======No.6 =================== 
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,umur,id_siswa,asal):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.umur=umur
        self.id=id_siswa
        self.sekolah=asal
    def __str__(self):
        a="ID Siswa :"+str(self.id)+'\n'+"Umur Siswa :"+str(self.umur)+'\n'+"Asal Sekolah :" +self.sekolah 
        print (a)
    def tampilkanumur(self):
        return self.umur
    def asalSekolah(self):
        return self.sekolah
    def idSiswa(self):
        return self.id


#####======No.7=================== 
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print ("python is cool. ")

#####====beri keterangan no.7==========
        # a.NIM                 ==>Mahasiswa
        # a.ambilKotaTinggal    ==>Mahasiswa
        # a.ambilkuliah         ==>Mahasiswa
        # a.ambilNIM            ==>Mahasiswa
        # a.ambilNama           ==>Mahasiswa
        # a.ambilUangSaku       ==>Mahasiswa
        # a.hapusKuliah         ==>Mahasiswa
        # a.katakanPy           ==>MhsTIF
        # a.keadaan             ==>Manusia
        # a.kotaTinggal         ==>Mahasiswa
        # a.listKuliah          ==>Mahasiswa
        # a.makan               ==>Manusia
        # a.mengalikanDenganDua ==>Manusia
        # a.nama                ==>Manusia
        # a.olahraga            ==>Manusia
        # a.perbaruiKotaTinggal ==>Mahasiswa
        # a.tambahUangSaku      ==>Mahasiswa
        # a.uangsaku            ==>Mahasiswa
        # a.ucapkanSalam        ==>Manusia
        
    
#####======No.3===================        
a=input("masukan nama : ")
b=input("masukan NIM : ")
c=input("masukan kota asal : ")
d= input("jumlah uang saku : ")

##instance
m1=Mahasiswa("Gilang Anggi Wisnu Brata","L200170011","Ngawi",10000000)
m2=Mahasiswa("Bandi","D2001800323","Solo",650000)
m3=Mahasiswa("Parjo","D2001*00625","Karanganyar",400000)
mb=Mahasiswa(a,b,c,d)
a= MhsTIF("Doni",2327,"Klaten",350000)
                                                                                                                                                                   
