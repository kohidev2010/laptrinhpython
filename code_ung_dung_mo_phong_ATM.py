tieuDe = "Máy Mô Phỏng ATM Rút Tiền"
print(tieuDe.center(40, "*"))

lsMenhGia = [500000,200000,100000,50000,20000,10000,5000,2000,1000]
tiepTuc = True
while(tiepTuc):
    soTienCanRut = int(input("nhập số tiền cần rút: "))
    soTo = 0
    for i in range(9):
        soTo = soTienCanRut // lsMenhGia[i]
        if soTo > 0:
            print(f"menh gia {lsMenhGia[i]}: {soTo} to")
            soTienCanRut = soTienCanRut % lsMenhGia[i]
    hoiNguoiDung = input("Bạn có muốn tiếp tục rút tiền không(yes/no): ")
    if hoiNguoiDung == "no":
        print("Xin chào bạn, hẹn gặp lại!")
        tiepTuc = False
