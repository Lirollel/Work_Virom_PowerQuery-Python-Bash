import json
import os

data_end={}
for filename in os.listdir('records\sybtypes_pr_rt_json'):
    link='records\sybtypes_pr_rt_json\\'+str(filename)
    with open(link, "r") as read_file:
        data = json.load(read_file)
        ID_seq = data['report']['inputSequence']['header']
        PR_seq = data['report']['alignedGeneSequences'][0]['alignedNAs']
        length_PR = data['report']['alignedGeneSequences'][0]['gene']['length']
        RT_seq = data['report']['alignedGeneSequences'][1]['alignedNAs']
        length_RT = data['report']['alignedGeneSequences'][1]['gene']['length']
        seq={}
        seq['PR_sequense']=PR_seq
        seq['PR_length']=length_PR
        seq['RT_sequense']=RT_seq
        seq['RT_length']=length_RT

        data_end[str(ID_seq)]=seq
  
new=json.dumps(data_end, indent=2)
with open ('records\\bd.json', 'a') as load_file:
    load_file.write(new)



