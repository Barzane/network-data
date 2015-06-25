# -*- coding: utf-8 -*-

import cPickle, numpy

from list_of_airlines import list_of_airlines
from list_of_airports import list_of_airports
from map_airports_code import map_airports_code
from adjacency_matrix import adjacency_matrix
from remove_zeros import remove_zeros
from invert_dict import invert_dict
from distance_matrix import distance_matrix
from degree_centrality import degree_centrality
from closeness_centrality import closeness_centrality
from centrality_betweenness import all_centrality_betweenness
from centrality_eigenvector import centrality_eigenvector
from density_degree_distribution import density_degree_distribution
from route_level_g import route_level_g

def add_network(year, quarter):

    src = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    all_airlines = list_of_airlines(data)
    all_airports = list_of_airports(data)
    N = map_airports_code(all_airports)  
    
    DC_dict = {}
    CC_dict = {}
    BC_dict = {}
    EC_dict = {}
    
    density_dict = {}
    
    DCroute_dict = {}
    CCroute_dict = {}
    BCroute_dict = {}
    ECroute_dict = {}
    
    count = 0
    
    for carrier in all_airlines:
        
        print '\t' + carrier + ' (' + str(count + 1) + ' of ' + str(len(all_airlines)) + ')'
        
        DC_dict[carrier] = {}
        CC_dict[carrier] = {}
        BC_dict[carrier] = {}
        EC_dict[carrier] = {}
        
        DCroute_dict[carrier] = {}
        CCroute_dict[carrier] = {}
        BCroute_dict[carrier] = {}
        ECroute_dict[carrier] = {}
        
        g = adjacency_matrix(data, N, carrier)
        Nbar, gbar = remove_zeros(N, g)
        network = (N, g)
        network_bar = (Nbar,gbar)
        inv_d = invert_dict(Nbar)
        
        network_star = route_level_g(network_bar)        
        Nstar = network_star[0]
        gstar = network_star[1]
        inv_d_star = invert_dict(Nstar)
            
        D, average_path_length = distance_matrix(gbar)
        density, Pd = density_degree_distribution(network_bar)
        
        density_dict[carrier] = density
            
        DC = degree_centrality(network_bar)
        DCroute = degree_centrality(network_star)
        
        CC = closeness_centrality(gbar)
        
        if len(Nstar) > 1:
            CCroute = closeness_centrality(gstar)
        
        eigenvector_map = centrality_eigenvector(gbar)
        
        if len(Nbar) > 2 and not numpy.isinf(average_path_length):
            BC = all_centrality_betweenness(D)
    
        for key in DC:
            DC_dict[carrier][inv_d[key]] = DC[key]
        
        for key in DCroute:
            DCroute_dict[carrier][inv_d_star[key]] = DCroute[key]
            
        for key in CC:
            CC_dict[carrier][inv_d[key]] = CC[key]
        
        if len(Nstar) > 1:
            for key in CCroute:
                CCroute_dict[carrier][inv_d_star[key]] = CCroute[key]
        
        if len(Nbar) > 2 and not numpy.isinf(average_path_length):
            for key in BC:
                BC_dict[carrier][inv_d[key]] = BC[key]
        
        for key in eigenvector_map:
            EC_dict[carrier][inv_d[key]] = eigenvector_map[key]
        
        count += 1
    
    for i in data:
        origin = i.split('_')[0]
        dest = i.split('_')[1]
        route = origin + '_' + dest
        carrier = i.split('_')[2]
        
        # add minimum, maximum degree centrality variable    
        
        data[i]['mindegree'] = min(DC_dict[carrier][origin], DC_dict[carrier][dest])
        data[i]['maxdegree'] = max(DC_dict[carrier][origin], DC_dict[carrier][dest])
    
        # add route-level degree centrality variable    
        
        data[i]['routedegree'] = DCroute_dict[carrier][route]
    
        # add minimum, maximum closeness centrality variable    
        
        data[i]['mincloseness'] = min(CC_dict[carrier][origin], CC_dict[carrier][dest])
        data[i]['maxcloseness'] = max(CC_dict[carrier][origin], CC_dict[carrier][dest])

        # add route-level closeness centrality variable    
        
        try:
            
            data[i]['routecloseness'] = CCroute_dict[carrier][route]
            
        except KeyError:
            
            data[i]['routecloseness'] = 'NA'
        
        # add minimum, maximum betweenness centrality variable    
        
        try:
            
            data[i]['minbetweenness'] = min(BC_dict[carrier][origin], BC_dict[carrier][dest])
            data[i]['maxbetweenness'] = max(BC_dict[carrier][origin], BC_dict[carrier][dest])
            
        except KeyError:
            
            data[i]['minbetweenness'] = 'NA'
            data[i]['maxbetweenness'] = 'NA'
    
        # add minimum, maximum eigenvector centrality variable    
        
        data[i]['mineigenvector'] = min(EC_dict[carrier][origin], EC_dict[carrier][dest])
        data[i]['maxeigenvector'] = max(EC_dict[carrier][origin], EC_dict[carrier][dest])
    
        # add density
    
        data[i]['density'] = density_dict[carrier]
    
    # save bin datafile to \temp (same filename as \input datafile)
        
    filename = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(filename, 'wb')
    cPickle.dump(data, f)
    f.close()
    
    return None
