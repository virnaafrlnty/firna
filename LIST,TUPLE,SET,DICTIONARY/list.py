# membuat list dan mengisi nilai list
data = [1,4,6,8,10]
print(data)
print("="*35)

#menampilkan isi list dengan perulangan
for d in data:
    print(d)

d = 0
while d < len (data):
    print (data[d])
    d += 1
print("="*35)

# mengupdate salah satu nilai didalam list
data [2]= 3
print(data)
print("="*35)

# menghapus salah satu nilai dalam list
# remove
data.remove (8)
print(data)

# delete
del data [1]
print(data)

# pop
data.pop()
print(data)
print("="*35)

# menambahkan nilai ke dalam list
# append
data.append(12)
print(data)

# insert
data.insert(0,20)
print(data)
print("="*35)