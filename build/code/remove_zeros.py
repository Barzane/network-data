# -*- coding: utf-8 -*-

import numpy
from map_airports_code import map_airports_code

def remove_zeros(Nodes_dict,g) :
    """FUNCTION	remove zero rows and columns from adjacency matrix g
        <(N,g) to (Nbar,gbar)>
		INPUT	adjacency matrix g
		INPUT	dictionary of nodes (output from Task 5)
		DETERMINE	integer n (the dimension of g)
		SET	an empty list of unused airports <unused = []>
		SET	airport_list equal to keys of nodes dictionary
		SORT	airport_list alphabetically
		SET	new_airport_list equal to an empty list
		FOR	row number i in 0,1,...,n-1 <range(n)>
			IF	row g[i] only contains zeros
			<numpy.array_equal(g[i], numpy.zeros(n))>
			THEN
				APPEND	row number i to unused list
			ELSE <the two IF / ELSE alternatives are exclusive>
				APPEND	airport_list[i] to new_airport_list
			ENDIF
		ENDFOR
		IF	unused list not empty
		THEN
			DELETE	all zero rows from g
					<g = numpy.delete(g, tuple(unused), axis=0)>
			DELETE	all zero columns from g
					<g = numpy.delete(g, tuple(unused), axis=1)>
		ENDIF
		COMPUTE	dictionary that maps airport codes in new_airport_list to numbers
				<call Task 5 function with new_airport_list, output newnodes>
		RETURN	g <this has been modified to gbar>
		RETURN	newnodes dictionary
	ENDFUNCTION"""
 
    n = len(Nodes_dict)
    airports_list = []
    unused_airports = []
    new_airports_list=[]
    
    for keys in Nodes_dict.keys(): 
        airports_list.append(keys)

    airports_list.sort()

    for i in range(n):
        
        if numpy.array_equal(g[i], numpy.zeros(n)):
            unused_airports.append(i)
        else:
            new_airports_list.append(airports_list[i])
    
    if unused_airports != []:
        gbar = numpy.delete(g, tuple(unused_airports), axis=0)
        gbar = numpy.delete(gbar, tuple(unused_airports), axis=1)
    
    Nbar = map_airports_code(new_airports_list)
    
    return Nbar,gbar
    