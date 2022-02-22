#inisialisasikan list yang akan diturunkan
arr = [5, 11, 91, 27, 3]

#cari panjang dari list
n = len(arr)

#lakukan perulangan untuk swap posisi array
for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j + 1] :
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

#tampilkan semua item list yang telah terurut
for i in range(len(arr)):
    print(arr[i])



