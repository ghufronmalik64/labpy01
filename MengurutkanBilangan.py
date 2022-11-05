print("Nama         :   Ghhufron Malik")
print("Kelas        :   TI.22.B2")
print("Mata Kuliah  :   Bahasa Pemrograman")
print("===================================")

data=[]

for i in range (3):
    x = int(input("Masukkan Bilangan: "))
    data.append(x)

print("")
print("Bilangan Sebelum Diurutkan", data)
list.sort(data)
print("Bilangan sesudah Diurutkan", data)