from numpy import exp, cos, linspace
import os, time, glob
from Bio import SeqIO

def comp(a, b, c):
    mirna_set = set(c.data.splitlines())
    motif_size = b
    results = []
    motif_set = set()
    handle = open("data/sorted.human.mature.fa", "rU")
    for record in SeqIO.parse(handle, "fasta"):
        if record.id in mirna_set: # check if db mirna is one in user input
            index_5p = a-1
            flag_motif_unique = False
            motif = ""
            while(flag_motif_unique == False):
                motif = record.seq.back_transcribe()[index_5p:index_5p+motif_size]
                if motif not in motif_set:
                    flag_motif_unique = True
                    motif_set.add(motif)
                index_5p += 1
            pos = "pos:" + str(index_5p) + "-" + str(index_5p+10)
            results.append(">" + record.id + " " + motif + " " + pos)
            results.append(record.seq.back_transcribe())
        else:
            continue
    handle.close()
    return(results)
