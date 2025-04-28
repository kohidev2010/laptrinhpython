
#capitalize()------------------------------------
"""txt = "hello, and welcome to my world"
x = txt.capitalize()
print(x)"""

#casefold()------------------------------------
"""txt = "Hello, And Welcome To My World"
x = txt.casefold()
print(x)"""

#center()------------------------------------
"""txt = "banana"
x = txt.center(20)# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
print(x)"""
"""txt = "banana"
x = txt.center(20, "*")
print(x)"""

#count()------------------------------------
#Returns the number of times a specified value occurs in a string
"""txt = "I love apples, apples are my favorite fruit"
x = txt.count("apple")
print(x)"""

"""txt = "I love apples, apples are my favorite fruit"
x = txt.count("apple",10,24)
print(x)"""

#endswith()--------------------------------------
#endswith()dùng để kiểm tra xem một chuỗi có kết thúc bằng một chuỗi con nào đó không.
#Nó sẽ trả về True hoặc False.
"""txt = "document.txt"
x = txt.endswith(".txt")
print(x)"""
#Check if the string ends with either the phrase "world." or "castle.":
"""txt = "hello, welcome to my castle."
x = txt.endswith(("world.","castle."))
print(x)
"""
#expandtabs()--------------------------------------
#The expandtabs() method sets the tab size to the specified number of whitespaces.
"""txt = "H\te\tl\tl\to"
x = txt.expandtabs(4)
print(x)"""

#find()--------------------------------------
#find() dùng để tìm vị trí đầu tiên của một chuỗi con trong chuỗi gốc.
#Nếu tìm thấy, nó trả về chỉ số (index).
#Nếu không tìm thấy, nó trả về -1.

"""txt = "hello world"
x = txt.find("world")
print(x)"""

"""txt = "hello world"
x = txt.find("python")
print(x)"""

"""txt = "hello world hello"
x = txt.find("hello",7)
print(x)"""

#format()--------------------------------------
#format() dùng để chèn dữ liệu vào bên trong một chuỗi, thay thế các dấu {}.
"""txt = "{ is { years old."
print(txt.format("Alice",30))"""
"""
txt = "{0 loves {1, and {0 also loves {2."
print(txt.format("Tom","pizza","ice-cream"))"""

#index()--------------------------------------
#Phương thức index() tìm kiếm lần xuất hiện đầu tiên của giá trị được chỉ định.
"""The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)"""
"""txt = "hello, welcome to my world."
x = txt.index("welcome")
print(x)"""

#string isalnum()--------------------------------------
#Check if all the characters in the text are alphanumeric:
"""txt = "company12"
x = txt.isalnum()
print(x)"""

#isalpha()--------------------------------------
#Check if all the characters in the text is alphabetic:
"""txt = "CompanyX"
x = txt.isalpha()
print(x)"""

#isdecimal()--------------------------------------
"""txt = "1234"
x = txt.isdecimal()
print(x)"""
"""
userName = input("please enter your name:")
userN =userName.isalpha()
if (userN is True):
    userPassword = input("enter your pass word(must be greater than 10):")
    userP = userPassword.isalnum()
    if userN is True:
        confirmPassword = input("confirm your password")
        if (userPassword == confirmPassword):
            print("your pass is correct")
        else:
            print("it's is not correct")
    else:
        print("please enter again. your password is not reasonable")
else:
    print("username is not correct, username only must contain alphabetic. please try again")"""

#isdigit()--------------------------------------
#Ngoài số 0–9, còn hỗ trợ: số mũ, số nhỏ (ví dụ: ², ³) hoặc chữ số trong các ngôn ngữ khác
"""txt = "50800"
x = txt.isdigit()
print(x)"""

#isidentifier()--------------------------------------
#Nó kiểm tra xem chuỗi đó có phải là một "tên hợp lệ" (identifier) trong Python hay không
#Chỉ chứa chữ cái (a-z, A-Z), số (0-9), hoặc dấu gạch dưới _.
#Không được bắt đầu bằng số.
#Không chứa dấu cách, ký tự đặc biệt (@, #, !,...) hoặc ký tự không hợp lệ.
"""a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())"""

#lower()--------------------------------------
#Check if all the characters in the text are in lower case:
"""txt = "hello world"
x = txt.islower()
print(x)"""

"""a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())"""


#isnumeric()--------------------------------------
#Nó kiểm tra xem tất cả ký tự trong chuỗi có phải là số (số tự nhiên) hay không.
#Nếu tất cả ký tự là số ➔ trả về True.
#Nếu có ký tự nào không phải số ➔ trả về False.
"""s1 = "12345"
print(s1.isnumeric())"""#true
"""s2 = "123abc"
print(s2.isnumeric()) """#false

#isnumeric()	Cực kỳ rộng: 0–9, phân số, số La Mã, Unicode số	"Ⅻ", "⅕"	Rộng nhất
#isdecimal()	Chỉ số 0–9 thuần túy	"123"	Nghiêm ngặt nhất
#isdigit()	Số 0–9 và thêm các số Unicode như ², ³	"²"	Linh hoạt hơn
"""Tóm lại:
Nếu bạn chỉ cần kiểm tra số 0–9 bình thường: dùng isdecimal().
Nếu cần kiểm tra thêm các số Unicode như mũ nhỏ: dùng isdigit().
Nếu muốn kiểm tra kể cả số La Mã, phân số Unicode...: dùng isnumeric()."""

#isprintable()--------------------------------------
#Nó kiểm tra xem mọi ký tự trong chuỗi có phải là ký tự in được (có thể hiển thị ra màn hình) hay không
#Nếu tất cả các ký tự in được ➔ trả về True.
#Nếu có ký tự không in được (ví dụ: xuống dòng \n, tab \t, ký tự điều khiển...) ➔ trả về False
"""s1 = "hello world"
print(s1.isprintable())"""#True
"""s2 = "Hello\nworld"
print(s2.isprintable())"""#False
"""s3 = "12345"
print(s3.isprintable())"""#True
"""s4 = " "
print(s4.isprintable())#True(khoang trang van in duoc)
"""
"""s5 = "hello\tworld"
print(s5.isprintable())"""

