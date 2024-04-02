def count_nt(s: str):
    nt_dict = {'A': 0, 
               'C': 0, 
               'G': 0, 
               'T': 0, 
               'U': 0}
    for nt in s:
        nt_dict[nt] += 1
    return nt_dict
        
teststr = 'GTTGAGTTCTATTGCCCGTTACGAAAACGCGCGTAAATGACGTAATCATGTGGACACACAAGCCATGCTCTCGCGACGTCGCAGGCACAGGTGTTCCTCCGCCATCTATACCCACGTCAGCGACAGTTCAATTGAACATTCCTAGACGGGGCGGTGCGATACCAGCCTAGCCGTATGTACAACTCATTAAAGTACAGGGGCGAAATAGTCAGGGACAAGCATAATCGTTTCACATCGAACGGTTACTTTCAAGAAGTACCAACCCAGGGACAATCGACCAGGTGTCCTAAAAGTAGAAACTAGGCTGAGTAGCTTATCGACTTGTAATTAAGAGTAGCCGCAAGAAGCAATTAGGCTCGCGCCCTAAGCTTTCTTTCGTGCGCTTCCTCGTACTCACGACACACCGAACTCGACAAAGAAAGCTTTTGACAACGTGAACTATGAGTCCTCGAGCAGCTGGCTTTCCCTCCTAGATCTGAGTACATGTCCTATTCGTTCTTTGTCTCCTGCAAAGTTAGCAAGGCATGTGGTAGTTATGTGCCTTCAGAGAGTCCCTCGGATATCCAAATTCTTGTCTAGTTACTACAGCTAGATAACCACGTGCAAGTGAAGTAAAGAGTGAGAAGCGGTAGCGGTCGGCTTAAAATTGATTGAAACTGGTCGGCAGAATAGGCTAACAATAGCTTAAAAACTGTTTGTCACTCAGCCTGCGCTGGCTGTTGCGAGTGGTTGTGCTTCGATACTGCCGGCAGTGCCTTATGAGGCACTTGATGATGCTTTCCGTCATGGTAACCGAGCCTACAGGCTCTCATGTCGAGACGAGGCCGGTCCGGGTGTAGTAGAGGACTCGTGTTTATATGATACAGTCTAACTCTTAATTCGCAAACATCTTGTACGCTTAAATCAACTCCGGTAGCCCCTGATAAATTACTACAGAGGCTCATTGAGACCGGCCCC'
print(count_nt(teststr))