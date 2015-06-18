# -*- coding: utf-8 -*-

import cPickle

def list_of_airlines(data):
    """FUNCTION create list of airlines codes
		INPUT	data dictionary for a single year-quarter
		SET	output list to be empty <output = []>
		FOR	each item in the list of data keys
			SPLIT	item into a list of strings <using item.split()>
			DETERMINE	airline (third element of split list) 
                 IF	airline not in output list
				APPEND airline to output list
			ENDIF
		ENDFOR
		SORT	output list alphabetically 
		OUTPUT	sorted output list
	ENDFUNCTION"""
     
    keys_list = []
    all_airlines = []

    for keys in data.keys():
        
        keys_list = keys.split("_")
        airline = keys_list[2]
        
        if airline not in all_airlines:
            all_airlines.append(airline)
       
    all_airlines.sort()
    
    return(all_airlines)