#Nama:Gilang Anggi Wisnu Brata
#NIM/Kelas:L200170011/A
#Modulke:8


class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.item=[]

	def isEmpty(self):
		return len(self)==0

	def __len__(self):
		return len(self.item)

	def peek(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.item[-1]

	def pop(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.item.pop()

	def push(self, data):
		self.item.append(data)
    
#=======No.1=============    
def cetakHexa(nilai):
	remstack = Stack()
	base="0123456789ABCDEF"
	while nilai > 0:
		rem = nilai % 16
		remstack.push(rem)
		nilai = nilai // 16
	x=""
	while not remstack.isEmpty():
		x = x + base[remstack.pop()]
	print(x)

print('#=======No.1============= ')	
cetakHexa(12)
cetakHexa(31)
cetakHexa(229)
cetakHexa(31519)

#=======No.2=============   
nilai=Stack() #Membuat objek dari kelas stack
for i in range(16): #Untuk i pada range (16)
	if i % 3 == 0: #Jika i habis di bagi 3
		nilai.push(i) #Meletakkan i dalam property nilai

print('\n'+'#=======No.2============= ')
print(nilai.item)

#=======No.3============= 
nilai=Stack()  #Membuat objek dari kelas stack
for i in range(16): #Untuk i pada range (16)
    if i % 3 == 0: #Jika i habis di bagi 3
        nilai.push(i) #Meletakkan i dalam property nilai
    elif i % 4 == 0: #Jika i habis di bagi 4
    	nilai.pop() #Mengembalikan nilai dari item paling atas dari property nilai lalu mengahpusnya
    	
print('\n'+'#=======No.3============= ')
print(nilai.item)	

#=======No.4=============
class Queue(object):
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist.pop(0)
    def getFrontMost(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def getRearMost(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]

Oke = Queue()
Oke.enqueue("A")
Oke.enqueue("B")
Oke.enqueue("C")
Oke.enqueue("D")
Oke.enqueue("E")

print('\n'+'#=======No.4============= ')
print(Oke.qlist)
print("item paling depan "+Oke.getFrontMost())
print("item paling belakang "+Oke.getRearMost())

class PriorityQueue():
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        yups= []
        for i in self.qlist:
            yups.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if yups[i].priority < yups[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item


#=======No.5=============
class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

oye = PriorityQueue()
oye.enqueue("Baca",4)
oye.enqueue("Buku",7)
oye.enqueue("Aku",2)

print('\n'+'#=======No.5============= ')
print(oye.dequeue())
print(oye.dequeue())
print(oye.dequeue())
