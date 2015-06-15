# -*- coding: utf-8 -*-

import cPickle, copy

def add_variables(year, quarter):

    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    dst = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    mktshr = {}
    airport = {}
    
    for key in data:
        data_s = key.split('_')
        origin = data_s[0]
        dest = data_s[1]
        carrier = data_s[2]
        
        if carrier not in mktshr:
            mktshr[carrier] = {}
    
        if origin not in mktshr[carrier]:
            mktshr[carrier][origin] = data[key]['pax']
        else:
            mktshr[carrier][origin] += data[key]['pax']        
        
        if dest not in mktshr[carrier]:
            mktshr[carrier][dest] = data[key]['pax']
        else:
            mktshr[carrier][dest] += data[key]['pax']
        
        if origin not in airport:
            airport[origin] = data[key]['pax']
        else:
            airport[origin] += data[key]['pax']
            
        if dest not in airport:
            airport[dest] = data[key]['pax']
        else:
            airport[dest] += data[key]['pax']
    
    carrier_airport_mktshr = copy.deepcopy(mktshr)
    
    for carrier in mktshr:
        for airp in mktshr[carrier]:
            carrier_airport_mktshr[carrier][airp] = float(mktshr[carrier][airp])/float(airport[airp])
    
    #   unit test, airport HHI calculation
    
    airp_hhi = {}
    
    for airp in airport:
        
        sum_ = 0
        sum_hhi = 0
        
        for carrier in carrier_airport_mktshr:
            
            try:
                sum_ += carrier_airport_mktshr[carrier][airp]
                sum_hhi += carrier_airport_mktshr[carrier][airp]**2
            except KeyError:
                pass
            
        if (sum_ - 1.0) > 0.00000001:
            print 'error', airp, sum_
            sss
            
        if airp not in airp_hhi:
            airp_hhi[airp] = sum_hhi
    
    for key in data:
        
        data_s = key.split('_')
        origin = data_s[0]
        dest = data_s[1]
        carrier = data_s[2]
        
        mktshr_endpoints = [carrier_airport_mktshr[carrier][origin], carrier_airport_mktshr[carrier][dest]]
        
        data[key]['minAirportMktshr'] = min(mktshr_endpoints)
        data[key]['maxAirportMktshr'] = max(mktshr_endpoints)
        
        hhi_endpoints = [airp_hhi[origin], airp_hhi[dest]]
        
        data[key]['minAirportHHI'] = min(hhi_endpoints)
        data[key]['maxAirportHHI'] = max(hhi_endpoints)
        
    f = open(dst, 'wb')
    cPickle.dump(data, f)
    f.close()
    
    return None

