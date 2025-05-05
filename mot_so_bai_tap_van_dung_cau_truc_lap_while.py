"""1. viết chhương trình tính s = x^2 +x^4+...+x^2n"""
"""2. Một người tiết kiệm được 10 triệu đồng và quyết định đi gửi ngân hàng, với 
lãi suất gửi tiết kiệm là 1%/tháng . hãy viết chương trình tính số tiền người này sẽ nhận được ssau 5 năm giả sử trong khoảng thời gian đó người này
không thực hiện giao dịch rút tiền nào ở ngân hàng"""
"""3. xây dựng chương trình nhập vào 2 số nguyên từ bàn phím , hiển thị ra màn hình ước chung lớn nhất của 2 số đó"""
"""4. viết chương trình nhập vào giờ ,phút, giây và một số giây là không từ bàn phím, sau đó cộng thêm k giây vào giờ phút giây vừa nhập.
hãy in giờ phút giây sau khi cộng thêm k giây vào"""
"""5. xây dựng chương trình nhập một số nguyên n từ bàn phím, cho biết n có bao nhiêu chữ
số và  tính tổng các chữ số của nó"""

#bai tap 3 (phep toan tru)
"""a = int(input("a = "))
b = int(input("b = "))

# dung phap toan tru
while(a!=b):
    if (a > b):
        a -= b
    else:
        b -= a
print(a)"""


#bai tap 4
"""h = int(input("nhap gio: "))
m = int(input("nhap phut: "))
s = int(input("nhap giay: "))
k = int(input("nhap vao so giay cong them: "))"""

#cach 1- khong dung vong lap
"""toTalS= h * 3600 + m * 60 + s + k #tong so giay
hNew = toTalS // 3600
mNew = (toTalS - hNew * 3600) // 60
sNew = toTalS - hNew*3600 -mNew * 60
print(hNew, mNew, sNew)"""

#bai tap 5

n = int (input("n = "))
dem = 0
s = 0
while (n != 0):
    i = n % 10 #lay duoc so hang don vi
    s += i
    n //= 10
    dem += 1
print(s, dem)
