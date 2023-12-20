import filedefs

def GCcontent(s):
    cg = s.count('C') + s.count('G')
    return round((cg/len(s))*100, 6)

path = "/Users/ameliadayton/Downloads/rosalind_gc(1).txt"
fastadict = filedefs.load_fasta_dict(path)

gc_cont = {}
for key, value in fastadict.items():
    gc_cont[key] = GCcontent(value)

max_key = max(gc_cont, key=gc_cont.get)

print(str(max_key[1:]), gc_cont[max_key])

