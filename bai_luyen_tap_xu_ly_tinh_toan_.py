# bài tập 2.1 : viết chương trình giá trị hàm số
# f(x)=e^x - X tại giá trị x = 0.501 và hiển thị kết quả ra màn hình
"""import math
x = 0.501
f = pow(math.e, x) -x #pow(2,3)=>2mu3
print(round(f,2))"""

#bài tập 2.2 viết chương trình cho người dùng nhập vào một số x bất kỳ sau
#đó tính và hiển thị(in) ra màn hình giá trị x^2,x^3,x^4
"""x_input = input("nhập giá trị x bất kì: ")
x = int(x_input)
import math"""
#print("giá trị x^2:{0}, x^3:{1}, và x^4:{2}".format(pow(x,2),pow(x,3),pow(x,4)))

#bài tập 2.3:viết chương trình cho người dùng nhập vào một số thực là 
#nhiệt độ , sau đó đổi sang nhiệt đọ C theo công thức sau
"""f = float(input("nhập nhiệt độ F: "))
c = (f - 32) / 1.8"""
#print("nhiệt độ c là: {}".format(round(c,2)))

#bài tập 2.5: write a python program to get a string consisting of the first characters and the last
#2 characters of a given string. if string length is less than 2,
#return empty string instead
character = input("enter a string:" )
if len(character) < 2:
    print("empty string")
else:
    fistTwo = character[0:2]
    lastTwo = character[-2:]
    print(fistTwo + lastTwo)