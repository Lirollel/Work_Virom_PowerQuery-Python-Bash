import os
import re

print('hi')
data = open('data.txt', 'a')

# последовательное открытие папок в выбранной директории
for dir in os.listdir(os.getcwd()):
    if os.path.isdir(dir):
        print("Walking to the " + dir)
        path = os.getcwd() + "\\" + dir
        print(path)

# открытие файла out*.log
        for file in os.listdir(path):
            if re.match(r'out.*\.log$', file):
                print (file)
                open_file = open(path+'\\'+file,'r', encoding='utf-8')
                
# чтение строк
                strings = open_file.readlines()
                #print(strings)
                for string in strings:
                    if strings.index(string) in range(2) or strings.index(string) in range(37,49):
                        print(strings.index(string))
                        print(strings[strings.index(string)])
                        data.write(string)
                
                open_file.close()
data.close()




    

print("bi")