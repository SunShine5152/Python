answer = 'FishC.com'
chance_num = 3
i=0
while chance_num > 0:
    secret = input("请输入密码:")
    for each in secret:    
        if each == '*':
            print('密码中不能含有"*"号!您还有',chance_num,'次机会!')
            break
        elif each != answer[i]:
            print('密码输入错误!您还有',chance_num-1 ,'次机会!')
            chance_num -= 1
            break        
        elif i == (len(answer)-1):
            print('密码正确,进入程序.....')
            chance_num -= 1
            break
        i += 1
        print('i=',i)
else:
    print('机会用完了!!!')            


'''
count = 3
password = 'FishC.com'

while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count-1, '次机会！', end=' ')    
    count -= 1
'''
