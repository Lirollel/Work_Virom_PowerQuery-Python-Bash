from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO

# функция подсчета штрафа за gap в Ref_seq
def gap_A_function(x, y):
    if y==0:
        return 0
    if y==1:
        return -30  
    return -20

# функция подсчета штрафа за gap в User_seq
def gap_B_function(x, y):
    if y==0:
        return 0
    if y==1:
        return -20
    if y%2==0:
        return -15
    if y%3==0:
         return -5
    if x in (2300, 2800):
        return 0
    return -20

# Парсинг файлов
for record in SeqIO.parse("seq.fasta", "fasta"):
    User_seq=record.seq

refs_id_dict={}
for record in SeqIO.parse("ref.fasta", "fasta"):
    refs_id_dict[str(record.seq)]=record.id
#print(refs_id_dict)

# Выбор лучшего референса
                         # ПРОГНАТЬ ПОСЛЕДОВАТЕЛЬНОСТИ ПО РЕГИОНУ ПОЛ
scores=[]
refs_score_dict={}
for Ref_seq in refs_id_dict.keys():
    alignment=pairwise2.align.localmd(Ref_seq, User_seq, 
    match=5, mismatch=-1, openA=-10, extendA=-10, openB=-5, extendB=-5, 
    one_alignment_only=True)
    #print(alignment)
    #print(pairwise2.format_alignment(aligment))
    scores+=[alignment[0].score]
    refs_score_dict[alignment[0].score]=alignment[0][0]

#print(scores)
max_score= max(scores) 
#print(max_score) 
print('Лучший рференс: '+ str(refs_id_dict[refs_score_dict[max_score]]))

alignment=pairwise2.align.localmc(refs_score_dict[max_score], User_seq, 
match=7, mismatch=-3, gap_A_fn=gap_A_function, gap_B_fn=gap_B_function)
print(format_alignment(*alignment))

    




#     # print('Варианты выравнивания для '+str(count)+' референса:')
#     # for aligment in alignments:
#     #     print(pairwise2.format_alignment(*aligment, full_sequences=True))



