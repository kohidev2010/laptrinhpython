#kieu du lieu danh sach list
"""tb = [6.7, 7.8, 8.9, 5.6]
print(type(tb))"""

"""a = [1, 3.4, "hello"]
print(a)"""

#ham list()
"""a = list(("aa", 3.4))
print(a)"""

# it is possible to contain many lists in one list
"""a = [[1,2,3], [34,34,56], 6, [8,9,10]]
print(a)"""


#list is an object which is indexed
"""a = [4,6,5,6,4,12]
print(a[0])"""

"""a = [8,6,5,9,10,12]
print(a[-1])"""

"""a = [8,6,5,9,10,12]
print(a[1::1])"""

"""a = [1, 2, 3, 4, 5, 6, 7]
print(a[0::2])"""

#them phan tu trong danh sach
#a = [1, 2, 3, 4, 5, 6, 7]
#<ten_ds>.append() them phan tu cuoi danh sacb
#a.append(8) #them phan tu append()
#<ten_ds>.insert(i, gtthem) them phan tu o vi tri duoc chi dinh
#a.insert(2,10)
#<ten_ds>.delitem_(index) xoa theo chi so index duoc chi dinh
#a.__delitem__(-3)
#<ten_ds>.remove(<gia tri can xoa>)
"""a = [1, 2, 3, 4, 5, 6, 7]
a.remove(6)
print(a)"""
#neu phan tu do khong co trong list vd la 8 nose bao loi
#a = [1, 2, 3, 3, 4, 3, 5, 6, 7]
"vi du trong danh sach co nhieu gia tri giong nhau"
"chung ta dung phuong thuc remove no se xoa di gia tri dau tien tu trai sang phai"
"""a.remove(3)
print(a)"""
#result [1, 2, 3, 4, 3, 5, 6, 7]



#khoi tao mot ds rong
"""a = []
n = int (input( "n = "))
for i in range(n):
    print("nhap phan tu thu", i + 1, ": ", end="")
    x = int(input())
    a.append(x)
for i in range(n):
    print("phan tu thu ", i+1, ": ", a[i])"""

#nhap vao n phan tu cua danh sach va tinh tong cac phan tu vua nhap
#sum(<ds>) tinh tong ca phan tu
"""a = []
n = int (input( "n = "))
for i in range(n):
    print("nhap phan tu thu", i + 1, ": ", end="")
    x = int(input())
    a.append(x)
tong = sum(a)
#ham len()ham lay do dai: 
print("chieu dai cua cac phan tu : ", len(a))
print("tong cac phan tu la: ", tong)"""

#ham sorted() sap xep cac phan tu trong mang----
b = [1,5,4,3,2,7,6,9,8]
print(sorted(b))
#sap xep theo thu tu giam dan
print(sorted(b, reverse=True))
