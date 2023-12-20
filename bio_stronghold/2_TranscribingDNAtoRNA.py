def DNAtoRNA(s):
    ret_s = ''
    for nt in s:
        if nt == 'T':
            ret_s += 'U'
        else:
            ret_s += nt
    return ret_s

teststr = 'GATGGAACTTGACTACGTAAATT'

test = DNAtoRNA(teststr)
if test == 'GAUGGAACUUGACUACGUAAAUU':
    print('yes')