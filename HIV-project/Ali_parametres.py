from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import json


with open ('records\mutations_DS\just_mutations.json', 'r') as file:
    data = json.load(file)
    
    for record in data:
        Reference = data[record]["Protease"]["PR sequense without mutations"]
        Sequence = data[record]["Protease"]["PR sequense"]

        match = 1
        mismatch = 0
        openA = 0
        extendA = 0
        openB = 0
        extendB = 0


        
        
        
        break
        status_match = 'match in'
        for match in range (1, 11):
            if status_mismatch == 'mismatch out':
                Alignment = pairwise2.align.localmd(Reference, Sequence, 
                match, mismatch, openA, extendA, openB, extendB, 
                one_alignment_only=True)
                
                if len(Alignment[0].seqA) == len(data[record]["Protease"]["PR sequense"]):
                    
                    with open ('result.txt', 'a') as txt:
                        txt.write('match = ' + str(match) + ' '
                        'mismatch = ' + str(mismatch) + ' '
                        'openA = ' + str(openA ) + ' '
                        'extendA= ' + str(extendA) + ' '
                        'openB= ' + str(openB) + ' '
                        'extendB= ' + str(extendB) + '\n') 
                        txt.write(format_alignment(*Alignment[0]) + '\n' + '\n')
                    status_match = 'match out'
                    break
                
            elif status_match == 'match in':
                for mismatch in list(reversed(range (-10, 0))):
                    status_mismatch = 'mismatch in'
                    if status_openA == 'openA out':

                        Alignment = pairwise2.align.localmd(Reference, Sequence, 
                        match, mismatch, openA, extendA, openB, extendB, 
                        one_alignment_only=True)
                        
                        if len(Alignment[0].seqA) == len(data[record]["Protease"]["PR sequense"]):
                            
                            with open ('result.txt', 'a') as txt:
                                txt.write('match = ' + str(match) + ' '
                                'mismatch = ' + str(mismatch) + ' '
                                'openA = ' + str(openA ) + ' '
                                'extendA= ' + str(extendA) + ' '
                                'openB= ' + str(openB) + ' '
                                'extendB= ' + str(extendB) + '\n') 
                                txt.write(format_alignment(*Alignment[0]) + '\n' + '\n')
                            status_mismatch = 'mismatch out'

                        for openA in list(reversed(range (-10, 0))):
                            status_openA = 'openA in'
                            if status_extendA == 'extendA out':

                                Alignment = pairwise2.align.localmd(Reference, Sequence, 
                                match, mismatch, openA, extendA, openB, extendB, 
                                one_alignment_only=True)
                                
                                if len(Alignment[0].seqA) == len(data[record]["Protease"]["PR sequense"]):
                                    
                                    with open ('result.txt', 'a') as txt:
                                        txt.write('match = ' + str(match) + ' '
                                        'mismatch = ' + str(mismatch) + ' '
                                        'openA = ' + str(openA ) + ' '
                                        'extendA= ' + str(extendA) + ' '
                                        'openB= ' + str(openB) + ' '
                                        'extendB= ' + str(extendB) + '\n') 
                                        txt.write(format_alignment(*Alignment[0]) + '\n' + '\n')
                                    status_openA = 'openA out'

                                for extendA in list(reversed(range (openA, 0))):
                                    status_extendA = 'extendA in'
                                    if status_openB == 'openB out':
                                        
                                        Alignment = pairwise2.align.localmd(Reference, Sequence, 
                                        match, mismatch, openA, extendA, openB, extendB, 
                                        one_alignment_only=True)
                                        
                                        if len(Alignment[0].seqA) == len(data[record]["Protease"]["PR sequense"]):
                                            
                                            with open ('result.txt', 'a') as txt:
                                                txt.write('match = ' + str(match) + ' '
                                                'mismatch = ' + str(mismatch) + ' '
                                                'openA = ' + str(openA ) + ' '
                                                'extendA= ' + str(extendA) + ' '
                                                'openB= ' + str(openB) + ' '
                                                'extendB= ' + str(extendB) + '\n') 
                                                txt.write(format_alignment(*Alignment[0]) + '\n' + '\n')
                                            status_extendA = 'extendA out'
                                        

                                        for openB in list(reversed(range (-10, 0))):
                                            status_openB = 'openB in'
                                            if status_extendB == 'extendB out':
                                                
                                                Alignment = pairwise2.align.localmd(Reference, Sequence, 
                                                match, mismatch, openA, extendA, openB, extendB, 
                                                one_alignment_only=True)
                                                
                                                if len(Alignment[0].seqA) == len(data[record]["Protease"]["PR sequense"]):
                                                    
                                                    with open ('result.txt', 'a') as txt:
                                                        txt.write('match = ' + str(match) + ' '
                                                        'mismatch = ' + str(mismatch) + ' '
                                                        'openA = ' + str(openA ) + ' '
                                                        'extendA= ' + str(extendA) + ' '
                                                        'openB= ' + str(openB) + ' '
                                                        'extendB= ' + str(extendB) + '\n') 
                                                        txt.write(format_alignment(*Alignment[0]) + '\n' + '\n')
                                                    status_openB = 'openB out'
                                                    break

                                                for extendB in list(reversed(range (openB, 0))):
                                                    status_extendB = 'extendB in'
                                                    if status_extendB == 'extendB in':

                                                        Alignment = pairwise2.align.localmd(Reference, Sequence, 
                                                        match, mismatch, openA, extendA, openB, extendB, 
                                                        one_alignment_only=True)

                                                        if len(Alignment[0].seqA) == len(data[record]["Protease"]["PR sequense"]):
                                                            
                                                            with open ('result.txt', 'a') as txt:
                                                                txt.write('match = ' + str(match) + ' '
                                                                'mismatch = ' + str(mismatch) + ' '
                                                                'openA = ' + str(openA ) + ' '
                                                                'extendA= ' + str(extendA) + ' '
                                                                'openB= ' + str(openB) + ' '
                                                                'extendB= ' + str(extendB) + '\n') 
                                                                txt.write(format_alignment(*Alignment[0]) + '\n' + '\n')
                                                            status_extendB = 'extendB out'
                                                            break

                

                # match += 1
                # Alignment_2 = pairwise2.align.localmd(Reference, Sequence, 
                # match, mismatch, openA, extendA, openB, extendB, 
                # score_only=True, one_alignment_only=True)

                # if int(Alignment_1) == int(Alignment_2):
                #     match = match - 1
                #     for Alignment in pairwise2.align.localmd(Reference, Sequence, 
                #     match, mismatch, openA, extendA, openB, extendB, 
                #     one_alignment_only=True):
                #         with open ('result.txt', 'a') as txt:
                #             txt.write(format_alignment(*Alignment[0]) + '\n'
                #             'match = ' + str(match) + ' '
                #             'mismatch = ' + str(mismatch) + ' '
                #             'openA = ' + str(openA ) + ' '
                #             'extendA= ' + str(extendA) + ' '
                #             'openB= ' + str(openB) + ' '
                #             'extendB= ' + str(extendB) + '\n')
        print('Done')
        break
        
        # Parameters_list = ["match", "mismatch", "openA", "extendA", "openB", "extendB"]
        # for parameter in Parameters_list:
        #     if parameter == 'match':
        #         counter = 0
        #         index = -1
        #         for match in range (-10, 11):
        #             counter += 1
        #             index += 1
        #             if counter in range (1, len(range (-10, 11))):
        #                 Alignment_1 = pairwise2.align.localmd(Reference, Sequence, 
        #                 match, mismatch, openA, extendA, openB, extendB, 
        #                 score_only=True, one_alignment_only=True)

        #                 match += 1
        #                 Alignment_2 = pairwise2.align.localmd(Reference, Sequence, 
        #                 match, mismatch, openA, extendA, openB, extendB, 
        #                 score_only=True, one_alignment_only=True)

        #                 if int(Alignment_1) == int(Alignment_2):
        #                     match = match - 1
        #                     for Alignment in pairwise2.align.localmd(Reference, Sequence, 
        #                     match, mismatch, openA, extendA, openB, extendB, 
        #                     one_alignment_only=True):
        #                         with open ('result.txt', 'a') as txt:
        #                             txt.write(format_alignment(*Alignment[0]) + '\n'
        #                             'match = ' + str(match) + ' '
        #                             'mismatch = ' + str(mismatch) + ' '
        #                             'openA = ' + str(openA ) + ' '
        #                             'extendA= ' + str(extendA) + ' '
        #                             'openB= ' + str(openB) + ' '
        #                             'extendB= ' + str(extendB) + '\n')
        #                         break
                            

print('DONE')


# refs_id_dict={}
# for record in SeqIO.parse("ref.fasta", "fasta"):
#     refs_id_dict[str(record.seq)]=record.id

# scores=[]
# refs_score_dict={}
# for Ref_seq in refs_id_dict.keys():
#     alignment=pairwise2.align.localmd(Ref_seq, User_seq, 
#     match=5, mismatch=-1, openA=-10, extendA=-10, openB=-5, extendB=-5, 
#     one_alignment_only=True)
#     #print(alignment)
#     #print(pairwise2.format_alignment(aligment))
#     scores+=[alignment[0].score]
#     refs_score_dict[alignment[0].score]=alignment[0][0]