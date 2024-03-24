import filedefs

def graphs_overlap(file):
    seqlist = filedefs.load_fasta_dict(file)
    adjacency_list = []
    for suffixseq in seqlist:
        for prefixseq in seqlist:
            suffix = seqlist[suffixseq][-3:]
            prefix = seqlist[prefixseq][:3]
            if prefix == suffix:
                adjacency_list.append((suffixseq, prefixseq))
                print(suffixseq[1:], prefixseq[1:])
    return adjacency_list

testfile = '/Users/ameliadayton/Downloads/rosalind_grph(4).txt'
adjlist = graphs_overlap(testfile)