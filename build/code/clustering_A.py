# -*- coding: utf-8 -*-

def cl(g) :

    n = len(g)

    numerator = 0
    denominator = 0
    
    for i in range(n):
        
        for j in range(n):
            
            if g[i][j]!=0:
                
                for k in range(n):
                    
                    if i!=j and i!=k and j!=k:
                        
                        numerator += g[i][j] * g[i][k] * g[j][k]
                        denominator += g[i][j] * g[i][k]
                        
    if denominator == 0:
#        raise Exception('no connected triples in network')
        return float('nan')
        
    overall_clustering = float(numerator) / float(denominator)
    
    return overall_clustering
