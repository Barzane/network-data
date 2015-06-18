# -*- coding: utf-8 -*-

import numpy

def distance_matrix(g) :
    """FUNCTION	determine connectedness of (N, g) and compute its diameter
INPUT	network tuple (N, g)
		SET	n x n adjacency matrix g <g = network[1]>
		DETERMINE	integer n (the dimension of g)
SET	an n x n matrix of zeros, G1 <numpy.zeros((n, n), dtype=numpy.int)>
<the matrix G1 will track which elements of D have been updated>
		SET	an n x n matrix G2 = g
		SET	n x n distance matrix D, initialized to 0s <D = numpy.zeros((n, n))>
		SET	flag = True <Boolean flag indicating an active algorithm>
		SET	j = 1 <scalar j representing the current path length>
		SET	n x n matrix of ones, J <J = numpy.ones((n, n))>
		<if n = 1 (trivial), then the function will not enter the WHILE loop, and the function will output D = 0 (scalar), as required>
		WHILE	(flag is True) AND (j<=n-1) <while flag and j<=n-1>
			DETERMINE n x n matrix of Booleans B, True if element of G2 is nonzero and corresponding element of G1 is zero (length of geodesic not yet found)
<B = (G2 != 0) * (G1 == 0)>
INCREMENT	D to D + B multiplied element-wise by (j multiplied by J)
<D += B * (j * J)> <update (with the current path length j) the elements of D that have corresponding nonzero elements in G, and that have not previously been updated>
			SET	matrixsum = G1 + G2
SET	condition = no zero elements in the upper-triangle of matrixsum (not including the leading diagonal)
<(matrixsum[numpy.triu_indices(n,1)]==0).any() ==False>
			IF	condition is True <if condition>	THEN <(N, g) connected>
				SET	flag = False <terminate search>
			ELSE <update and continue search>
				INCREMENT	G1 to G1 + D <G1 += D>
				SET	G1 = G1 + G2 <actually, this is INCREMENT>
				SET	G2 = G2 multiplied by g <G2 = G2.dot(g)>
			ENDIF
			INCREMENT	j to j+1
		ENDWHILE
		SET	D to float-type, in case it is an integer-type <D = D.astype(float)>
		<this is because the following addition of infinity will only work if applied to a matrix of floats; if applied to a matrix of integers, then it will give unexpected results in the place of infinity; also, it may be safer for subsequent (out of function) computations if the elements of D are guaranteed to be floats>
		IF	zeros still remain in the upper-triangle of the distance matrix D	THEN	replace these by infinity <the diagonal may still have zeros, if the network is complete and the routine ends at j = 1; these diagonal elements will be set to infinity, and then set back to zero; we particularly need to replace any off-diagonal elements of D that are zero at the end of the search (corresponding to nodes that are not linked by any path) with infinity>
		<if (D[numpy.triu_indices(n,1)]==0).any()>
			SET	matrix C, with infinity in place of 0 in D, and nan otherwise
			<C = (D == 0) * float("inf")> <C will contain nan and / or inf>
			SET	nan elements in C to zero, and inf elements in C to a very large number <otherwise, adding a nan element to an integer in D will give a nan, when we want no change to take place> <C = numpy.nan_to_num(C)>
			INCREMENT	D to D + C <this replaces all of the zero elements in D with a very large number, representing infinity>
			SET	all diagonal elements of D to 0 <we set the shortest path from a node to itself to be 0; we could also imagine it being 2 or infinity, but we will use 0>
			<numpy.fill_diagonal(D, 0)>
		ENDIF
		DETERMINE	average_path_length <numpy.sum(D) / (n * (n-1))>
		OUTPUT	D
		OUTPUT	average_path_length
	ENDFUNCTION"""
 
    n = len(g) 
    G1 = numpy.zeros((n, n), dtype=numpy.int)
    G2 = g
    D = numpy.zeros((n, n))
    flag = True 
    j = 1 
    J = numpy.ones((n, n))
    
    if n == 1:
        
        D = 0
        
        return D
    
    while flag and j <= (n-1):
        
        B = (G2 != 0) * (G1 == 0)
        D += B * (j * J)
        matrixsum = G1 + G2
        
        if (matrixsum[numpy.triu_indices(n,1)]==0).any()==False:
            flag = False
        else : 
            G1 += D
            G1 = G1 + G2 
            G2 = G2.dot(g)
            
        j += 1 
    
    D = D.astype(float)
    
    if (D[numpy.triu_indices(n,1)]==0).any():
        
        C = (D == 0)*float("inf")
        C = numpy.nan_to_num(C)
        D += C
        
    numpy.fill_diagonal(D, 0)
    
    average_path_length = numpy.sum(D) / (n * (n-1))
    
    return D, average_path_length
    