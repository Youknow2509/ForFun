n = int(input())
a = n
answer1 = 0
answer2 = 0

while n>= 1:
    answer1 +=n
    n -=1
print(answer1)

for i in range (1, a+1):
    answer2 +=i
print(answer2)
