def load_fasta_dict(path):
    retdict = {}
    potentialseq = ''
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            if line.startswith('>'):
                key = line.strip()
                retdict[key] = ""
                if i != 0:
                    retdict[key] = potentialseq
                    potentialseq = ''
            if '>' not in line:
                potentialseq += line.strip()
        retdict[key] = potentialseq
    return retdict

def load_file_list(path):
    retlist = []
    with open(path, 'r') as f:
        for line in f:
            retlist += line.strip()
    return retlist

def load_fastaseq_list(path):
    retlist = []
    potentialseq = ''
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            if '>' not in line:
                potentialseq += line.strip()
            if '>' in line and i != 0:
                retlist.append(potentialseq)
                potentialseq = ''
        retlist.append(potentialseq)
    return retlist

codon_protein_dict = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",     
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "STOP",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "STOP",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "STOP",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}