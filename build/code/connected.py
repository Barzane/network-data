# -*- coding: utf-8 -*-

import numpy 

def connected(g):
    """FUNCTION	determine connectedness of (N, g) and compute its diameter
		INPUT	adjacency matrix g (output from Task 6)
		INPUT	dictionary of nodes (output from Task 5)
		DETERMINE	integer n (the dimension of g)
		SET	an n x n matrix of zeros, G1 <numpy.zeros((n, n), dtype=numpy.int)>
		SET	an n x n matrix G2 = g
		SET	diameter = infinity <diameter = float("inf")>
		SET	flag = True <Boolean flag indicating an active algorithm>
		SET	j = 1 <scalar j representing the current path length>
		WHILE	(flag is True) AND (j<=n-1) <while flag and j<=n-1>
			<n-1 is the maximum possible diameter for a connected network>
			SET	matrixsum = I + G1 + G2 <numpy.eye(n, dtype=numpy.int)>
			<I is the n x n identity matrix>
			SET	matrixsum = G1 + G2
			SET	condition = no zero elements in the upper-triangle of matrixsum (including the leading diagonal)
SET	condition = no zero elements in the upper-triangle of matrixsum (not including the leading diagonal)
			<numpy.min(matrixsum[numpy.triu_indices(n)])!=0>
<matrixsum[numpy.triu_indices(nodes)]==0).any() ==False>
<matrixsum[numpy.triu_indices(nodes,1)]==0).any() ==False>
			IF	condition is True <if condition>	THEN <(N, g) connected>
				SET	diameter = j
				SET	flag = False <terminate search>
			ELSE <update and continue search>
				SET	G1 = G1 + G2
				SET	G2 = G2 multiplied by g <G2 = G2.dot(g)>
			ENDIF
			INCREMENT	j to j+1
		ENDWHILE
		OUTPUT	diameter
	ENDFUNCTION   """
 
    n = len(g)
    G = numpy.zeros((n, n), dtype = numpy.int)
    G_plus = g 
    diameter = float("inf")
    flag = True
    j = 1
    
    while (flag) and (j <= n-1):
        
        M = G + G_plus

        if (M[numpy.triu_indices(n, 1)] == 0).any() == False:
            
            diameter = j 
            flag = False
            
        else:
            
            G = G + G_plus
            G_plus = G_plus.dot(g)
            j += 1 
                            
    return diameter
