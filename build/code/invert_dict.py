# -*- coding: utf-8 -*-

def invert_dict(d):
    
    inv_d = {v: k for k, v in d.items()}
    
    # error trap: repeated values in original dictionary -> lost information

    if len(d) != len(inv_d):
        
        raise RuntimeError('repeated values in original dictionary, cannot invert')
    
    return inv_d
      