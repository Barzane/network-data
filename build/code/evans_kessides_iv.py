# -*- coding: utf-8 -*-

import cPickle, numpy, copy, operator

from scipy.stats.stats import pearsonr

def add_iv(year, quarter):
        
    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    dst = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
#    route_carrier_mktshr must first be created, saved to \temp, by competitive_dummy.py
#    call the current function from within competitive_dummy.py, to ensure this
    
    src_route_carrier_mktshr = '..\\temp\\route_carrier_mktshr_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    f = open(src_route_carrier_mktshr, 'rb')
    route_carrier_mktshr = cPickle.load(f)
    f.close()
        
    evans_kessides_iv = {}    
    
    for route in route_carrier_mktshr:
                
        route_x = copy.deepcopy(route_carrier_mktshr[route])
        
        if route in evans_kessides_iv:
            raise IndexError('duplicate route in evans_kessides_iv dictionary')
        
        evans_kessides_iv[route] = {}
        
#        http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

        route_data = sorted(route_x.items(), key = operator.itemgetter(1))
        route_data.reverse()
        
#        check for non-unique route market share
#        how to define the IV in this case?
        
        route_mvals = route_x.values()
        route_mvals2 = set(route_mvals)
        route_mvals2 = list(route_mvals)
        
        route_mvals.sort()
        route_mvals2.sort()        
        
        if route_mvals != route_mvals2:
            raise NotImplementedError('non-unique route market share')
        
        route_iv = []
                
        for item_num in range(len(route_data)):
            
            if item_num <= 1:
                route_iv.append((route_data[item_num][0], item_num + 1))
            else:
                route_iv.append((route_data[item_num][0], 3))
        
        evans_kessides_iv[route] = dict(route_iv)
        
#        print route
#        print route_carrier_mktshr[route]
    
    for key in data:
        
        data_s = key.split('_')
        origin = data_s[0]
        dest = data_s[1]
        carrier = data_s[2]
        
        route = origin + '_' + dest
        
        data[key]['evans_kessides_iv'] = evans_kessides_iv[route][carrier]

#    by construction, Evans & Kessides IV is negatively correlated with route-carrier market share

    corr_x = []
    corr_y = []
    
    for route in route_carrier_mktshr:
        for carrier in route_carrier_mktshr[route]:
            corr_x.append(route_carrier_mktshr[route][carrier])
            corr_y.append(evans_kessides_iv[route][carrier])

    print '\t' + 'Pearson correlation (route mkt share, Evans & Kessides IV) = ' + str(pearsonr(corr_x, corr_y)[0])
    
    f = open(dst, 'wb')
    cPickle.dump(data, f)
    f.close()
    
    return None
