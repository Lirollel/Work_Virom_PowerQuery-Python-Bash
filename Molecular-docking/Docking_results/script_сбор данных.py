import os
import re

print('Starting the work...')
# Получение полного пути к файлу скрипта
file_path = os.path.realpath(__file__)
# Получение директории, в которой находится файл скрипта
script_dir = os.path.dirname(file_path)
print("The script is in the dir: "+script_dir)

# Создание файла
data = open(str(script_dir) + "\\" + 'data.txt', 'x')
data.close()
# Открытие файла для записи
data = open(str(script_dir) + "\\" + 'data.txt', 'a')

# последовательное открытие папок в выбранной директории
for dir in os.listdir(script_dir):
    path = str(script_dir) + "\\" + str(dir)
    if os.path.isdir(path):
        print("Walking to the " + path)

# открытие файла out*.log
        for file in os.listdir(path):
            if re.match(r'out.*\.log$', file):
                print(file+" is opening")
                open_file = open(path+'\\'+file,'r', encoding='utf-8')
                data.write(file+"\n")
                
# чтение строк
                strings = open_file.readlines()
                #print(strings)
                for string in strings:
                    if strings.index(string) in range(2) or strings.index(string) in range(37,49):
                        # print(strings.index(string))
                        # print(strings[strings.index(string)])
                        data.write(string)
                
                open_file.close()
data.close()

print("The work has finished")