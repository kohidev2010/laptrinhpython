"""1. viết chhương trình tính s = x^2 +x^4+...+x^2n"""
"""2. Một người tiết kiệm được 10 triệu đồng và quyết định đi gửi ngân hàng, với 
lãi suất gửi tiết kiệm là 1%/tháng . hãy viết chương trình tính số tiền người này sẽ nhận được ssau 5 năm giả sử trong khoảng thời gian đó người này
không thực hiện giao dịch rút tiền nào ở ngân hàng"""
"""3. xây dựng chương trình nhập vào 2 số nguyên từ bàn phím , hiển thị ra màn hình ước chung lớn nhất của 2 số đó"""
"""4. viết chương trình nhập vào giờ ,phút, giây và một số giây là không từ bàn phím, sau đó cộng thêm k giây vào giờ phút giây vừa nhập.
hãy in giờ phút giây sau khi cộng thêm k giây vào"""
"""5. xây dựng chương trình nhập một số nguyên n từ bàn phím, cho biết n có bao nhiêu chữ
số và  tính tổng các chữ số của nó"""

#bai tap 1
"""import math
s = 0
x = int(input("x = "))
n = int(input("n = "))
for i in range(2,2 * n + 1, 2):
    s += math.pow(x,i)
print(s)"""


#bai tap 2
"""tongTien = 10000000
laiHangThang = 0
for i in range(1, 61):
    laiHangThang= tongTien * 0.01
    tongTien = tongTien + laiHangThang
print(round(tongTien,2))"""


#bai tap 3
"""a = int(input("a = "))
b = int(input("b = "))
if a < b:
    a, b = b, a
for i in range (b, 0, -1):
    if (a % i == 0 and b % i == 0):
        ucln = i
        break
print(ucln)"""