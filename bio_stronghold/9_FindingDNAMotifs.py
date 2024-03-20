def findDNAmotif(s, t):
    # needs 1 based numbering so returns location + 1
    motif_locations = []
    motif_len = len(t)
    for i, nt in enumerate(s):
        if nt == t[0]:
            if s[i:i+motif_len] == t:
                motif_locations.append(i+1)
    return motif_locations
        
teststr = 'CTCGCCAACAATCGCCAAGTGTCGCCAAGTTCATATCGCCAATCGCCAACTCGCCAAGCTTTCGCCAAAACAAAGTCGCCAAGGTCGCCAATTCGCCAATCGCCAAATCGCCAACGGAGCTCGCCAACCTCGCCAACCTGGTTTCGCCAATCGCCAATCGCCAATCGCCAATGTCGCCAATCGCCAATCGCCAAGATGTCGCCAATTAGACCGTCTACCCGGTTCGCCAATCGCCAAATGTGCAAAGTCGCCAAAATCGCCAAACGTCATCGCCAATCGCCAATCGCCAATCGCCAACTTCTCGCCAAACGCATTCGCCAATACAATCCTCGCCAATCGCCAATCTCGCCAACCTCGCCAAAGTCGCCAAACACATCGCCAATTCGCCAAACGTCGCCAAGTCGCCAATGAAATCGCCAAACTCGCCAATCGCCAAACACTGATCTCGCCAATCGCCAAATTTTGTCGCCAAGTATATCGCCAATAACTCGCCAATCGCCAAGTCGCCAATCGCCAATGTCGCCAAGGGTTTCGCCAATCGCCAAATCGCCAATCGCCAATCGCCAAAGGATCGCCAAATCGCCAAGTCGCCAATCGCCAATCGCCAACCTTCTCTTCGCCAAACTCGCCAACTATCTCGCCAATCGCCAAGAGTCGCCAAACGGCAATCGCCAATTCGCCAATCGCCAATCGCCAACCCCCGGCTCGCCAACTCGCCAAGTGTCGCCAAATCGCCAATTAATCGCCAATCGCCAAAGCTCGCCAAGGTTCCATTAACTCGCCAAAAGGTCGCCAATAGTTCGCCAATTCGCCAAACTACGCTCGCCAATTTCGCCAATTCGCCAACCTCGCCAACAATTCGCCAAAT'
testmotif = 'TCGCCAATC'

DNAmotiflocations = findDNAmotif(teststr, testmotif)
for motif in DNAmotiflocations:
    print(motif)