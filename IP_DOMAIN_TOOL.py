# -*- coding: utf-8 -*-
import re
import requests
import argparse

def argument():
    parser = argparse.ArgumentParser(prog='IP_DOMAIN', description='IP——域名整理小工具 by白泽Sec_ahui')
    parser.add_argument('-f','--file',help=u'指定要处理的文件名，例如：-f C:\test.txt',type=argparse.FileType('r+'))
    global args
    args = parser.parse_args()
argument()
if not args.file:
    print(u"请指定要处理的域名——IP文件，例如：-f C:\test.txt")
    exit()
IP_DOMAIN=args.file
ip=open('ip.txt','w+')
domain=open('domain.txt','w+')
lines=IP_DOMAIN.readlines()
lines=sorted(list(set(lines)))
c_dict={}
b_dict={}
for str in lines:
    arr1 = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",str)
    arr2 = re.findall(r"[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?[a-zA-Z][-a-zA-Z]{0,62}",str)
    if (arr1):#c段整理功能还没写完
        for i in arr1:
            ip.write(i.strip()+'\n')
            c = re.findall('((?:\d*\.){2}(?:\d)*)',i.strip())
            for j in range(len(c)):
                if not c[j] in c_dict:
                    c_dict[c[j]] = 1
                else:
                    c_dict[c[j]] +=1
            b = re.findall('(^\d{0,3}.\d{0,3})',i.strip())
            for k in range(len(b)):
                if not b[k] in b_dict:
                    b_dict[b[k]] = 1
                else:
                    b_dict[b[k]] +=1
    elif(arr2):
        for i in arr2:
            domain.write(str.strip()+'\n')
ip.write((u"您搜索的结果共包含{}个C段，统计结果如下：\n".format(len(c_dict))).encode("GBK","ignore"))
c_dict=sorted(dict.items(c_dict), key=lambda item:item[1], reverse=True)
for i,j in (c_dict):
    ip.write((U"C段：{}.0/24\t\t{}条数据在此C段中\n".format(i,j)).encode("GBK","ignore"))

b_dict=sorted(dict.items(b_dict), key=lambda item:item[1], reverse=True)
ip.write((u"您搜索的结果共包含{}个B段，统计结果如下：\n".format(len(b_dict))).encode("GBK","ignore"))
for i,j in (b_dict):
    ip.write((U"B段：{}.0/16\t\t{}条数据在此B段中\n".format(i,j)).encode("GBK","ignore"))
