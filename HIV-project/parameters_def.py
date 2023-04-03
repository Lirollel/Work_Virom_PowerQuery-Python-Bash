# %matplotlib inline
from os import close
import matplotlib.pyplot as plt
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import json

def final_score(matches, all_symbols_in_seq, letters_in_seq, gaps_count_in_seq):

    y = (matches / all_symbols_in_seq) + (gaps_count_in_seq / letters_in_seq)
    return y 


with open ('records\mutations_DS\just_mutations.json', 'r') as file:
    data = json.load(file)
    
    for record in data:
        Reference = data[record]["POL sequence without mutations"]
        Sequence = data[record]["Protease"]["PR sequense"]

        openA = - 3
        extendA = 0
        openB = - 1
        extendB = 0

        for extendB in range (-1, 1):

            Alignment = pairwise2.align.localxd(Reference, Sequence, openA, extendA, openB, extendB, 
            one_alignment_only=True)

            gaps_symbols_in_ref = 0
            gaps_count_in_ref = 0
            letters_in_seq = 0
            gaps_symbols_in_seq = 0
            gaps_count_in_seq = 0

            for symbol in Alignment[0].seqA:
                if symbol == '-':
                    gaps_symbols_in_ref += 1
                    if Alignment[0].seqA[Alignment[0].seqA.index(symbol) + 1] != '-':
                        gaps_count_in_ref += 1
            
            matches = pairwise2.align.localxd(Reference, Sequence, openA, extendA, openB, extendB, one_alignment_only=True, score_only = True)

            for symbol in Alignment[0].seqB:
                if symbol == '-':
                    gaps_symbols_in_seq += 1
                    if Alignment[0].seqB[Alignment[0].seqB.index(symbol) + 1] != '-':
                        gaps_count_in_seq += 1
                elif symbol != '-':
                    letters_in_seq += 1

            all_symbols_in_seq = len(Alignment[0].seqB)

            if all_symbols_in_seq != letters_in_seq + gaps_symbols_in_seq:
                print('ошибка')

            Score = round(final_score(matches, all_symbols_in_seq, letters_in_seq, gaps_count_in_seq), 4)

            with open ('result.txt', 'a') as txt:
                txt.write('openA = ' + str(openA ) + ' ' +
                'extendA= ' + str(extendA) + ' ' +
                'openB= ' + str(openB) + ' ' +
                'extendB= ' + str(extendB) + '\n' +
                'Score = ' + str(Score) + '\n')
                txt.write(format_alignment(*Alignment[0]) + '\n' + '\n')
            
            plt.scatter(Score, extendB)
            plt.xlabel("Score") # ось абсцисс
            plt.ylabel("extendB") # ось ординат
            plt.grid() # включение отображение сетки
            plt.title('Оценка влияния параметра extendB на выравнивание') # заголовок
        
        plt.show()

        break