import filedefs

def sharedmotif(file):
    seqs = filedefs.load_fastaseq_list(file)
    longestsubstrings = []
    for i, seq in enumerate(seqs):
        if i == 0:
            continue
        longestsubstrings.append(longestcommonsubstring(seq, seqs[0]))
   
    shortestsubstring = []
    shortestsubstringlen = len(max(seqs))
    for i, substringlist in enumerate(longestsubstrings):
        for substring in substringlist:
            if len(substring) < shortestsubstringlen:
                shortestsubstringlen = len(substring)
                shortestsubstring = [substring]
            elif len(substring) == shortestsubstringlen and substring not in shortestsubstring:
                shortestsubstring.append(substring)
    return shortestsubstring
            
            
def longestcommonsubstring(s, t):
    #https://en.wikipedia.org/wiki/Longest_common_substring
    m = len(s)
    n = len(t)
    z = 0
    ret = []
    longestmatrix = [[0 for k in range(n+1)] for l in range(m+1)]
    
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                if i == 1 or j == 1:                  
                    longestmatrix[i][j] = 1
                else:
                    longestmatrix[i][j] = longestmatrix[i-1][j-1]+1
                if longestmatrix[i][j] > z:
                    z = longestmatrix[i][j]
                    ret = [f'{s[i-z+1:i+1]}']
                elif longestmatrix[i][j] == z:
                    ret.append(f"{s[i-z+1:i+1]}")
            else:
                longestmatrix[i][j] = 0
    return ret
    
inputfile = "/Users/ameliadayton/Downloads/rosalind_lcsm(1).txt"
sharedmotif(inputfile)