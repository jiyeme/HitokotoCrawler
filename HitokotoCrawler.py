#!/usr/bin/env python3
import requests
import os
counter=1
list1=[]
time=int(input('输入请求次数'))
while counter<=time:
    print ('当前正在请求第 %d 次，共 %d 次' % (counter,time))
    gethitokoto = requests.get('https://sslapi.hitokoto.cn/?encode=text')
    text=gethitokoto.text
    textlong=len(text)
    if textlong<=100:
        list1.append(text)
        counter=counter+1
    else:
        print ('该字符串不符合要求，已经舍去，继续尝试下一次操作..')
else:
    print ('请求已完成')
    input ('按下Enter以列出请求数据,并把数据写入 output.txt')
    os.remove('output.txt')
    file=open('output.txt','a')
    for output in list1:
        print (output)
        file.write(output + '\n')
    file.close()
    input ('按下Enter键以退出')