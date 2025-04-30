#1. giải và biện luận phương trình bậc nhất
#2. giải và biện luận phương trình bậc 2
#3. xác định số ngày trong tháng
#4. game kéo-búa-bao

#bài tập 1------------------------
# a != 0 có một nghiệm duy nhất -b/a
#a = 0, b = 0, phương trình vô số nghiệm
#a = 0 , b!= 0 phương trình vô nghiệm

"""a = int(input("nhập hằng số a: "))
b = int(input("nhập hằng số b: "))
if a != 0:
    print("phương trình có một nghiệm dn: ", (-b/a))
else:
    if a == 0 and b == 0:
        print("phương trình vô số nghiệm")
    if a == 0 and b != 0:
        print("phương trình vô nghiệm")"""


#bài tập số 2-----------------------------
#bước 1
#ax^2 +bx +c = 0
#x là hằng số
#a,b,c là hệ số thực, với a != 0, nếu a = 0 thì là phương trình bậc nhất
#bước 2
# tính delta
#delta = b^2 - 4ac
#del >0 có 2 nghiệm phân biệt: x1 = (-b+sqrt(delta))/2a, x2=(-b-sqrt(delta))/2a
#del = 0 x=-b/2a
#del <0 phương trình vô nghiệm
import math
a = int(input("nhập hệ số a: "))
b = int(input("nhập hệ số b: "))
c = int(input("nhập hệ số c: "))
if a == 0:
    print("đây là phương trình bậc nhất với a = 0")
else:
    delta = math.pow(b,2) - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        print("phương trình có 2 nghiệm x1:{0} và x2:{1}".format(x1,x2))
    if delta == 0:
        x = -b /2*a
        print ("phương trình có nghiệm x: ", x) 
    else:
        print("phương trình vô nghiệm")
