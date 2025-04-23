""" s = "\thello everyone. welcome to my channel \ntoday i'm going to teach you english"
print(s)
print("\' my name is loi\'")

print("--------------------------------")
s1 = "abc"
s2 = "def"
s3 = s1 + s2
s4 = "a" in s3
print(s4)
print("---------------------------")
a = "kohidev2010@gmail.com"
b = "@gmail.com"
if (b in a):
    print("gmail hop le")
else:
    print("gmail khong hop le")


print("------------------------------")

s = "Hello"
print(s[-1])
print_hello = s[0:5:1]
print(print_hello)
print(s[5:2:-1])

print("--------------------------")
s = "hello"
s1 = "c" + s[1:5]
print(s1)
*/"""
"""print ('----------------------------')
x = 10
y = 20
z = x + y"""
# print("gia tri cua a la %d \n gia tri cua b %d \n tong a va b la %d" %(x,y,z))

a = 10
b = 30
c = 45.5
s = "hello"
print("gia tri cua a la %d cua b %d cua c %.2f va s có nghia la %s "% (a,b,c,s))
print("gia tri cua a la {0}\n gia tri cua b la {1}\n gia tri cua c la {2}\n va chuoi s co nghia la {3}".format(a,b,c,s))