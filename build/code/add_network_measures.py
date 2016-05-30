# -*- coding: utf-8 -*-

import cPickle, numpy

import list_of_airlines
import list_of_airports
import map_airports_code
import adjacency_matrix
import remove_zeros
import invert_dict
import distance_matrix
import degree_centrality
import closeness_centrality
import centrality_betweenness
import centrality_eigenvector
import density_degree_distribution
import route_level_g
import connected

import other_carrier_centrality

def add_network(year, quarter):

    test_output = True

    print '\nadd network measures to data_year_quarter.bin, save to \\temp'

    src = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    print '\nloading', src, '\n'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    all_airlines = list_of_airlines.list_of_airlines(data)    
    all_airports = list_of_airports.list_of_airports(data)
    
    N = map_airports_code.map_airports_code(all_airports)
    
    DC_dict = {}
    CC_dict = {}
    BC_dict = {}
    EC_dict = {}
    
    density_dict = {}
    diameter_dict = {}
    nodes_dict = {}
    edges_dict = {}
    
    DCroute_dict = {}
    CCroute_dict = {}
    BCroute_dict = {}
    ECroute_dict = {}
    
    count = 0
    
    for carrier in all_airlines:
        
        test_condition = (carrier == 'AA' and year == 2013 and quarter == 3)         
        
        print '\t' + carrier + ' (' + str(count + 1) + ' of ' + str(len(all_airlines)) + ')'
        
        DC_dict[carrier] = {}
        CC_dict[carrier] = {}
        BC_dict[carrier] = {}
        EC_dict[carrier] = {}
        
        DCroute_dict[carrier] = {}
        CCroute_dict[carrier] = {}
        BCroute_dict[carrier] = {}
        ECroute_dict[carrier] = {}
        
        g = adjacency_matrix.adjacency_matrix(data, N, carrier)
        
        Nbar, gbar = remove_zeros.remove_zeros(N, g)
        
        number_nodes = len(gbar)
        number_edges = sum(sum(gbar)) / 2
        
        nodes_dict[carrier] = number_nodes
        edges_dict[carrier] = number_edges
        
        network = (N, g)
        network_bar = (Nbar, gbar)
        inv_d = invert_dict.invert_dict(Nbar)
        
        network_star = route_level_g.route_level_g(network_bar)        
        Nstar = network_star[0]
        gstar = network_star[1]
        inv_d_star = invert_dict.invert_dict(Nstar)
            
        try:
            
            diameter_g = connected.connected(gbar)
            
        except:
            
            diameter_g = 'NA'

        if test_output and test_condition:

            print 'Nbar', Nbar
            print 'gbar[2]', gbar[2] # Austin-Bergstrom International Airport            
            print 'number_nodes', number_nodes
            print 'number_edges', number_edges
            print 'inv_d_star', inv_d_star
            number_nodes_star = len(gstar)
            number_edges_star = sum(sum(gstar)) / 2
            print 'number_nodes_star', number_nodes_star
            print 'number_edges_star', number_edges_star
            print 'diameter_g', diameter_g
            
        sss
            
#        diameter_gstar = connected.connected(gstar)
#        
#        print 'diameter g = ', diameter_g
#        print 'diameter gstar = ', diameter_gstar
        
        D, average_path_length = distance_matrix.distance_matrix(gbar)
        
        if len(Nstar) > 1:
            Dstar, average_path_length_star = distance_matrix.distance_matrix(gstar)
            
        density, Pd = density_degree_distribution.density_degree_distribution(network_bar)
        
#        try:
#            
#            density_star, Pd_star = density_degree_distribution.density_degree_distribution(network_star)
#            print density, density_star
#            
#        except ZeroDivisionError:
#            
#            pass

        diameter_dict[carrier] = diameter_g
            
        density_dict[carrier] = density
            
        DC = degree_centrality.degree_centrality(network_bar)
        DCroute = degree_centrality.degree_centrality(network_star)
        
        CC = closeness_centrality.closeness_centrality(gbar)
        
        if len(Nstar) > 1:
            CCroute = closeness_centrality.closeness_centrality(gstar)
        
        eigenvector_map = centrality_eigenvector.centrality_eigenvector(gbar)
        eigenvector_map_route = centrality_eigenvector.centrality_eigenvector(gstar)
        
        if len(Nbar) > 2 and not numpy.isinf(average_path_length):
            BC = centrality_betweenness.all_centrality_betweenness(D)
            
#        if len(Nstar) > 1 and not numpy.isinf(average_path_length_star):
#            BCroute = centrality_betweenness.all_centrality_betweenness(Dstar)
    
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
            
        for key in eigenvector_map_route:
            ECroute_dict[carrier][inv_d_star[key]] = eigenvector_map_route[key]
        
        count += 1
    
    centrality_dicts = ({'betweenness': BC_dict, 'closeness': 
        CC_dict, 'degree': DC_dict, 'eigenvector': EC_dict})
    
    other_centrality = other_carrier_centrality.centrality(centrality_dicts)
    
    for i in data:
        origin = i.split('_')[0]
        dest = i.split('_')[1]
        route = origin + '_' + dest
        carrier = i.split('_')[2]
        
        # add minimum, maximum degree centrality variable    
        
        data[i]['mindegree'] = min(DC_dict[carrier][origin], DC_dict[carrier][dest])
        data[i]['maxdegree'] = max(DC_dict[carrier][origin], DC_dict[carrier][dest])
    
        # add origin, destination degree centrality variable
    
        data[i]['origindegree'] = DC_dict[carrier][origin]
        data[i]['destinationdegree'] = DC_dict[carrier][dest]
        
        # add route-level degree centrality variable    
        
        data[i]['routedegree'] = DCroute_dict[carrier][route]
    
        # add minimum, maximum closeness centrality variable    
        
        data[i]['mincloseness'] = min(CC_dict[carrier][origin], CC_dict[carrier][dest])
        data[i]['maxcloseness'] = max(CC_dict[carrier][origin], CC_dict[carrier][dest])

        # add origin, destination closeness centrality variable
    
        data[i]['origincloseness'] = CC_dict[carrier][origin]
        data[i]['destinationcloseness'] = CC_dict[carrier][dest]

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
    
        # add origin, destination betweenness centrality variable    
        
        try:
            
            data[i]['originbetweenness'] = BC_dict[carrier][origin]
            data[i]['destinationbetweenness'] = BC_dict[carrier][dest]
            
        except KeyError:
            
            data[i]['originbetweenness'] = 'NA'
            data[i]['destinationbetweenness'] = 'NA'
            
        # add minimum, maximum eigenvector centrality variable    
        
        data[i]['mineigenvector'] = min(EC_dict[carrier][origin], EC_dict[carrier][dest])
        data[i]['maxeigenvector'] = max(EC_dict[carrier][origin], EC_dict[carrier][dest])
    
        # add origin, destination eigenvector centrality variable    
        
        data[i]['origineigenvector'] = EC_dict[carrier][origin]
        data[i]['destinationeigenvector'] = EC_dict[carrier][dest]
        
        # add route-level eigenvector centrality variable    
        
        data[i]['routeeigenvector'] = ECroute_dict[carrier][route]
    
        # add density
    
        data[i]['density'] = density_dict[carrier]
        
        # add diameter
    
        data[i]['diameter'] = diameter_dict[carrier]
        
        # add number of nodes
    
        data[i]['nodes'] = nodes_dict[carrier]
        
        # add number of edges
    
        data[i]['edges'] = edges_dict[carrier]
    
    # save bin datafile to \temp (same filename as \input datafile)
        
    filename = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(filename, 'wb')
    cPickle.dump(data, f)
    f.close()
    
    return None
