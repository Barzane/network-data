# -*- coding: utf-8 -*-

def centrality(centrality_dicts):
    
    centrality_types = centrality_dicts.keys()
    
    all_carriers = centrality_dicts[centrality_types[0]].keys()
    all_carriers.sort()

#    check carrier list constant across centrality measures

    for centrality in centrality_types[1:]:
        
        all_carriers_check = centrality_dicts[centrality].keys()
        all_carriers_check.sort()
        
        if all_carriers != all_carriers_check:
            
            raise ValueError('carrier list not constant across centrality measures')
    
    output = {}
        
    for centrality in centrality_dicts:
        
        output[centrality] = {}        
        
        for carrier in centrality_dicts[centrality]:
            
            output[centrality][carrier] = {}            
            
            for airport in centrality_dicts[centrality][carrier]:
                
                output[centrality][carrier][airport] = {}                
                
#                print centrality, carrier, airport, centrality_dicts[centrality][carrier][airport]
                
                for carrier2 in centrality_dicts[centrality]:
                    
                    if carrier2 != carrier:
                        
                        try:
                            
                            centrality_dicts[centrality][carrier2][airport]
#                            print '...', carrier2, centrality_dicts[centrality][carrier2][airport]
                            output[centrality][carrier][airport][carrier2] = centrality_dicts[centrality][carrier2][airport]
                        
                        except KeyError:
                            
                            pass
    
    return output
