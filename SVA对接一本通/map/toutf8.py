#coding:utf-8

import sys

file_name = sys.argv[1]

with open(file_name,'r') as f:
    content = f.read()
    f.close()

with open(file_name,'w+') as f:
    content = content.decode('utf-16').encode('utf-8')
    f.write(content)
    f.close()
          
