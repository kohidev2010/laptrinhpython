#các phép toán theo tác bit cơ bản
#phép toán AND (&)
#phép toán Or (|)
#phép toán XOR (^)
#phép toán NOT (~)
#toán tử bit
#dịch phải (>>)
#dịch trái bit (<<)

#AND(&)------------------------
"""a = 10 #1010
b = 2 #0010
print(a & b) """#0010
#=> 1&1=1 1&0=0 0&1=0 0&0=0
#OR(|)------------------------
"""a = 10 #1010
b = 2  #0010
print(a | b)"""
#=> 1|1=1, 1|0=1, 0|1=1, 0|0=0

#XOR(^)--------------------------
"""a = 10 #1010
b = 2 #00100010
print(a^b)"""
# 1^1=0, 1^0=1, 0^1=1, 0^0=0

#NOT(~)----------------------
"""a = 10 
b = 2 
print(~a)""" #-(n+1)

#Dịch trái bit (<<)
"""a = 10 #00001010
b = 2 
print(a << 1)""" #00010100
#==> cách tính nhanh: 10*2^n

#dịch phải bit (a >> 1)
a = 12 #00001010
b = 2 
print(a >> 2)
#==> cách tính nhanh: 12/2^n
