# -*- coding: utf-8 -*-

def cl_avg(g):
    
    n = len(g)
    
    sum_of_Cl_i = 0
    
    def FN_A(i):
        
        numerator = 0
        denominator = 0
        
        for j in range(n):
            
            if g[i][j] != 0:
                
                for k in range(n):
                    
                    if i != j and i != k and j != k:
                        
                        numerator += g[i][j] * g[i][k] * g[j][k]
                        denominator += g[i][j] * g[i][k]

        if denominator == 0:
            
            Cl_i = 0

        else:
            
            Cl_i = float(numerator) / (denominator)
            
        return Cl_i 
        
    for i in range(n):
        
        sum_of_Cl_i += FN_A(i)

    Cl_Avg = sum_of_Cl_i / n

    return Cl_Avg
    