# -*- coding: utf-8 -*-

import cPickle

def merge(src_data, full_data):
    
    print '[loading]', src_data
        
    f = open(src_data, 'r')
    data = cPickle.load(f)
    f.close()

#    http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression
        
    full_data.update(data)
    
    del data    
        
    return full_data

def wrapper(time_periods):
    
    full_data = {}
    
    for (year, quarter) in time_periods:

        src_data = '..\\output\\data_' + str(year) + '_' + str(quarter) + '.bin'
            
        try:
                            
            full_data = merge(src_data, full_data)
                
        except IOError:

            raise IOError('requested data unavailable: year ' + str(year) + ', quarter ' + str(quarter))
    
    dst_full_data = '..\\output\\data_full_with_network.bin'
    
    print '[saving]', dst_full_data    
    
    f = open(dst_full_data, 'wb')
    cPickle.dump(full_data, f)
    f.close()

    del full_data
       
    return None