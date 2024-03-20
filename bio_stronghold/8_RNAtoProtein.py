import filedefs

def getcodon_list(s):
    if len(s) % 3 == 0:
        return [s[i:i+3] for i in range(0, len(s), 3)]
    raise ValueError("Full input length not divisible by 3")

def RNA_to_protein(s):
    proteinstring = ''
    codon_list = getcodon_list(s)
    for codon in codon_list:
        if filedefs.codon_protein_dict[codon] == 'STOP':
            return proteinstring
        proteinstring += filedefs.codon_protein_dict[codon]
    return proteinstring

teststr = "AUGGACACGGCAUUAAUGAAUACAUCAGGCCAAGAGACCAUGACAGGUAUCUGUCGAAGAAAUUUCGGAAAGAUGGGGUGGAACUCCUGCUCCUUACAAGGUCAGAUCCUCACUAGCAACAUGGGUGGACGACUCGACGAACCUUUACGAGCCGUUCCAAGGAGUUAUUCGAUCCAGAAGGCUGGCACAAUGGCCUUAGGCAGGAGAUGCGCGAGACCUCUUAUCCCCACGCGAAUAUACAAUUCAUCUGGACAUACAAUUAUCUAUAAGAGUGAUCGACGGACCACGUCAUCUGCACCGUCCGCGAGUACCCAAACGCGUCAACCAGAGAGCACGAUUCUUAAAGCCCAGCAAUGCGUGCUCGGGCACGGAAACCGCUCCACGACGGUAUCGACCGUUGAAGUGAUUUGUUGGGUUCAACCGACAGUCACAUUCCAACAGCAGUGCCCGCAAAACCUGUUUAGCCUGCUGGUAUUUUUUGACUGUAUGGUCCUUGAAGCCGUUCUAUUAUACGUCAUAUUGCUCGAGUUGGCCCGUUCUGUAAGUCUCUUGAGGCUGUGCGAUGAUUUUACAGUUGAGUCGUGUGCUAGAGUAGCCCCGGGCUGCACAUUCCUAGACGCUUCAGUACCUCAUCGGGCCGAAGCGGAGAUCUGUGAUGGCCUCUUAUCCUCGGGUGUCAUUCGGCAUGCUCUGAGGCUUUUUUCUUCGUGCCGAACCCCAACGUCGGCUAGACCCGCACUACUACGUUUCCUCGAAUCCUGGUAUCGCGUCGCUGUGCGCAAUCCGCCCAGCCAGCCCUUGCUAAAGCGUCAUCUCCACGUAGGCCCCACCGGGACGAGUCGGUGGGUAGAAGCGGCACGGCUCGUCGAGCGCUCGCUGGGGCACGGCUGUUGUCCAGCACUACAAACUUGGGGUGUCUUAAUGCCGGGAGUCUCCAAUCAGCCGGCGCUUGAUCCUAGUCGCCCGUGUCGCGGAGUCGUGUUACAGCAGGGUCUUUCUGGUCAAUGCCUUGAGCAUCCACGCACAAUUGAUGCGUUCACGAACAUCGAAGUCUCCCAGGACAGUGCACACCCCCGGGCUCUGAAGUGGGCGUAUUUGAAAUUCAUGUCAGCGGAGGUGACACAGCCUCUACGGGCCGCCUAUUUUGGACUGGUAGUGGUUGCUAAAUCCGGAACGGCAUUCGGAUACUUCCCCAUAUAUCUCCAUUUCUCCUGGUCGCAUCAGACAUUGAUUUCCAGACGAGAAAUGUGUUCGUUUCAAUCUCAAGUUGCCGACCACCUGAUAGUGUGGUCGUACGCUCCUAUCCGUGGCGCAGAAGAGAUUACAAGGUCCCCGGAUUUAUUGACGUUGGGGAUGUUAUGCAGAAAAAUCCUCCUGGCAAAGCGUUUUUUCUUCCAGGUCCGUGCGGGGAGACGCUCCGUGCUACGGCAUGGCUCUUUGAGGGGAAGGUCUAUUCAGGAACGGGUGCUCAUUUGCGGCCGGAUGCGACAUGCGGUACGGUCCGGACAGCCCGGUUGCAUCUUACGAUCAGAUUACACUUGUGCGCAAGGGGAGCGUAGUUCAUCCGGCGCUAAAUUGCGCUCAUUCUCGAAUGUAUGGAUUUGUAGGAAUGACACCGGGAUUAGGCCAACACAGUCGUACAUUUUAUCGAACUUGAUGCGAUGUGCUACAGACUCCAAAUGUGAAUAUGCGACGAUGCUCACGUACCCCCUGCGUAUUCUCUUUGAUCCGAAUCCCGGACGAGGGUGGUCUAAACACUGUGGUCGGCGUAAGAUCGCGUCUGCAAUCGCGUGUAUACGAAGUUCCUCUAACCGUAGCCGUUUGACUCAAGACUUGCUGACACCAGUCACUAUGACGUGCUACGAAUUAAAGUCUGAUAGUAUGCAAGCGGCGGUAGUAACGGCUGGACCGGAAUUGGGAAUAGUUCAUCCGCAACCGGGAGCUUGUACAUGCACGCCUCUAGACGAGGUGCAUGCCAUUGGUCCCCGACUGAUGGAGGAGCUCGGCUCCAAAGGGUCCUCGUGGAAUAGCGCGCCCUACAUAUCUCGGAUUGCCAUUCGCGUGACCUAUGGCUCCACCAAGCCGGUAACCGGGCAACCAUUAACGUGUCCGUCUUACACUCGUCGCCAUGCAAUCCUCCGCAUCACUCUGAACUGGCUCCUUAUAAAACUACUGUAUCACCAUCAUGGCGCGGCGAUUCGAAUACCGUCAAUUAUAUUCGAAACAACCGCGAUUUCACGUUAUCCUUGCCUAAAUUCCUUAAACUAUCUACCCCACCUGCGUUCCACUGCCUCUGAGCGAUGGACUGUUUCUUCUACACCUCCACCUCCUGAUAAAUGUGACAUCGGAACAGGGCAUGGCACUUUGUCUCGGGGCGGGCAGCUUGCUGGACUCACCACUGAGUACAGAGGGCUAUUUCAGGCGAGCCCCCGAGUUCGACGUUCACGCUGUGAAGCAGUCAGUCGGCUCUGGGUUUUUAACUCAGGCCGGCGCGAUCAGCGGCCUGUAAGUGUUAAGUCAAGUAGAAGGGGCUUACGGGCAGUGGCGAAAGAUUCGGCUAGGACCAAAAUUCCCCGGGAAUUUAAGGUUGCCCUUUACGGCGUUCUGAAUGUUGUCCGUCCAAAAGGAUAUACUUCUACGGGAAAGACGGUAUUAGUACGGGCGGCUAGGAUGAUAGGGUAUGUAACAAUGAUUCCAACAGCGCGAAAACCAAGCCUCGGUACUUACUUGGCUGCGUGUCGUCUCUGUGAGGUAACCAACUAUAGCUAUAUUAAUGAACUGACGCGUUUCUGUACAAAAGGGAGCGUGCUAGAAAAUCCUCUUCGCCUAGUAAAGUCUCGGCAUAAGUGCCUUCGUAUUACUUUACAAGUCCAGACUAGGCACCUGAGUAAAAGGCCCACACGUACCCGACCCUGGAUAAGCCCAAGCGACGAAGGCAUGCGAGCGCUAGUAGGCGAUUGCGUCUUGCAUCAAACCUGCGCAGUUGAAGACUUUGGGUUAACAGUGUCCAUGUCGGUCUGGCAGGGGGAACUAAACCUAAGGCUAGGAGUGUGGCGGGUUGCUCAGAGUGCUAGCGGGGUCCGGGUCCUAGGUACGGGCCAUUGUACAGACGGGACUGCCUGGCAACAGUACUUGAGGGCACUCUUUAUCCAUCUUCAGGUAAAAUCAUUAGUGGAUUCGACUCAAGACGCGGACGCGAUGGUUCUAGUCCAGGGUGCAUCUGGGCGAGGUUACGCUGUGCAUAACUUUAGAGGCUGUGCCCGUACGUCGCCACGAACGCUCUUCGUGAGCCUGUACGAUGCGUUUUCACGUCCCUUACAGCGAGACGACGUCCGUAUUAGGCUCCGAGCCUCACCUGUGACCUCUAGUCGUUCAGGUACGAAGACAGGCAUACGGCACCGGCGUCUACGAACGAGAAUGCAUAAAUUGUCUGAGAACUACCCCUUUCGCGGAGGUCGUCUUGAAGAACCCCGGGCUGCUCCCGACUAUUUAGCGAGUUCGUCCAGCAAAUCCAUAGGCCUUUUUAACAGACAAAGUGAGCCACGUUAUUUCGCCUUGCCCUUGGGUCGCAGGGCCAAAUCAACGGGGCCGUCAAAGGCUAAGCAGGUUACUGAAGCACCUCUGCAAUGGCACAAUUCACGGCUCACUAGCCGGUAUGAAGAGAGCAAGGGAUGUGUCAGAUCACCGGAAGCAGCAACGGAGGAUCACCCUAAGUACCCUAUCCUUGAGAGCGAUACGUCGAUAAUUCCGAGGCCGCUUUUAUGGAUCUCGGCCCUGGAGCGGCUCCCCAUAGGUAAACGUGUUGUGUGGCUCUUGGCUUGGAGCAUACAAAAAGCGCCGCCUUUACGAUGUCUUUACGCUCUCCGUAGCGAGAGGGUCCAUGCCCGGUUGAUGGCCAACUGUAUUCUUAACGAAAUCGGCAAGGGGUGUGCGCAUGUUAGCGUAUACCACUUUAGCACACGACGGGCACUUAACCGCGUAUACAGCGAACAUCAAACUAUCGCCCCCCAAAACGAAUGGACUUCCUAUGAUAACCGAACUAGGGGCCCCUCACGGUAUCCUUGGAGGUUUGGGUCGUCGGGGUUGAGUGAUCUUUCGGGCCCGCGACGUAGAGCAUUCCCUAGACUCGGCUACGGUUGCUCGCAAUCUUGUAUACUCCGACUUCCCCGCCUACCUCGUACAAUCUACCUUGCCCAUAUGUUUGCAACCCACCCAUCAAUGCUGUUUACAACCUUCAUGGUACUAGUCACCACCGAAGGCAGUCGAUGCCGCGCCAUGAGCCACUCAGCAAGGGUGCUAGUCUGGCCCCAAGACACUGAAACAUUAAGCGGCCAAAACUUACUUUCGCGACUAUCUAUUCUAAAACAUCAGGUGACUCUAGCAGCUCUAAUAAGGGCACCAGCAGGUUGCGAGCGGUCCAACGCCCCGUUUAAGUCGGAAACCGUGCCAAAUCGUGUACAGCUCCAUGGCGUAUUUAUUGACGCUAGCCUUAAUACUCGCAAUCACUCGAGACAAGGUAAGAUAUGUACGGAGGGUAGGGGACAAAGAACUCCCACUACGCCGUAUAUUCCGAGAUCUGCGCCCGACCUUGCGUCCAUCAACAUUACCGCAACGGAUUGCUCCGCCCGUGUGUGCCUUGUUGACUCAAGCUUCCCACUAUGGGAACGGCUGGCCCAGACUCCUCGAACUGCCGGUGACUUUCGCAUUCGGGCUAUACGUGAGGACGUAAGUACUCUUUCCAUCAUAUCACUGAACGUUCAGGUCGUUCUCUACACCGCGUCUACGACUGUACUCGCAUAUCCAGUUCCGGUCCUUAUUUAUCUCAGAUGUCCUGGUUGCCGAUUUAUACGGACGGGAAGCUCACUGAUUGGUUCGUCCUGCCUGUCAAUGAGCAGACUACUGGUACAUUUAAUGCGCGGACAUACCGAGCGGACCACUAUUACAUUUGAAUUAAACGUGAUUGACAGGUUCCUGGAGCGGCCGCAUUCGGGUUAUGUUGCUGUAGCUAUGAGAUUUAGUGGGCCACAGAAGCGGAGUAGGAGCCUUGUAAGCUACCGGUUAAUAUGGACCGUUAGGCUUCCUUUGUUCAGUAUGGGUUCUACGCUGGUAGAGUAUCUCGGGCCGAAUCUGGUUCACCGCCCCCGUCGUUAUUACAAUGGGCUAGGAUGUCAUUUAACGGCCAGCGACCAUUUGGAAGUAACCACUAUUCACGAAGAUUAUGGAUCCCUUCCUAUUGAGAAGUAUCAGGUUGUGAUUCAUGCGGACUUUAUAUGCUUUCGUCUAGGGUCGAGCAACGCAAGCAAUAGAGCGGGUAGCGUGGCCGCGGUCCAGGCUUCUUGCGCACCUUCCACAUCGAGCCUCCUUGCUCUGAAAGCACACAUUCAUAAUCUAACCAAUCAUAGCGGACGCGCAGUGUAUGCUCUGUUACAACAACUAGAACUCUUAUUCCGGGCAAGUAGACUAUGCUCAUUUCCCCACAGGGAGCCAAAACCUUUUUCCCCGCUAGUCGAGCAAUUCCAGUCCUUUAACGGCGUGCCCCAGCUGCGUGAGUGUGUGCUCGCCUUCACGACCGUAUUUUCGUACAUUCUGUUGGUCGGCCAAUCUCCCACGAAUGCUGUAUUCAUAUUAACCAGUACUCACCAGCGCGGUCUCGCCAGUUCUACAGGAAAUUUGCCACCUCUAAAACGCGGUAUGACCACGAAAAUAGUGAGUUCGUGCAACCGUCACUUUGGCUUGGCCCCCGUACGUUACUUCGACUAUGCGGGCGCGUCGGUCAGUAGUGACAAAAAAUUAGCUCCGUCUACUUGCAGGCUAUGCGCUGGGUCUGUCUUUACACUCUUAUUCGGUGCUCAUACAACAGCUGACCUUGUGGUACCUCGUGCAAUAAAUAUUAGCAAGCACUUACUCUUGAUGCGUAGUUUCUCCCGCCGACGCUCAUGCCGGGAGAUAAACCGUACGUUACAAUACCAUCCGACACAGAUGAAUCACUUCUCCUUCGAUUCCCCGAGAAUCUUUGCGGAACGUUGGCUGCUUUCACGUGGCACGGCUAUAGUCUAUAUCCCAGGUUGCUUAUGGAUCCCAGCGAUCCUUCUUCUGGAGCCCACAGCACACCAAUACCCUAUACCCGGUGCUCAAGCCCCAAUAGGAAAGACGUAUCCCGUUACGUUUACGACAUGGUGCAUUAAACUGGCUGCAUUGCAGUUCGAAAUUAGGGGUCUCCCUCGAAGGCCUAAUCGCAAAUAUGUUGCGCCAGGCAAAACUGAAGGACGUAGCGUGUACCCGUGGCUGCAGCCCCCAGACGCCACCCCCCAGGAUUACGAUGCGAAAACACGGGCCCACUUCACUACGGUGCCUACUGAAAAGUGGCGGUGGCUUAGGGCUUCAAACACUGCUCGAGUGGCUAGAGCCAGCGGGCCGGACGGACGUGACAGGUACUCACCAUGCAACGGACAGAGGAGAGAUUGGCUGGGCGGUGGACCUCAGCACGCGGAAAUUAAUCACAUUCUAUCUUAUGCCACUUGUAUACCAGGGCUAUCCAAAACCACUCCCACAAGAGUCGGACAUGUACGGCGGUUGACAACUACGGGCCGAGUUAUUUGUAUAAACGGAGGAGGGCGGUCAUUAUUAGAGUCAAAUGACGUGACGAUGCUCUAUCCACGAGUAACCGGACCAGGGCAGUUCAGAGAAACAAGCCGUAAGGUGGUCAAGUUCGAACUCAAUCCCUUAGAUGCCAGCUCGGGGAAUCUUUGCCAGAAGCGGUCUGCGUCGUCUAUCCUAUGGCCCUCAUUGGGGUGGCAGUCGGGGAAGAGGCUAAAUACCAUCCCCAGAUGGGUCUUAUCCAGUCUCGCCCCUGUAAGGAUCCUCGGAGGGUUCAACAUUACCCUUUUGUCAGCUAGGGAUGUUGUCUACUUAGUGUCUCUACCUCAUUUCAUAUCCGCCGUGCCGCCCCCGAGGUACCUCUAUACUAGGGCCCACUCAAAUAUGUACCCCAAAAGCAGAACCGAGAAAGCGCGUGGGGUUACCGAGGAACCACUUUUCCCAAUUCGAUGGAGUGAUCCGGCGACGAAGCCUUGGAGUCGGAAAUCAGGUCACGAGUGUGGUCCCUCCCAGGCCACGGAUCCAUCGCGUGUCGUUUGUAGGUCAUAUUUGAUACCCAUUAAACAGCACUACAGAGACGUCAACGUGCACCUGCAUGAAUCACAGGAAUCCACAAACUGUUUUGGGAGUCCUUUUACAGCCAGUAGACCUGGAGCGAAACCGCUAUGCCAUCCCUACAGGGCCUAUUCACACACCUCACGACCUGCUGAGUCUCAAGGUGAUCAUCUCAACAGUCUAAAUGACUCUGGGAUUGACUGCCCGAUAGUGCUGGCAUUGUCCUUAGGGCUGCUUUCCGGCGAAAUUGUCGAAUACCACUCCGCGACGCCUUCUCAAAAUCUCGUGAGCGACCUUGCUAUUGUUUGGACGCUCGGCCGCCAGCGAGGGGCUACCUAUUCUGAGACCUCCGCCUUGGAACUCAAGUUUGGAUCAUCAGUUCCUCGACAACGUUCGUCGAGGUGCGUGCUGCCCAGUCACACUUGGCCGGCCCAUUCGAAUUCUCUCGCACCCAUGUCAACCACACAACAUACUUCGUCGCAUAGCGUAACAACGAGGGGACAGCUGUACGCUAACAUAAAUCCGAAUGGGAACAUCGGUCCGGUAAAAAAGGCCUUUAAGGACGCACGUCGUAGAAACCACGAUAUUACAUCGUGGAUGACUUAUUACGCAUGGGCGUACAAAGCACCGGUGAGAUGCAACACCAGCUGGUUUCGCAUCGGGAUAUCACAGCGCAGGCGCGCCGCGUUGGCGUCGUCCGACAGCACGGAACCAACUCCCUGUAUCGGUGUUAGGCCGAACCUCCAAUUUCCGAACCCCCUAAUAAUCACAUAUACACUGUCUUCUGUUCCAUCGACAAUGGGAUUUAAAGCGCACACCAUGGGGCCUGGGUCUUGGUUAGUUAUCGGACCGACCCCCGAUUCCAUCUUUCUAGCCGUAAAACCGAGCCUUAGCAUAAGACAGAUCAAUGUCCACUCGCGGCGCGACAAUAGCAGGUGGAGCGAAGAGGCCUUACACAUCGGGGUCCCUAUUGCAACCUUUGCACAAGGACACGUCUCAGAGCAGUAUAUAUUGAUACCGGACUUCGCUGUAGCCCAUGCGCGUACGCACGAUGCUGUGUUCCUCUUCUUAAAUCGUCCGAAGCCUUUUGAGUCCUUAAACACAAACCCGCCACCCCCUCGCUCAGACUCAACUCUCGACAUCUUGCCCGCUCCCAAAACUCAUGGUACCCGGGUGAUUUGUUGUGCCACGGUAAGCCGGUUUAGACUUUGCCAAAGCAGGGGUUGUAAGUGUUCAAGUCCGCCGAUACCGCGUCGCUAUGAUUCGGACAAACGUUUUUUUACGUUACCGCACUCAAAGGCCAUACUUGGAGCAAAUUACCCACGGGAUUUUCGGCUUAGUCUGAUAGAUCUCGACAGACUGCGGUCAGUUUCAUGUCCCCUAUCAUCUAUCCGCAUCGAGGAUAAACUACCGAUUCGUCACUUCGUAUUGCUUGUUAACUGCCUGUGCAUGCGUCCAUUGGGGCCCAGAGGUGACGAACUGCUAGUGCAGAGUUCGUCGACUUGCUUGAGUCACCUAAUUCCCCGUCAGGGAUACCUGAUCGAGAGGCCCUCCUCCUCAAGCACCUGUGGGUGCUUUCGGCUUGACUCAUAUAUAGGGCGCGUCAAAAAGUUGCAGCAAGGGCAGUGUCCGGAUCUUUGCCGCUCUCGUUAUGCAGCGGCUCUUUUGUCCAUAUUAGCUUCUGCUUUGAAUCGUUCGCUCCUGCAAGGAGAGAGUGUUAGUGAGACGGCUGACAUGGAGGCUACUUCAACCUUAGAAGGCGAUCCUCCCGCGCUAUCAUACAGUAUUUUGCGUCUAUUGAAACCCGACCGAUUGUAUCUAUACUUUGCUCGGAAUGCACGGGCACCACGCGGGGGCCAGAGUCUCUAUAAUCCCGACCGGCCACACCACUCGGCCCGGUGUUCGCUGAAGCUCCACCGAAAGAAAACCUAUAGAAGCGGCCUCUGGCCCAGCGUGAUCAUUACUCUCGCCUGCAUUGUGGCUGCUAAUUGGUUCAACUUCAGACCCUCUAUCAGCUUGUAUAAAAUGCAAUCACGUAAUCCCGUGCAUACUUCACGAGAUUCCGCACCCUUGCGAGGGGCUUGUAGCUCUACUACAUUUGCGAUGACAAUGUCUCAUGUCGCGUUUCCGGCCGUUAUAGCAUCCGGCUCUUUGAGUUUUUUCGGUGACAGUCGUGAACCGGAUAGAGGCCUAUUGUAUGAUGGGCAACCAUAUAGGGCAUCCGCGCGCAUAGCGCCGCUCGUGCCUAGCACGGACCCGAGCGGCUAG"

RNA_to_protein(teststr)