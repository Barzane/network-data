# -*- coding: utf-8 -*-

import numpy

from invert_dict import invert_dict

def route_level_g(network):
    
    N = network[0]
    g = network[1]
    
#    test case
#    N = {'one':0, 'two':1, 'three':2, 'four':3, 'five':4}
#    g = numpy.array([[0,0,1,0,0], [0,0,1,0,1], [1,1,0,1,1], [0,0,1,0,1], [0,1,1,1,0]])    
    
    inv_d = invert_dict(N)
    
    number_of_nodes = len(N)
    number_of_routes = int(sum(sum(g)) / 2)
    
    route_list = []
    
    gstar = numpy.zeros((number_of_routes, number_of_routes), dtype=int)
    
#    identify all routes from g
    
    for row in range(number_of_nodes):
        for col in range(row + 1, number_of_nodes):
            
            if g[row][col] == 1:
                
                route = inv_d[row] + '_' + inv_d[col]
                route_list.append(route)
    
    route_dict = dict(zip(range(number_of_routes), route_list))
    
#    node = route
#    link = two routes (nodes) have one endpoint in common
#    no own-links
    
    for route1 in range(number_of_routes):
        
        endpoint1 = route_dict[route1].split('_')[0]
        endpoint2 = route_dict[route1].split('_')[1]
            
        for route2 in range(route1 + 1, number_of_routes):
            
            link_found = (endpoint1 in route_dict[route2]) or (endpoint2 in route_dict[route2])
            
            if link_found:
                
                gstar[route1][route2] = 1
                gstar[route2][route1] = 1
                
#    walks of length 2

    g2 = g.dot(g)
    
#    by construction, number of walks of length 2 (i>j)
#    must equal number of links in gstar (i>j)    
    
    checksum = (sum(sum(numpy.triu(g2, 1))) != sum(sum(gstar)) / 2)
    
    if checksum:
        raise ArithmeticError('gstar checksum condition not satisfied')
    
    network_star = (invert_dict(route_dict), gstar)
    
    return network_star

