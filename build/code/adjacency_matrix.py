# -*- coding: utf-8 -*-

import numpy

def adjacency_matrix(data,Nodes_dict,carrier):
    """FUNCTION	create an adjacency matrix for nodes in N
		INPUT	data dictionary data_2013_4.bin
		INPUT	dictionary of nodes (output from Task 5)
		INPUT	a 2 letter string, carrier, corresponding to a specific airline
		SET	integer n equal to length of nodes <use len(nodes)>
		SET	n x n matrix g with all elements equal to integer zero <use						numpy.zeros((n, n), dtype = numpy.int)>
		SET	flag = False <flag indicates that no links have been added to g>
FOR	each item in the list of data_2013_4.bin keys
			SPLIT	item into a list of strings
			DETERMINE	origin (first element of split list)
			DETERMINE	destination (second element of split list)
			DETERMINE	airline (third element of split list)
			IF	airline is equal to carrier <use airline == carrier condition>
			THEN
				DETERMINE	row = origin node <nodes[origin]>
				DETERMINE	column = destination node <nodes[destination]>
				SET	element (row, column) of g = 1 <g[row][column] = 1>
				SET	element (column, row) or g = 1 <g[column][row] = 1>
				<There is no need for an error trap here, since the dictionary of					 nodes is exhaustive, and is generated from data_2013_4.bin, i.e.,					 nodes[origin] and nodes[destination] will always be found>
				SET	flag = True <flag indicates that a link has been added to g>
			ENDIF
		ENDFOR
		IF	flag is False <no links have been added to g>
		THEN
			PRINT	“Warning: adjacency matrix is empty”
			WAIT	<use raw_input() to pause the code until a key is pressed; is this a 				critical problem that requires the code to be terminated? if it is, we				 	could use import sys and sys.exit(0) to kill the code>
		ENDIF
		OUTPUT	adjacency matrix g
	ENDFUNCTION"""

    n = len(Nodes_dict) 
    g = numpy.zeros((n, n), dtype = numpy.int)
    flag = False
    row = int 
    column = int 

    for keys in data.keys():
        
        keys_list = keys.split("_")
        origin = keys_list[0]
        destination = keys_list[1]
        airline = keys_list[2]
        
        if airline == carrier:
            
            row = Nodes_dict[origin]
            column = Nodes_dict[destination]
            g[row][column] = 1
            g[column][row] = 1
            flag = True
        
    if flag == False :
        print("Warning: adjacency matrix is empty")
        raw_input()
        
    return(g)
    