def load_fasta_dict(path):
    retdict = {}
    with open(path, 'r') as f:
        for line in f:
            if '>' in line:
                key = line
                retdict[key] = ""
            else:
                retdict[key] += line
    return retdict

def load_file_list(path):
    retlist = []
    with open(path, 'r') as f:
        for line in f:
            retlist += line
    return retlist

def load_fastaseq_list(path):
    retlist = []
    with open(path, 'r') as f:
        for line in f:
            if '>' not in line:
                retlist += line
    return retlist

print(load_fasta_dict("bio_stronghold/5_testfile.txt"))