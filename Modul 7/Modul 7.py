#Nama      :Gilang Anggi Wisnu Brata
#NIM/Kelas :L200170011/A
#Modul ke- : 7

#=====No.1============
print('=====No.1============')

import re
file_p = open("Indonesia.txt", "r")
p = file_p.read()
file_p.close()
ukiran=r'me[\w]+'
tampil= re.findall(ukiran,p)
print(tampil,'\n')

#=====No.2============
print('\n','=====No.2============')

import re
file_p = open("Indonesia.txt", "r")
p = file_p.read()
file_p.close()
ukiran=r'di[\w]+'
tampil= re.findall(ukiran,p)
print(tampil,'\n')

#=====No.3============
print('\n','=====No.3============')

import re
file_p = open("Indonesia.txt", "r")
p = file_p.read()
file_p.close()
ukiran=r'di [\w]+'
tampil= re.findall(ukiran,p)
print(tampil,'\n')

#=====No.4============
print('\n','=====No.4============')

import re
file_p = open('KEI.htm', 'r',encoding='latin1')
p = file_p.read()
file_p.close()
ukiran=r'(\w+)</a></td>'
tampil= re.findall(ukiran,p)
print(tampil)

import re

wiki = open('KEI.htm', 'r', encoding='latin1')

teks = wiki.read()
wiki.close()


cari = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', teks)

listbaru = []

for i in cari:
    a = (i[0],float(i[4]))
    listbaru.append(a)

print(listbaru)
