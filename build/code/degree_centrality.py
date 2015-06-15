# -*- coding: utf-8 -*-

import numpy

def degree_centrality(network) : 
    """FUNCTION	compute degree centrality of every node in (N, g)
		INPUT	network tuple (N, g)
		SET	adjacency matrix g
DETERMINE	integer n (the dimension of g)
DETERMINE	array all_dc_i, all degree centralities, as floats <numpy.sum(g, axis=1) / float(n - 1)>
SET	dictionary DC, with key = node number, value = degree centrality <dict(zip(range(n), all_dc_i))>
		OUTPUT	DC
	ENDFUNCTION"""

    g = network[1]
    n = len(g)
    all_dc_i = numpy.sum(g, axis=1) / float(n - 1)
    DC = dict(zip(range(n), all_dc_i))
    
    return DC
    