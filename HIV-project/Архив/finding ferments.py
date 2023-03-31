import json
from Bio import SeqIO
from Bio import pairwise2

for record in SeqIO.parse("records\example.fasta", "fasta"):
    pol_seq = record.seq
    id_seq = record.id
    with open ('records\\bd.json', 'r') as file:
        data = json.load(file)
        # PR_seq = data[id_seq]["PR_sequense"]
        alignment = pairwise2.align.localms(pol_seq, data[id_seq]["PR_sequense"], match=10, mismatch=-10, open=-10, extend=-10, one_alignment_only=True)
        PR_start = alignment[0][3] + 1
        PR_end = alignment[0][4] 
        data[id_seq]['PR stars from'] = PR_start
        data[id_seq]['PR to'] = PR_end
        new=json.dumps(data, indent=2)
        with open ('records\\bd.json', 'w') as load_file:
            load_file.write(new)

