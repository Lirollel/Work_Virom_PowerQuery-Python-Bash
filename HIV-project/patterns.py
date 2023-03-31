# from Bio import SeqIO
# records=list(SeqIO.parse('result\example.fasta', 'fasta'))
# record=records[0]
# for letter in record.seq:
#     prot_start_codon=''
#     for place in range(172,175):
#         prot_start_codon+=str(record.seq[place])
#         print(prot_start_codon)

# import json
# with open ('records\\bd.json', 'r') as file:
#     data = json.load(file)
#     print(data["01_AE.TH.1995.95TNIH022.AB032740"]["PR_length"])
#     data["01_AE.TH.1995.95TNIH022.AB032740"]['data'] = 'new'
# new=json.dumps(data, indent=2)
# with open ('records\\bd.json', 'w') as load_file:
#     load_file.write(new)


# from Bio import pairwise2
# pol_seq = '123456789'
# PR_seq = '456'
# alignment=pairwise2.align.localms(pol_seq, PR_seq, match=10, mismatch=-10, open=-10, extend=-10, one_alignment_only=True)
# PR_start = alignment[0][3] + 1
# PR_end = alignment[0][4]
# print(PR_start, PR_end)

# lst = ['1', '2', '3', '4']
# print(len(lst))

# dc = {'one':'1', 'two':'2', 'three':'3'}
# print(dc)
# dc['один'] = dc.pop('one')
# print(dc)

# a = 'строка'
# print(a)
# print(a[2])
# a = a[:1] + 'оро' + a[4:]
# print(a)

import random
# translation_data = {'A':['abc', 'bca', 'cba']}
# new_AC_codon = random.choice(translation_data['A'])
# print(str(new_AC_codon))

# lst = [1, 2, 3]
# lst2 = [4, 5]
# lst+=[4]
# print(lst)
# b = 3
# for a in range (1,6):
#     if a in lst:
#         print('a in lst')
#     if a in lst and b not in lst2:
#         print('a in lst and b not in lst2')


# print(type(int('3')))
# print(type(int('A')))

import re
from turtle import done
# text = 'L23V'
# match = re.findall(r'\d+', text)
# print(str(match[0]))

# del_list = ['D67S', 'S68K', 'T69M', 'K70Y', 'K70I']
# new = {}
# for i in del_list:
#     new [re.findall(r'\w\d+', i)[0]] =i [-1]
# del_list = []
# for key in list(new.keys()):
#     del_list += [str(key)+str(new[key])]
# print(new)
# print(del_list)


# PR_m_pos = random.sample (range(1,100), 15)
# print(PR_m_pos)

# drug_mut_PR = ['D1S', 'S35K', 'T69M', 'K15Y', 'K23I']
# mut_list_PR = ['D67S', 'S3K', 'T45M', 'K20Y', 'K200I']
# PR_random_mutations = ['D67S', 'S68K', 'T69M', 'K70Y', 'K70I']
# PR_lst_for_nums = [drug_mut_PR, mut_list_PR, PR_random_mutations]

# x = 2
# while x == 2:
#     PR_m_pos = random.sample (range(1,100), 15)

#     ran_drug_mut_PR = []
#     ran_mut_list_PR = []
#     R_random_mutations_PR = []


#     print(PR_m_pos)
#     for num in PR_m_pos:
#         print(num)
#         for lst in PR_lst_for_nums:
#             print(lst)
#             for m in lst:
#                 print(m)
                
#                 if int(re.findall(r'\d+', m)[0]) == num:

#                     созадние списков по именам
#                     if lst == drug_mut_PR:
#                         if len(ran_drug_mut_PR)<5: 
#                             ran_drug_mut_PR += [m] 
#                     if lst == mut_list_PR:
#                         if len(ran_mut_list_PR)<5: 
#                             ran_mut_list_PR += [m] 
#                     if lst == PR_random_mutations:
#                         R_random_mutations_PR += [m]
#                 if ran_drug_mut_PR != [] and ran_mut_list_PR != [] and R_random_mutations_PR != []:
#                     x +=1
#                 elif ran_drug_mut_PR ==[] or ran_mut_list_PR == [] or R_random_mutations_PR == []:
#                     continue
# print(ran_drug_mut_PR)
# print(ran_mut_list_PR)
# print(R_random_mutations_PR)

# dct = {}
# dct['P1'] = ['Y', 'D']
# print(dct)

# lst = []
# for key in dct.keys():
#     for item in dct[key]:
#         lst += [str(key+item)]  
# print(lst)

# dct = {'P1': ['Y', 'D', 'R'], 'P2': ['Y', 'D', 'R']}
# for key in list(dct.keys()):
#     val = random.choice(dct[key])
#     dct[key] = val
# print(dct)

# print('a')
# del_list_RT = {'D67': ['del'], 'S68': ['del'], 'T69': ['del'], 'K70': ['del']}
# RT_lst_for_nums = [del_list_RT]

# RT_m_pos = [69, 68, 70]

# ran_del_list_RT = {}

# for dct in RT_lst_for_nums:
                    
#     for num in RT_m_pos:

#         for m in dct.keys():
            
#             if int(re.findall(r'\d+', m)[0]) == num:

#                 # созадние списков по именам
#                 # вставка делеций
#                 if dct == del_list_RT:
#                     if len(list(ran_del_list_RT.keys()))<1: 
#                         val = dct[m]
#                         if m not in ran_del_list_RT.keys():
#                             ran_del_list_RT[m] = []
#                         ran_del_list_RT[m] += val
#                         RT_m_pos.remove(num)

# ran_del_list_RT_lst = []
# for key in ran_del_list_RT.keys():
#     for item in ran_del_list_RT[key]:
#         ran_del_list_RT_lst += [str(key+item)]  

# print(ran_del_list_RT_lst)

# def sus (x, y):
#     return x * y

# for x in range (0,5):
#     for y in range (1,3):
#         print(sus(x, y))

# for i in range (1,11):
#     print('i='+str(i))
#     for k in range (5, 7):
#         print('k='+str(k))
#         if i == k:
#             break
#     break

# for mismatch in range (0, -10):
#     print(mismatch)
# print('done')

# b = 'авария'
# print(b.index('и'))

# import matplotlib.pyplot as plt

# for i in range (1,11):
#     y = 2
#     plt.scatter(i, y)
# plt.show()


# def final_score(matches, 
# all_symbols_in_seq, letters_in_seq,
# gaps_count_in_seq, gaps_symbols_in_seq, 
# gaps_count_in_ref, gaps_symbols_in_ref):

#     k = 0

#     if gaps_symbols_in_seq % 3 == 0 and gaps_count_in_ref <= 2 and gaps_symbols_in_ref % 3 == 0:
#         k = 0.3
#     elif gaps_symbols_in_seq % 3 != 0 and gaps_count_in_ref <= 2 and gaps_symbols_in_ref % 3 == 0:
#         k = 0.6
#     elif gaps_symbols_in_seq % 3 != 0 and gaps_count_in_ref > 2:
#         k = 2
#     else:
#         k = 1

#     y = (matches / all_symbols_in_seq) + k * 100 * (gaps_count_in_seq / letters_in_seq)
#     return y 


# def final_score(matches, all_symbols_in_seq, letters_in_seq, gaps_count_in_seq):

#     y = (matches / all_symbols_in_seq) + (gaps_count_in_seq / letters_in_seq)
#     return y 

# from Bio import pairwise2

# from Bio.pairwise2 import format_alignment

# my_seq = 'AGACAGGCTAATTTTTTAGGGAGAATCTGGCCTTCCAGCAAAGGGAGGCCAGGGAATTTTCCTCAGAGCAGACCAGAGCCATCAGCCCCACCAGCAGAAATCTTGGGGATGGGGGAAGAGACAACCCCCTCCCTGAAACAGGAACAGAAAGACAGGGAACAGTATCCTCCTTCAATCTCCCTCAAATCACTCTTTGGCAACGACCCCTTGTCACAGTAAAAATAGGAGGACAGCTAAGGGAAGCTCTATTAGATACAGGAGCAGATGATACAGTATTAGAAGAAATAAATTTGCCAGGAAAATGGAAACCAAAAATGATAGGGGGAATTGGAGGTTTTATCAAAGTAAGACAATATGATCAGATACTTATAGAGATTTGTGGAAAAAAGGCTATAGGTACAGTATTAGTAGGACCTACCCCTGTCAACATAATTGGAAGGAATATGTTGACCCAGCTTGGTTGTACTTTAAATTTTCCAATAAGTCCTATTGAAACTGTACCAGTAACATTAAAGCCAGGAATGGATGGGCCAAAGGTTAAACAATGGCCATTRACAGAAGAGAAAATAAAAGCATTAACAGAAATTTGTCTGGAGATGGAAAAGGAAGGAAAAATTTCAAAAATTGGGCCTGAAAACCCATACAATACTCCAGTTTTTGCTATAAAGAAAAAGGACAGCACTAAGTGGAGAAAATTAGTAGATTTCAGAGAGCTCAATAAAAGAACTCAGGACTTTTGGGAAGTTCAATTAGGAATACCCCATCCAGCGGGTTTAAAAAGGAAAAAATCAGTAACAGTACTAGATGTAGGGGATGCATATTTTTCAGTTCCTCTACATGAAAGCTTCAGAAAATACACTGCATTCACTATACCAAGCACAAACAATGAGACCCCAGGAATCAGATATCAGTACAATGTGCTTCCACAGGGATGGAAAGGATCACCATCAATATTCCAGAGCAGCATGACAAAAATCTTAGAACCCTTTAGATCAAAAAATCCAGAGATAATTATCTATCAATACGTGGATGACTTATATGTAGGCTCTGATTTAGAAATAGGACAACATAGAGCAAAAATAGAGGAGTTAAGAGCTCATCTATTGAGCTGGGGATTTACTACACCAGACAAGAAGCATCAGAAAGAACCTCCATTTCTTTGGATGGGATATGAACTCCATCCTGACAAATGGACAGTCCAGCCTATAATGCTGCCAGAAAAAGACAGCTGGACTGTCAATGATATACAGAAATTAGTGGGAAAACTAAATTGGGCAAGTCAAATTTATGCAGGGA'
# mv_seq = 'AGTATCCTCCTTCAATCTCCCTCAAATCACTCTTTGGCAACGACCCCTTGTCACAGTAAAAATAGGAGGACAGCTAAGGGAAGCTCTATTAGATACAGGAGCAGATGATACAGTATTAGAAGAAATAAATTTGCCAGGAAAATGGAAACCAAAAATGATAGGGGGAATTGGAGGTTTTATCAAAGTAAGACAATATGATCAGATACTTATAGAGATTTGTGGAAAAAAGGCTATAGGTACAGTATTAGTAGGACCTACCCCTGTCAACATAATTGGAAGGAATATGTTGACCCAGCTTGGTTGTACTTTAAATTTTCCAATAAGTCCTATTGAAACTGTACCAGTAACATTAAAGCCAGGAATGGATGGGCCAAAGGTTAAACAATGGCCATTAACAGAAGAGAAAATAAAAGCATTAACAGAAATTTGTCTGGAGATGGAAAAGGAAGGAAAAATTTCAAAAATTGGGCCTGAAAACCCATACAATACTCCAGTTTTTGCTATAAAGAAAAAGGACAGCACTAAGTGGAGAAAATTAGTAGATTTCAGAGAGCTCAATAAAAGAACTCAGGACTTTTGGGAAGTTCAATTAGGAATACCCCATCCAGCGGGTTTAAAAAGGAAAAAATCAGTAACAGTACTAGATGTAGGGGATGCATATTTTTCAGTTCCTCTACATGAAAGCTTCAGAAAATACACTGCATTCACTATACCAAGCACAAACAATGAGACCCCAGGAGTCAGATATCAGTACAATGTGCTTCCACAGGGATGGAAAGGATCACCATCAATATTCCAGAGCAGCATGACAAAAATCTTAGAACCCTTTAGATCAAAAAATCCAGAGATAATTATCTATCAATACGTGGATGACTTATATGTAGGCTCTGATTTAGAAATAGGACAACATAGAGCAAAAATAGAGGAGTTAAGAGCTCATCTATTGAGCTGGGGATTTACTACACCAGACAAGAAGCATCAGAAAGAACCTCCATTTCTTTGGATGGGATATGAACTCCATCCTGACAAATGGACAGTCCAGCCTATAATGCTGCCAGAAAAAGACAGCTGGACTGTCAATGATATACAGAAATTAGTGGGAAAACTAAATTGGGCAAGTCAA'
# Alignment = pairwise2.align.localxx(my_seq, mv_seq, one_alignment_only=True)
# print(format_alignment(*Alignment[0]))