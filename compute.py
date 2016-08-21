from numpy import exp, cos, linspace
import os, time, glob
from Bio import SeqIO

def unpack_to_set(textarea):
    return set(textarea.data.splitlines())

def generate_unique_subsequences(index_5p_begin, motif_size, mirna_set):
    """Return

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.

    Returns:
    """
    results = []
    motif_set = set()
    handle = open("data/sorted.human.mature.fa", "rU")
    for record in SeqIO.parse(handle, "fasta"):
        index_5p = index_5p_begin - 1
        while True:
            motif = record.seq.back_transcribe()[index_5p:index_5p+motif_size]
            if motif not in motif_set:
                motif_set.add(motif)
                break
            else:
                index_5p += 1
                if index_5p+motif_size == len(record.seq):
                    motif = "NO-UNIQUE-MOTIF-FOUND"
                    break
        pos = "pos:" + str(index_5p+1) + "-" + str(index_5p+motif_size+1)
        if record.id in mirna_set:
            results.append(">" + record.id + " " + motif + " " + pos)
            results.append(record.seq.back_transcribe())
    handle.close()
    return(results)
