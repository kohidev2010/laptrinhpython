#bài tập 3: xác định số ngày trong tháng
#tháng 2 năm nhuận thì có 29 ngày:
"""năm nhuận là năm có điều kiện là năm chia hết cho 4
nhưng không chia hết cho 100 hoặc chia hết cho 400"""
#2100 không phải là năm nhuận: tháng 2 có 28 ngày
#2000 là năm nhuận: tháng 2 có 29 ngày
#2020 là năm nhuận: tháng 2 có 29 ngày
#tháng 2 bình thường sẽ có 28 ngày
"""
month = int (input("nhập vào tháng: "))
year = int (input("nhập vào năm: "))
if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("tháng:", month,"có 31 ngày")
elif(month == 4 or month == 6 or month == 9 or month == 11):
    print("tháng:", month,"có 30 ngày")
else:
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print("tháng:", month,"có 29 ngày")
    else:
        print("tháng:", month,"có 28 ngày")"""



#bài tập số 4 : game kéo - búa - bao -----------------
#quy ước 1 - keo ; 2 - bua, 3 -bao
import random
robot = random.randint(1, 3) #may tinh se sinh ngau nhien tu 1 den 3
user = int(input("bạn định ra cái gì: "))
if(user == 1):
    if(robot == 1):
        print("hoa")
    elif(robot == 2):
        print("robot thang")
    else:
        print("ban thang")
elif (user == 2):
    if(robot == 1):
        print("ban thang")
    elif(robot == 2):
        print("hoa")
    else:
        print('robot thang')
else:
    if(robot == 1):
        print("robot thang")
    elif(robot == 2):
        print("ban thang")
    else:
        print("hoa")





