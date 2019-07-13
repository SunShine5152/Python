import random
secret = random.randint(1,10)
i = 0

while(i<3):
    temp = input("pls guess which is my number?")
    while(temp.isdigit()==False):
        print("input type error,input again")
        temp = input("input again")
    guess = int(temp)
    if guess == secret:
        print ('right!!!')
        break
    else:
        if guess >secret:
            print("big!!!")
        else:
            print("small!!!")
    i += 1            
print ("game over!")    
