def mendels_first(k, m, n, dominant=True):
    # P_dom = n_dominant/n_total or 1 - n_recessive/n_total
    # k = AA homozygous dominant
    # m = Aa heterozygous
    # n = aa homozygous recessive
    fullpop = k + m + n
    punnet_dom = {
            "kk": (k * (k-1)    * 1),
            "km": (k * m        * 1),
            "kn": (k * n        * 1),
            "mk": (m * k        * 1),
            "mm": (m * (m-1)    * 0.75),
            "mn": (m * n        * 0.5),
            "nk": (n * k        * 1),
            "nm": (n * m        * 0.5),
            "nn": (n * (n-1)    * 0),
              }
    if dominant is True:
        return round(sum(punnet_dom.values())/fullpop/(fullpop-1), 5)
    else:
        return round(1 - sum(punnet_dom.values())/fullpop/(fullpop-1), 5)
        
mendels_first(25, 24, 16)
