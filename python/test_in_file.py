import time 


f = open("hinhgau.txt")
i=1
while True: 
    a = f.readline(i)
    print(a)
    i+=i
    time.sleep(0.5)
    # in thử text
    