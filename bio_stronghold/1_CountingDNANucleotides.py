def count_nt(s: str, DNA=True):
    if DNA is True:
        nt_count = {'A': s.count('A'), 
                    'C': s.count['C'], 
                    'G': s.count['G'], 
                    'T': s.count['T']}
    else:
        nt_count = {'A': s.count('A'), 
                    'C': s.count['C'], 
                    'G': s.count['G'], 
                    'T': s.count['T']}
    return nt_count['A'], nt_count['C'], nt_count['G'], nt_count['T']

teststr = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

print(count_nt(teststr))