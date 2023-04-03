import json
import random
import re

# формирование списков мутаций из БД
with open ('records\\hivmutdb.json', 'r') as file:
    data = json.load(file)

    drug_mut_PR = {}
    drug_mut_RT = {}
    mut_list_PR = {}
    mut_list_RT = {}
    PR_random_mutations = {}
    RT_random_mutations = {}
    count = -1
    for position in data["hivmutdb"]:
        mut_dict = {}
        count +=1 
        mut_dict[str(data["hivmutdb"][count][0])] = list(data["hivmutdb"][count][1].keys())

        if data["hivmutdb"][count][1] != {}:
            for letter in list(data["hivmutdb"][count][1].keys()):

                if letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    mut_dict[str(data["hivmutdb"][count][0])].remove(letter)
                
            if data["hivmutdb"][count][1][letter] != [] and count in range (0, 99):
                # мутация ЛУ в ПР
                drug_mut_PR = drug_mut_PR | mut_dict
            if data["hivmutdb"][count][1][letter] != [] and count in range (99, 659):
                # мутация ЛУ в РТ
                drug_mut_RT = drug_mut_RT | mut_dict
            if data["hivmutdb"][count][1][letter] == [] and count in range (0, 99):
                # обычная мутация в ПР
                mut_list_PR = mut_list_PR | mut_dict
            if data["hivmutdb"][count][1][letter] == [] and count in range (99, 659):
                # обычная мутация в ПР
                mut_list_RT = mut_list_RT | mut_dict

    turn = [drug_mut_PR, mut_list_PR, drug_mut_RT, mut_list_RT]
    for dct in turn:
        lst = []
        for key in list(dct.keys()):
            for item in dct[key]:
                lst += [str(key+item)]
            if dct == drug_mut_PR:
                drug_mut_PR_lst = lst 
            if dct == mut_list_PR:
                mut_list_PR_lst = lst 
            if dct == drug_mut_RT:
                drug_mut_RT_lst = lst 
            if dct == mut_list_RT:
                mut_list_RT_lst = lst 
    
    Huge_mutation_list = drug_mut_PR_lst + drug_mut_RT_lst + mut_list_PR_lst + mut_list_RT_lst
    
    # список случайных муктаций
    PR_acids_num = []
    RT_acids_num = []
    count=-1
    for mutation in data["hivmutdb"]:
        count+=1
        if count in range (0, 99):
            PR_acids_num+=[str(data["hivmutdb"][count][0])]
        if count in range (99, 659):
            RT_acids_num+=[str(data["hivmutdb"][count][0])]

    with open ('records\\translation.json', 'r') as translation:
        translation_data = json.load(translation)
        acids_2 = list(translation_data.keys())
        del acids_2[-1]

        for acid_num in PR_acids_num:
            for acid_2 in acids_2:
                if acid_2 != acid_num[0]:
                    mutation = str(acid_num) + str(acid_2)
                    if mutation not in Huge_mutation_list:
                        if acid_num not in PR_random_mutations.keys():
                            PR_random_mutations[acid_num] = []
                        PR_random_mutations[acid_num] += [acid_2]
        
        for acid_num in RT_acids_num:
            for acid_2 in acids_2:
                if acid_2 != acid_num[0]:
                    mutation = str(acid_num) + str(acid_2)
                    if mutation not in Huge_mutation_list:
                        if acid_num not in RT_random_mutations.keys():
                            RT_random_mutations[acid_num] = []
                        RT_random_mutations[acid_num] += [acid_2]

del_list_RT = {'D67': ['del'], 'S68': ['del'], 'T69': ['del'], 'K70': ['del']}
ins_list_RT = {'T69': ['ins']}

with open ('records\mutations_DS\del_random.json', 'r') as file:
    data = json.load(file)

    keys_list = list(data.keys())
    
    for sequence in keys_list:
        # выбор случаных мутаций для каждой последовательности
        PR_lst_for_nums = [drug_mut_PR, mut_list_PR, PR_random_mutations]
        RT_lst_for_nums = [del_list_RT, drug_mut_RT, mut_list_RT, RT_random_mutations]
        
        # Подбор мутаций для протеазы
        x = 2
        while x == 2:
            PR_m_pos = random.sample (range(1,100), 15)

            ran_drug_mut_PR = {}
            ran_mut_list_PR = {}
            R_random_mutations_PR = {}

            for dct in PR_lst_for_nums:
                                
                for num in PR_m_pos:

                    for m in dct.keys():
                        
                        if int(re.findall(r'\d+', m)[0]) == num:

                            # созадние списков по именам
                            if dct == drug_mut_PR:
                                if len(list(ran_drug_mut_PR.keys()))<5: 
                                    val = random.choice(dct[m])
                                    if m not in ran_drug_mut_PR.keys():
                                        ran_drug_mut_PR[m] = []
                                    ran_drug_mut_PR[m] += val
                                    PR_m_pos.remove(num)

                            if dct == mut_list_PR:
                                if len(list(ran_mut_list_PR.keys()))<5: 
                                    val = random.choice(dct[m])
                                    if m not in ran_mut_list_PR.keys():
                                        ran_mut_list_PR[m] = []
                                    ran_mut_list_PR[m] += val
                                    PR_m_pos.remove(num)

                            if dct == PR_random_mutations:
                                val = random.choice(dct[m])
                                if m not in R_random_mutations_PR.keys():
                                    R_random_mutations_PR[m] = []
                                R_random_mutations_PR[m] += val
                                
                        if ran_drug_mut_PR != {} and ran_mut_list_PR != {} and R_random_mutations_PR != {}:
                            x +=1
                        elif ran_drug_mut_PR == {} or ran_mut_list_PR == {} or R_random_mutations_PR == {}:
                            continue

        # Подбор мутаций для ривертазы
        x = 2
        while x == 2:
            RT_m_pos = random.sample (range(1,100), 19)

            ran_drug_mut_RT = {}
            ran_mut_list_RT = {}
            R_random_mutations_RT = {}
            ran_del_list_RT = {}

            for dct in RT_lst_for_nums:
                                
                for num in RT_m_pos:

                    for m in dct.keys():
                        
                        if int(re.findall(r'\d+', m)[0]) == num:

                            # созадние списков по именам
                            # вставка делеций
                            if dct == del_list_RT:
                                if len(list(ran_del_list_RT.keys()))<5: 
                                    val = dct[m]
                                    if m not in ran_del_list_RT.keys():
                                        ran_del_list_RT[m] = []
                                    ran_del_list_RT[m] += val
                                    RT_m_pos.remove(num)

                            if dct == drug_mut_RT:
                                if len(list(ran_drug_mut_RT.keys()))<5: 
                                    val = random.choice(dct[m])
                                    if m not in ran_drug_mut_RT.keys():
                                        ran_drug_mut_RT[m] = []
                                    ran_drug_mut_RT[m] += val
                                    RT_m_pos.remove(num)

                            if dct == mut_list_RT:
                                if len(list(ran_mut_list_RT.keys()))<5: 
                                    val = random.choice(dct[m])
                                    if m not in ran_mut_list_RT.keys():
                                        ran_mut_list_RT[m] = []
                                    ran_mut_list_RT[m] += val
                                    RT_m_pos.remove(num)

                            if dct == RT_random_mutations:
                                val = random.choice(dct[m])
                                if m not in R_random_mutations_RT.keys():
                                    R_random_mutations_RT[m] = []
                                R_random_mutations_RT[m] += val
                                
                        if ran_drug_mut_RT != {} and ran_mut_list_RT != {} and R_random_mutations_RT != {} and ran_del_list_RT!= {}:
                            x +=1
                        elif ran_drug_mut_RT == {} or ran_mut_list_RT == {} or R_random_mutations_RT == {} or ran_del_list_RT == {}:
                            continue

        # внесение значений в БД
        ran_drug_mut_PR_lst = []
        for key in ran_drug_mut_PR.keys():
            for item in ran_drug_mut_PR[key]:
                ran_drug_mut_PR_lst += [str(key+item)]  
        data[sequence]['Protease']["DrugR mutations"] =  ran_drug_mut_PR_lst

        ran_mut_list_PR_lst = []
        for key in ran_mut_list_PR.keys():
            for item in ran_mut_list_PR[key]:
                ran_mut_list_PR_lst += [str(key+item)]  
        data[sequence]['Protease']["Simple mutations"] =  ran_mut_list_PR_lst
        
        ran_drug_mut_RT_lst = []
        for key in ran_drug_mut_RT.keys():
            for item in ran_drug_mut_RT[key]:
                ran_drug_mut_RT_lst += [str(key+item)]  
        data[sequence]['Reverse Transcriptase']["DrugR mutations"] =  ran_drug_mut_RT_lst
        
        ran_mut_list_RT_lst = []
        for key in ran_mut_list_RT.keys():
            for item in ran_mut_list_RT[key]:
                ran_mut_list_RT_lst += [str(key+item)]  
        data[sequence]['Reverse Transcriptase']["Simple mutations"] =  ran_mut_list_RT_lst
        
        R_random_mutations_PR_lst = []
        for key in R_random_mutations_PR.keys():
            for item in R_random_mutations_PR[key]:
                R_random_mutations_PR_lst += [str(key+item)]  
        data[sequence]['Protease']["Random mutations"] =  R_random_mutations_PR_lst
       
        R_random_mutations_RT_lst = []
        for key in R_random_mutations_RT.keys():
            for item in R_random_mutations_RT[key]:
                R_random_mutations_RT_lst += [str(key+item)]  
        data[sequence]['Reverse Transcriptase']["Random mutations"] = R_random_mutations_RT_lst

        ran_del_list_RT_lst = []
        for key in ran_del_list_RT.keys():
            for item in ran_del_list_RT[key]:
                ran_del_list_RT_lst += [str(key+item)]  
        data[sequence]['Reverse Transcriptase']["Deletions"] = ran_del_list_RT_lst

        # выбор мутации, поиск кодона в рефе, выбор кодона мутации
        turn = [ran_drug_mut_PR_lst, ran_mut_list_PR_lst, ran_drug_mut_RT_lst, ran_mut_list_RT_lst, R_random_mutations_PR_lst, R_random_mutations_RT_lst, ran_del_list_RT_lst]
        
        for mutations_list in turn:

            for mut in mutations_list:

                mut_number = int(re.findall(r'\d+', mut)[0])
                new_AC = mut[-1]

                f_codon_number = mut_number*3-3

                if mutations_list == ran_del_list_RT_lst:
                    data[sequence]['Reverse Transcriptase']["RT sequense"] = data[sequence]['Reverse Transcriptase']["RT sequense"][0:f_codon_number] + '---' + data[sequence]['Reverse Transcriptase']["RT sequense"][f_codon_number+3:]
                else:

                    with open ('records\\translation.json', 'r') as translation:
                        translation_data = json.load(translation)
                        new_AC_codon = str(random.choice(translation_data[new_AC]))

                    if mutations_list == ran_drug_mut_PR_lst or mutations_list == ran_mut_list_PR_lst or mutations_list == R_random_mutations_PR_lst:
                        data[sequence]['Protease']["PR sequense"] = data[sequence]['Protease']["PR sequense"][:f_codon_number] + new_AC_codon + data[sequence]['Protease']["PR sequense"][f_codon_number+3:]
                    if mutations_list == ran_drug_mut_RT_lst or mutations_list == ran_mut_list_RT_lst or mutations_list == R_random_mutations_RT_lst:
                        data[sequence]['Reverse Transcriptase']["RT sequense"] = data[sequence]['Reverse Transcriptase']["RT sequense"][0:f_codon_number] + new_AC_codon + data[sequence]['Reverse Transcriptase']["RT sequense"][f_codon_number+3:]

        # Переименовывание последовательности
        new_name = str(sequence[-8:-1]) + str(sequence[-1])
        if ran_del_list_RT_lst in turn:
            for deletion in ran_del_list_RT_lst:
                new_name += '_'
                new_name += deletion
        data[new_name] = data.pop(sequence)
    
new = json.dumps(data, indent=2)
with open ('records\mutations_DS\del_random.json', 'w') as load_file:
        load_file.write(new)
print('DONE')

