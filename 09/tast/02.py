

for num in range(100,1000):
    i = num//100
    j = num//10 - i*10
    k = num %10
    l = i**3 + j**3 + k**3
    if num == l:
        print('num=',num)
    

        
    
'''
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)
'''        
