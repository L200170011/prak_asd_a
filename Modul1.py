print (" Praktikum Modul 1","\n",
       "Nama     :Gilang Anggi Wisnu Brata","\n",
       "NIM/Kelas:L200170011/A","\n","\n")

print ("====L200170011====","Nomer 1","\n")
def CetakSiku(x):
    for a in range(1,x+1):
        print ("*"*a)
CetakSiku(5)

print ("\n","====L200170011====","Nomer 2","\n")
def gambarlahPersegi4(x,y):
    for a in range(x):
        if a==x-1 or a==0 :
            print ("@"*y)
        else:
            print ("@"+" "*(y-2)+ "@")
gambarlahPersegi4(4,5)


print ("\n","====L200170011====","Nomer 3","\n")
def jumlahHurufVokal(x):
    kumpulanvokal="AUIEOauieo"
    jml=0
    for a in x:
        if a.lower() in kumpulanvokal:
            jml+=1
    return (len(x),jml)
print (jumlahHurufVokal("Surakarta"))
def jumlahHurufKonsonan(x):
    kumpulanvokal="AUIEOauieo"
    jml=0
    for a in x:
        if a.lower() not in kumpulanvokal:
            jml+=1
    return (len(x),jml)
print (jumlahHurufKonsonan("Surakarta"))


print ("\n","====L200170011====","Nomer 4","\n")
def rerata(b):
    hasil=sum (b)/len(b)
    return hasil
print(rerata([1,2,3,4,5]))


print ("\n","====L200170011====","Nomer 5","\n")
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primaKecil=[2,3,5,7,11]
    bukanPrKecil=[0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range (2,int(sq(n))+1):
            if(n%i==0):
                return False
        return True
print(apakahPrima(17))
print (apakahPrima(97))
print (apakahPrima(123))

                        
print ("\n","====L200170011====","Nomer 6","\n")
def bilPrima(a,b):
    for num in range(a,b + 1): 
        if num > 1: 
            for i in range(2,num): 
                if (num % i) == 0: 
                    break 
            else: 
                print(num)
print (bilPrima(2,1000))



print ("\n","====L200170011====","Nomer 7","\n")
def faktorPrima(bilangan):
    factorlist=[]
    a=2
    while a<=bilangan:
        if bilangan%a==0:
            bilangan/=a
            factorlist.append(a)
        else:
            a+=1
    return factorlist
print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))


print ("\n","====L200170011====","Nomer 8","\n")
h="do"
k="indonesia tanah air beta"
def apakahTerkandung(h,k):
    return h.lower() in k.lower()
print (apakahTerkandung(h,k))
print (apakahTerkandung("pusaka",k))


print ("\n","====L200170011====","Nomer 9","\n")
def Cetak(awal,akhir):
    for x in range(awal,akhir):
        if x%3 == 0 and x%5==0:
            print("python UMS")
        elif x%5 == 0:
            print ("UMS")
        elif x%3 == 0 :
            print("python")
        else:
            print(x)
Cetak(1,100)

print ("\n","====L200170011====","Nomer 10","\n")
def selesaikanABC(a,b,c):
    a=float (a)
    b=float(b)
    c=float(c)
    d=((b**2)-(4*a*c))
    if d<0:
        return "Determinannya negatif. Persamaan tidak mempunyai akar real"
    else:
        p1=(-b+(d**0.5))/(2*a)
        p2=(-b-(d**0.5))/(2*a)
        jadi=(p1,p2)
        return jadi
print (selesaikanABC(1,2,3))


print ("\n","====L200170011====","Nomer 11","\n")
def apakahKabisat(tahun):
    if (tahun % 4) == 0:
        if (tahun % 100) == 0:
            if (tahun % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(apakahKabisat(1896))
print(apakahKabisat(1900))
print(apakahKabisat(2004))


print ("\n","====L200170011====","Nomer 12","\n")
from random import randint as rentangtebakan
a=rentangtebakan(1,10)
print("Game Tebak angka antara 1-10","\n",
      "---------------------------")
x = -1
while x != a:
    x= eval(input("masukan tebakan anda: "))
    if x == a:
        print ("tebakan benar")
    elif x < a:
        print("angka terlalu kecil.Coba lagi")
    else:
        print ("angka terlalu besar.Coba lagi")
        


print ("\n","====L200170011====","Nomer 13","\n")
def katakan(x):
    satuan = [' ', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    hasil = " "
    if x < 12 :
        hasil += satuan[x]
    elif x < 20 :
        hasil += katakan(x-10) + " belas"
    elif x < 100:
        hasil += katakan(int(x/10)) + " puluh" + katakan(x%10)
    elif x < 200 :
        hasil += "seratus" + katakan(x-100)
    elif x < 1000 :
        hasil += katakan(int(x/100)) + " ratus" + katakan(x%100)
    elif x < 2000 :
        hasil += "seribu" + katakan(x-1000)
    elif x < 1000000 :
        hasil += katakan(int(x/1000)) + " ribu" + katakan(x%1000)
    elif x < 1000000000 :
        hasil += katakan(int(x/1000000)) + " juta" + katakan(x%1000000)
    elif x >= 1000000000 :
        hasil += katakan(int(x/1000000000)) + " milyar" + katakan(x%1000000000)

    return hasil
print (katakan(3488900000))


print ("\n","====L200170011====","Nomer 14","\n")
def formatRupiah(x):
    L200170011=""
    a=0
    for l in str(x) [::-1]:
        if a<3:
            L200170011 += l
            a += 1
        else:
            L200170011= L200170011+"."+l
            a=1
    return "Rp. " + L200170011[::-1]
print(formatRupiah(1500))
print(formatRupiah(2560000))


