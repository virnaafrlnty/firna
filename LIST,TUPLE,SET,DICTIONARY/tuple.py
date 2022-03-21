# membuat Tuple dan mengisi nilai Tuple
data = (1,2,3,4,5,6,7)
print(data)
print("="*35)

#menampilkan isi Tuple dengan perulangan
for d in data:
    print(d)
print("="*35)
d = 0
while d < len(data):
    print (data[d])
    d += 1
print("="*35)

# mengupdate salah satu nilai didalam Tuple
d = list(data)
d [2]=10

data = tuple(d)
print(data)

print("="*35)

# menghapus salah satu nilai dalam Tuple
d = list(data)

# remove
d.remove(7)
data=tuple(d)
print(data)

# delete
del d [0]
data=tuple(d)
print(data)

# pop
d.pop()
data=tuple(d)
print(data)

print("="*35)

# menambahkan nilai ke dalam Tuple
d = list(data)

# append
d.append(25)
data=tuple(d)
print(data)

# insert
d.insert(1,35)
data=tuple(d)
print(data)

print("="*35)