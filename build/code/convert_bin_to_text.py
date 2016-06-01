# -*- coding: utf-8 -*-

import cPickle, copy

def convert():
    
    print '\nconvert .bin to .txt'
    
    src_data = '..\\output\\data_full_with_network.bin'
    
#    data .bin loaded from \output, not moved to \temp first
    
    print 'loading', src_data
    
    try:
        
        f = open(src_data, 'rb')
        data_hold = cPickle.load(f)
        f.close()

    except IOError:
    
        raise IOError('data unavailable', src_data)
  
    var_list = copy.deepcopy(data_hold[data_hold.keys()[0]].keys())
    
#    http://stackoverflow.com/questions/16581695/python-how-to-sort-lists-alphabetically-with-respect-to-capitalized-letters
    var_list = sorted(var_list, key=lambda L: (L.lower(), L))
    
    data_dict = {}
    
    for key in data_hold:
        
        data_dict[key] = []
        
        for var in var_list:
            
            data_dict[key].append(data_hold[key][var])
    
    output_string = ''

    first_key = data_dict.keys()[0].split('_')
    
    dst_txt = '..\\output\\'+'data_full_with_network.txt'

    header_line = 'origin' + '\t' + 'dest' + '\t' + 'carrier' +\
        '\t' + 'year' + '\t' + 'quarter' + '\t'

    for i in var_list:
        
        header_line += str(i)
        header_line += '\t'
        
    header_line = header_line.rstrip()    
    header_line += '\n'

    output_string += header_line

    for key in data_dict.keys():
        
        data_line = key.split('_') + data_dict[key]
        
        for item in data_line:
            
            output_string += str(item)
            output_string += '\t'
            
        output_string = output_string.rstrip()
        output_string += '\n'
        
    output_string = output_string.rstrip()

    print 'saving', dst_txt

    f = open(dst_txt, 'w')
    f.write(output_string)
    f.close()
    
    return None
