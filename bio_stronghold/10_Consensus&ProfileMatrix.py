import filedefs

def consensus_profilematrix(file):
    seqlist = filedefs.load_fastaseq_list(file)
    seqlen = len(seqlist[0])
    profilematrix = {
        'A': [0 for nt in range(seqlen)],
        'C': [0 for nt in range(seqlen)],
        'G': [0 for nt in range(seqlen)],
        'T': [0 for nt in range(seqlen)],
        }
    for seq in seqlist:
        for i, nt in enumerate(seq):
            profilematrix[nt][i] += 1
            
    consensus = ''
    for i in range(seqlen):
        potential_nt = ['', 0]
        for nt in 'ACGT':
            if potential_nt[1] < profilematrix[nt][i]:
                potential_nt[0] = nt
                potential_nt[1] = profilematrix[nt][i]
        consensus += potential_nt[0]
    return consensus, profilematrix

def return_consensus_profilematrix(consensus, profilematrix):
    print(consensus)
    for nt in 'ACGT':
        print(f"{nt}: {' '.join(map(str, profilematrix[nt]))}")

testfile = '/Users/ameliadayton/Downloads/rosalind_cons(1).txt'
consensus, profilematrix = consensus_profilematrix(testfile)
return_consensus_profilematrix(consensus, profilematrix)