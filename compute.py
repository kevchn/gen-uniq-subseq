from numpy import exp, cos, linspace
import os, time, glob
from Bio import SeqIO

def comp(a, b):
    motif_size = b
    results = []
    motif_set = set()
    handle = open("data/human_mature.fa", "rU")
    for record in SeqIO.parse(handle, "fasta"):
        index_5p = a-1
        flag_motif_unique = False
        motif = ""
        while(flag_motif_unique == False):
            motif = record.seq.back_transcribe()[index_5p:index_5p+motif_size]
            if motif not in motif_set:
                flag_motif_unique = True
                motif_set.add(motif)
            index_5p += 1
        results.append(">" + record.id + " " + motif)
        results.append(record.seq.back_transcribe())
        results.append("pos:" + str(index_5p) + "-" + str(index_5p+10))
    handle.close()
    return(results)

if __name__ == '__main__':
    print(comp(1, 0.1, 1, 20))
