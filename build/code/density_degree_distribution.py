# -*- coding: utf-8 -*-

import numpy

def density_degree_distribution(network):
    
    """FUNCTION	compute the density and the degree distribution of (N, g)
		INPUT	network tuple = (N, g), where N is a dictionary of nodes (output from Task 5) and g is the corresponding adjacency matrix (output from Task 6) <I think that it will be convenient to define networks as (N, g), especially when we will have multiple quarters and N or Nbar(s); a network can be defined as network = (N, g), outside of the function>
		<def some_function(network)>
		SET	dictionary of nodes N <N = network[0]> <not used in this function>
		SET	n x n adjacency matrix g <g = network[1]>
            DETERMINE	integer n <dimension of g>
		IF	n = 1	THEN <for n = 1, the density will not be defined, so stop>
			STOP	<raise Exception('n>1 required')>
		ENDIF
		DETERMINE	array all_degrees, containing sum of each row of g
    <numpy.sum(g ,axis=1)>
    DETERMINE	float density = sum of all elements in g, divided by n x (n-1)
    <in some Python implementations, e.g., ⅔ will give 0, so we force a float>
    <float(numpy.sum(g)) / (n * (n-1))>
    <minimum degree = 0, for a network of isolated nodes>
    <maximum degree = 1, for a completely connected network>
    DETERMINE	a dictionary Pd, keys = degree, values = degree density P(d)
    <y = numpy.bincount(all_degrees)>
    <ii = numpy.nonzero(y)[0]>
    <Pd = dict(zip(ii, y[ii] / float(n)))>
    <Pd = dict(zip(range(len(y)), y / float(n)))>
    IF	sum of values in Pd not = 1	THEN <error> <int(sum(Pd.values()))!=1>
    <can this error trap run into rounding errors? e.g., int(0.9999999999) gives 0>
    STOP <raise Exception('frequencies P(d) do not sum to 1')>
    ENDIF
    OUTPUT	density
    OUTPUT	Pd
    ENDFUNCTION"""
    
    g = network[1]
    n = len(g)
    
    if n == 1:
        raise ZeroDivisionError('n > 1 required')
        
    all_degrees = numpy.sum(g ,axis=1)
    density = float(numpy.sum(g)) / (n * (n-1))
    y = numpy.bincount(all_degrees)
    ii = numpy.nonzero(y)[0]
    Pd = dict(zip(ii, y[ii] / float(n)))
    
#    if int(sum(Pd.values()) != 1) :
#        raise Exception('frequencies P(d) do not sum to 1')        
#    Pd = dict(zip(range(len(y)), y / float(n)))
       
    return density, Pd
    
        
    
    
    
    
   
    
    

