from Bio import SeqIO
from Bio.Align import PairwiseAligner

# import matplotlib.pyplot as plt

record = list(SeqIO.parse("y:\Sequence\\2022\ГБУЗ ТО ЦПБС\\72_1045\\72.fas", "fasta"))
p1 = record[0].seq
p2 = record[1].seq
r1 = record[2].seq
r3 = record[3].seq
r3 = record[4].seq
r4 = record[5].seq
cons = record[6].seq
ref = SeqIO.read("y:\Sequence\\2022\\ГБУЗ ТО ЦПБС\\KU749403_A6 pol2148.fasta", "fasta").seq

# from collections import defaultdict

# channels = ["DATA9", "DATA10", "DATA11", "DATA12"]
# trace = defaultdict(list)
# for c in channels:
#     trace[c] = record.annotations["abif_raw"][c]

#     plt.plot(trace["DATA9"], color="blue")
#     plt.plot(trace["DATA10"], color="red")
#     plt.plot(trace["DATA11"], color="green")
#     plt.plot(trace["DATA12"], color="yellow")
#     plt.show()

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

aligner = PairwiseAligner()
aligner.mode = 'global'
alignments = aligner.align(ref, cons)

# for al in alignments:
#     print(al)

aligner.open_gap_score = -40
aligner.extend_gap_score = -2
aligner.target_end_gap_score = 0.0
aligner.query_end_gap_score = 0.0
# alignment = alignments[]
for ali in alignments:
    print(ali)
# print(dir(alignment))
# print(alignment.coordinates)

# for alignment in sorted(alignments):
#      print("Score = %.1f:" % alignment.score)
#      print(alignment)
# print(format_alignment(*Alignment[0]))
