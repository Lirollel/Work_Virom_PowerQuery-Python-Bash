import json
from Bio import SeqIO


for record in SeqIO.parse("records\example.fasta", "fasta"):
    pol_seq = record.seq
    id_seq = record.id
    with open ('records\\bd.json', 'r') as file:
        data = json.load(file)
        data[id_seq]['POL_sequence'] = str(pol_seq)
        new=json.dumps(data, indent=2)
        with open ('records\\bd.json', 'w') as load_file:
            load_file.write(new)
