import os

print('Скрипт начал свое выполнение')
# Получение полного пути к файлу скрипта
file_path = os.path.realpath(__file__)
# Получение директории, в которой находится файл скрипта
script_dir = os.path.dirname(file_path)
print("Скрипт работает в папке: "+script_dir)

# data = open('data.txt', 'a')
nucleotides_dict = {0: 'G', 1: 'A', 2: 'T', 3: 'C'}

# открытие файла *.txt
for file in os.listdir(script_dir):
    if file.endswith(".txt"):
        print("Будет открыт файл "+file)
        open_file = open(script_dir+'\\'+file,'r', encoding='utf-8')
        
# чтение строк
        strings = open_file.readlines()
        for string in strings:
            if strings.index(string)!=0:
             
                line_dict_values=string.split(  )
                line_dict_values = [int(item) for item in line_dict_values]
                # print(line_dict)
                # print(max(line_dict))
                
                percent_list=[]
                try:
                    for value in line_dict_values:           
                        percent_list.append(value/max(line_dict_values))
                    for ithrough_values in percent_list:
                        if ithrough_values == 1:
                            percent_list.remove(ithrough_values)
                    # print(percent_list)
                    if max(percent_list)<0.51:
                            print(nucleotides_dict[line_dict_values.index(max(line_dict_values))], end='')
                    else:
                        print("N", end='')
                except ZeroDivisionError:
                    print("N", end='')
        #print(strings)
        # for string in strings:
        #     print(str(strings.index(string))+string)
            
            # if strings.index(string) in range(2) or strings.index(string) in range(37,49):
            #     print(strings.index(string))
            #     print(strings[strings.index(string)])
            #     data.write(string)
        
        # open_file.close()
# data.close()




    

# print("bi")