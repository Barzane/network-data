# -*- coding: utf-8 -*-

def map_airports_code(all_airports):
    """FUNCTION	create a dictionary to map airport codes to integers
		INPUT	list all_airports from the function in Task 4 <these will be the keys>
            SET	integer n equal to length of all_airports <use len(all_airports)>
            SET	list nodes equal to a list of integers from 0 to n-1 <use range(n)>
            SET	output dictionary to have keys from all_airports list, and corresponding
	 	values from nodes list <use output = dict(zip(all_airports, nodes))>
           OUTPUT output dictionary
	ENDFUNCTION"""


    nodes = range(len(all_airports))
    N = dict(zip(all_airports, nodes))
    
    return N
