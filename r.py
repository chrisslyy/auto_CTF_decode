import os
import a
# os.system('assister.exe')
# os.system('del /a:H assister.exe')
value = a.ass()
#print(value)
with open('注册码.txt', 'w') as f:
    f.write(value)
print('注册码文件成功生成')
os.system('pause')
os.system('del *.zip')