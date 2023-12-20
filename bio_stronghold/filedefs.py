import builtins

def load_fasta_dict(path):
    retdict = {}
    with builtins.open(path, 'r') as f:
        for line in f:
            if line.startswith('>'):
                key = line.strip()
                retdict[key] = ""
            else:
                retdict[key] += line.strip()
    return retdict

def load_file_list(path):
    retlist = []
    with open(path, 'r') as f:
        for line in f:
            retlist += line.strip()
    return retlist

def load_fastaseq_list(path):
    retlist = []
    with open(path, 'r') as f:
        for line in f:
            if '>' not in line:
                retlist += line.strip()
    return retlist