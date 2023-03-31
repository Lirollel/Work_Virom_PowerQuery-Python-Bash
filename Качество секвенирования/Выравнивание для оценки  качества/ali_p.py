from Bio import pairwise2
from Bio import SeqIO
import re
import os

reference = str(SeqIO.read("y:\Sequence\\2022\\ГБУЗ ТО ЦПБС\\KU749403_A6 pol2148.fasta", "fasta").seq)

for filename in os.listdir('y:\Sequence\\2022\\ГБУЗ ТО ЦПБС\\for_python'):
    link='y:\Sequence\\2022\\ГБУЗ ТО ЦПБС\\for_python\\'+str(filename)
    one_sequense_records = list(SeqIO.parse(link, "fasta"))
    
    for count in range (0,6):
        record = one_sequense_records[count]
        record_seq = str(record.seq)
        
        # удалить маленькие буквы
        record_seq_good = re.sub (r'[a-z]', '', record_seq)

        alignment = pairwise2.align.localmd(reference, record_seq_good, 
        match = 1, mismatch = 0, openA = -10, extendA = -9, openB = -2, extendB = -1, one_alignment_only=True)

        record_id = record.id
        start_id = alignment[0][3]

        
        # записать в файл
        with open ('results.txt', 'a') as txt:
            txt.write('record id\n' + str(record_id) +'\n' +
            'start position in ref\n' + str(start_id) +'\n')