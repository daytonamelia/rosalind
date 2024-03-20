def revcomp(s, RNA=False):
    comps = {'A': 'T', 
             'T': 'A',
             'C': 'G',
             'G': 'C'}
    if RNA is True:
        comps['A'] = 'U'
        comps['U'] = 'A'
    return "".join(comps.get(base) for base in reversed(s))

teststr = 'CTGTCAGCACCGACCTCGCATGAGGCCATGAGGGACTTCAATGTGATGTATGACAGTTTTACACAGGCTGAAAGGCCACTCGATATCCTGGGCTAACGTCGAATTCCTGATATACACTCGCTGTAAGGGGTGGAATAAACCGGGCATGCTCCGAATGCATCGACGACAGTAAATGCTCATTTTCAGGACATTCTGTACAAGAAATCCCGCGTTAACCTATGCACAGACATAATGAAGAAGTCTGTATAAAGTGTGTCACAGCAAAATCCAACACCATCTTATTCATGGCGGTGAGTTTCAAGTGCAAGTGGTCGCGCGGGACTTGAGTCAACATGACTTACTCCTGCAACTGGGACGGCTCACGGCCCCTTTCCTTCCACGCCTCTCCCGCATCAGCAGCGGGAAAGATAGCCGCGCTCTAGCCAGTGAGGTAAGCGCTTTCCAGCATTGATAGATGAAAGTGACGAGTAGATATCTCACTATGCGGTGGACTTCGACGTCCGGCAATTCTAAAAAGCCGAAACGATACTAGGGGCTATGTGCAAGACATGTCTGTCTGGGGCCGGTTTACTTCTGTAGACTACAACGTGTCCCGTTGCCGGGCCCCTGCTACATTGATTGATTCCCTAGGCCCCTCAACCCACGGCGTTAAAGTGTGTACAACTGACGTCTACTCTCGCTTGACCAAAATCCGGCTTGACGCATTGATCAAATACCAAATCTGCCCGTAGACACGCTCCCGATCTAAGACACATAACCGTAAATGGGGTCTTTCGACGATTATAGTTTTTTTTCGCTCGGTTCCTATGATGACTTCGAGGGCCGCGTTGACGACCCAATCTATTTAAGTCAGTCTGG'

print(revcomp(teststr))
