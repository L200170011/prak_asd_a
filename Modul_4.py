class MhsTIF(object):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""

    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.nama=nama
        self.NIM=NIM
        self.kotaTinggal=kota
        self.uangsaku=us
    



c0 = MhsTIF('Ika', 10, 'sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'purwadadi', 265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
target = 'klaten'
Angka  = [1,4,5,10,18,23,29,31,51,64]
target1=18
Angka1 = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target2=6

#======No1=========#
def cari(Daftar,target):
    ls=[]
    for i in Daftar:
        if i.kotaTinggal == target:
            ls.append(Daftar.index(i))
    return ls

print(cari(Daftar,target))

#======No2=========#
def CariTerkecil(Daftar):
    terkecil = Daftar[0].uangsaku
    for i in Daftar:
        if i.uangsaku < terkecil:
            terkecil = i.uangsaku
    return terkecil

#======No3=========#
def UangSakuTerkecil(Daftar):
    n = []  
    terkecil = Daftar[0].uangsaku
    for i in Daftar:
        if i.uangsaku < terkecil:
            terkecil = i.uangsaku
            n.append(Daftar.index(i))
    return n

#======No4=========#
def UangSakuKurang(Daftar):
    b = []  
    for i in Daftar:
        if i.uangsaku < 250000:
            terkecil = i.uangsaku
            b.append(Daftar.index(i))
    return b

#======No5=========#
print('======output nomer 5(program linked list)======'+'\n')
class ListNode:  
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False
node1 = ListNode(15)  
node2 = ListNode(8.2)  
node3 = ListNode("Berlin")

class SingleLinkedList:  
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return
    def add_list_item(self, item):
        "add an item at the end of the list"

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return
    def list_length(self):
        "returns the number of list items"

        count = 0
        current_node = self.head

        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next

        return count

    def output_list(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next

        return
    
node1 = ListNode(15)  
node2 = ListNode(8.2)  
item3 = "Berlin"  
node4 = ListNode(15)

track = SingleLinkedList()  
print("track length: %i" % track.list_length())

for current_item in [node1, node2, item3, node4]:  
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()


        
#======No6=========#
def cari1(Angka, target1):
    low = 0
    high = len(Angka) -1
    data = []

    while low <= high:
        mid = (high + low) //2
        if Angka[mid] == target1:
            data.append(Angka.index(target1))
            return True
        elif target1 < Angka[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

#======No7=========#
def cari2(Angka1, target2):
    low = 0
    high = len(Angka1) -1
    data = []

    while low != high:
        mid = (high + low) //2
        if Angka1[mid] == target2:
            break
        elif target2 < (Angka1[mid]):
            high = mid -1
        else :
            low = mid +1
    for i in range (low, high):
        if target2 == Angka1[i]:
            data.append(i)
    return data


#======No8=========#


"""
untuk mencari berapa jumlah tebakan yang digunakan oleh Binary Search
yaitu dengan menggunakan Logaritma basis 2 (log2(n))
misalkan :
        // apabila terdapat elemen array berjumlah 100 maka memiliki maksimal 7 kali tebakan
           itu dikarenakan log2(100) = 6.643856189774725 sehingga diperoleh angka 7
           dapat juga diperoleh dari log2(128) = 7 karena yang mendekati dari 100 adalah 128

       //  apabila terdapat elemen array berjumlah 1000 maka memiliki maksimal 10 kali tebakan
           itu dikarenakan log2(1000) = 9.965784284662087 sehingga diperoleh angka 10
           dapat juga diperoleh dari log2(1024) = 10 karena yang mendekati dari 1000 adalah 128
""" 
