#bài tập vận dụng
# yêu cầu người dùng nhập thông tin
# họ tên với chữ không số
# tuổi với số không chữ
#gmail với chữ và số và đuôi kết thúc @gmail
# password yêu cầu độ dài tối thiểu 10 kí tự bao gồm chữ in hoa a-z 0-9 và kí tự
#confirm pass nếu sai gõ lại qua 3 làn . pass sai cho tới khi in được
count_fname = 0
count_age = 0
while(True):
    fullName = input("nhap ho ten cua ban: ")
    if fullName.isalpha() == False:
        print("ban nhap sai ten! ")
    count_fname += 1
    if count_fname == 3:
        print("ban da nhap qua 3 lan hay coi lai thong tin")
        break         
    else: pass
while (True) :       
    age = input("nhap tuoi cua ban: ")
    if age.isdecimal() == False:
        print("ban nhap sai tuoi! ")
    count_age += 1
    if count_age == 3:
        print("ban da nhap qua 3 lan hay coi lai thong tin")
        break
    break            
    
        
    

#thongTin  = "Thong tin nguoi dung"
#print(thongTin.center(50, "*"))
