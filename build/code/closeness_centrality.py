# -*- coding: utf-8 -*-

import numpy
from distance_matrix import distance_matrix

def closeness_centrality(g) :
    """FUNCTION	compute closeness centrality of every node in (N, g)
		INPUT	network tuple (N, g)
		SET	adjacency matrix g
DETERMINE	integer n (the dimension of g)
DETERMINE	distance matrix D (the first output from Task 15) <the elements of D are l(i,j)>
DETERMINE	array all_cc_i, all closeness centralities, as floats <float(n - 1) / numpy.sum(D, axis=1)>
SET	dictionary CC, with key = node number, value = closeness centrality <dict(zip(range(n), all_cc_i))>
		OUTPUT	CC
	ENDFUNCTION"""

    n = len(g)
    D = distance_matrix(g)[0]
    all_cc_i = float(n - 1) / numpy.sum(D, axis=1)
    CC = dict(zip(range(n), all_cc_i))
    
    return CC