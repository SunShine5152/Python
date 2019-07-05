f = open('record.txt')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        (role,line_spoken) = each_line.split(':',1);
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        filename_boy = 'boy_'+str(count)+'.txt'
        filename_girl = 'girl_'+str(count)+'.txt'

        file_boy = open(filename_boy,'w')
        file_girl = open(filename_girl,'w')

        file_boy.writelines(boy)
        file_girl.writelines(girl)


        file_boy.close()
        file_girl.close()

        boy = []
        girl = []
        count += 1


filename_boy = 'boy_'+str(count)+'.txt'
filename_girl = 'girl_'+str(count)+'.txt'

file_boy = open(filename_boy,'w')
file_girl = open(filename_girl,'w')

file_boy.writelines(boy)
file_girl.writelines(girl)


file_boy.close()
file_girl.close()

f.close()        
    
      
