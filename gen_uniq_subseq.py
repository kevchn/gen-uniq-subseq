#!/usr/bin/env python
from Bio import SeqIO

motif_set = set()
handle = open("data/human_mature.fa", "rU")
for record in SeqIO.parse(handle, "fasta"):
    flag_motif_unique = False
    index_5p = 2
    motif = ""
    while(flag_motif_unique == False):
        motif = record.seq.back_transcribe()[index_5p:index_5p+10]
        if motif not in motif_set:
            flag_motif_unique = True
            motif_set.add(motif)
        index_5p += 1
    print(record.id + " " + motif)
    print(index_5p)
handle.close()
