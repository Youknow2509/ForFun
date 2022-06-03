n = int(input("SO so trong day la: ")) #nhap
i=0
lst = []
#Nhap mang cac so
for i in range(n):
    lst.append(int(input("\nCac so trong day :")))
min_value = lst[0] #gan mot gia tri de so sanh
for i in lst:      #chay lai cac gia tri trong day
    if i < min_value:  #thuc hien phep toan
        min_value = i
print("So nho nhat trong day la",min_value)