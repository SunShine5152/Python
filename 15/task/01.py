'''
while True:
    str1 = input('请输入一个整数(输入Q结束程序):')
    if not str1 == 'Q':
        print ("十进制 -> 十六进制 :{0} -> {1}".format(str1,hex(int(str1))))
        print ("十进制 -> 八进制 :{0} -> {1}".format(str1,oct(int(str1))))
        print ("十进制 -> 二进制 :{0} -> {1}".format(str1,bin(int(str1))))
    else:
        break
'''
q = True
while q:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制 : %d -> 0x%x' % (num, num))
        print('十进制 -> 八进制 : %d -> 0o%o' % (num, num))
        print('十进制 -> 二进制 : %d -> ' % num, bin(num))
    else:
        q = False
