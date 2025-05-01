#cấu trúc lặp for------------------------
"""for <ten_bien> in <tap_hop>:
    <lenh trong for>
cau lenh tiep theo
"""
"""s = "hello" 
for character in s:
    print(character)"""
#lenh range----------------------------
#range(start, end, step)
"""for i in range(10):
    print("hoc cong nghe")"""
"""for i in range(1, 10,2):#nếu i = 10 sẽ ngừng vòng lặp
    print(i)"""
"""for i in range(10, 0, -1):
    print(i)"""

#bài tập ví dụ
"""n = int(input("enter n: "))
s = 0
for i in range (1, n + 1):
    s+=i
print(s)"""

#cấu trúc lặp while
"""while(<điều kiện>):
    <các lệnh trong while>"""
#trong khi điều kiện đúng thì các câu lệnh thực hiện trong while nếu sai sẽ thoát
"""i = 0
while (i <= 10):
    print(i)
    i+=2"""
    
#bài tập tính n! với n nhập từ bàn phím
"""n = int (input("nhập n:"))
i = 1
s = 1
while(i <= n):
    s = s * i
    i += 1
print(s)"""

#câu lệnh break
"""i = 1
while (i <= 10):
    print(i)
    i+=1
    if i == 6:
        break"""


# bài tập vận dụng----------------------------
#nhập và các số dương và tính tổng các số dương vừa nhập
#nếu gặp số âm thì thoát và in ra tổng các số dương vừa nhập
"""s = 0
while(True):
    n = int (input("nhap n: "))
    if (n < 0):
        break
    s += n
print(s)"""

# câu lệnh continue-----------------------
"""i = 1
while (i <= 10):
    i+=1
    print("xin chao")
    continue
    print("hoc cong nghe")"""
#bài tập tính tổng các số chẵn từ 1 đến n với n nhập từ bàn phím
"""n = int (input("nhap n: "))
s = 0
for i in range (1, n+1):
    if(i % 2 == 1):
        continue
    s += i
print(s)"""


   

