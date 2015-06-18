# -*- coding: utf-8 -*-

def list_of_airports(data):
    """FUNCTION create list of airport codes
		INPUT	data dictionary for a single year-quarter
		SET	output list to be empty <output = []>
		FOR	each item in the list of data keys
			SPLIT	item into a list of strings <using item.split()>
			DETERMINE	origin (first element of split list) <Python counts from 0>
			DETERMINE	destination (second element of split list)
			IF	origin not in output list
				APPEND	origin to output list <using output.append(origin)>
			ENDIF
			IF	destination not in output list
				APPEND	destination to output list
			ENDIF
		ENDFOR
		SORT	output list alphabetically <using output.sort()>
		OUTPUT	sorted output list
	ENDFUNCTION"""
    
    keys_list = []
    all_airports = []

    for keys in data.keys():
        
        keys_list = keys.split("_")
        origin = keys_list[0]
        destination = keys_list[1]

        if origin not in all_airports :
            all_airports.append(origin)

        if destination not in all_airports : 
            all_airports.append(destination)

    all_airports.sort()
    
    return all_airports
    