def mortalfib(n, m):
    # Fn = Fn-1 + Fn-2 - Fn-(m+1)
    bunnies = [ 0 for b in range(1, m+1)] # an index for however many months
    bunnies[0], bunnies[1] = 1, 1
    
    for i in range(2, n+1):
        bunnies = [sum(bunnies[1:]),] + bunnies[:-1]
        # sum takes new number of pairs (excluding babies)
        # bunnies[:-1] takes out dead ones
    return bunnies[0]

mortalfib(91,17)
