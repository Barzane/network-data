# -*- coding: utf-8 -*-

def add_node(i, j, D, inlist):
    """ADD-NODE(i, j, D, inlist)
		// extend a partial (m < l(i, j) segment) geodesic, starting at i, with all valid m + 1 segments
// update partial geodesic and terminate if last node is only one step away from j
		if D[inlist[-1]][j] == 1
			return [append j to inlist] // <inlist.append(j) followed by return [inlist]>
		// if partial geodesic > 1 step away from j, find all valid next segments
		outlist = []
		for k = 0 to D.size - 1
			inlist_mutable = inlist // do not modify input inlist, in case of multiple branches
			if (k not in inlist) and k != j and D[inlist[-1]][k] == 1 and D[k][j] == D[i][j] - D[i][k]
				append [append k to inlist_mutable] to outlist // separate the append steps
		return outlist"""

    if D[inlist[-1]][j] == 1:
        inlist.append(j)
        return [inlist]
        
    outlist = []    

    for k in range(len(D)):

        inlist_mutable = inlist[:]        

        if (k not in inlist) and (k != j) and  (D[inlist[-1]][k] == 1) and (D[k][j] == D[i][j] - D[i][k]) and (D[k][j] == D[i][j] - len(inlist)) :
            inlist_mutable.append(k)
            outlist.append(inlist_mutable)
            
    return outlist
    
def shortest_paths(i, j, D):
    """SHORTEST-PATHS(i, j, D)
		// find all shortest paths from node i to node j in a network (N, g)
		// D = (l(i, j)) is the distance matrix corresponding to g (from Task 15)
// element l(i, j) of D is the length of any geodesic between i and j
		// terminate immediately if i and j are neighbours (geodesic length 1)
		if D[i][j] == 1
			return [[i, j]]
		// terminate immediately if i and j are not path-connected (geodesic length infinity)
		if D[i][j] == infinity
			return [[]]
		// terminate with error message if i == j
		if D[i][j] == 0
			print “Start and end nodes are identical”
			stop
		// if geodesic length > 1, identify first (length 1) segments i to k, of all geodesics from i to j
// (this is the initialization step for non-trivial geodesics)
		paths = []
		for k = 0 to D.size
			if k != j and k != i and D[i][k] == 1 and D[k][j] == D[i][j] - 1
				append [i, k] to paths
		// if geodesic length > 1 then, for every identified first segment, find all possible geodesics from i to j, by iteratively adding valid second, third, ..., segments, e.g., i to k to a to b to j
// (this is the update step for non-trivial geodesics)
		// by definition, no geodesic can have length > n - 1, if nodes i and j are path-connected, and this implicitly bounds the following while loop; while infinite geodesics will have been dealt with above
		flag = True // flag set to True indicates an ongoing iteration / search 
		while flag == True
			newpaths = []
			for item in paths
				newitems = ADD-NODE(i, j, D, item)
				for element in newitems
					append element to newpaths // can this operation be performed in a single step? i.e., flatten list and add all elements to another list? (otherwise ok to use an explicit loop)
			paths = newpaths // update list of every (partial) geodesic of length m to list of (partial) geodesics of length m + 1, where a partial geodesic can have multiple continuations (branches)
			flag = False // iterations will end, unless some geodesic still requires completion
			for path in paths
				if path[-1] != j // is this path incomplete? (if so, continue loop)
					flag = True // flag remains False if all geodesics fully specified
		// error trap: each geodesic must have D[i][j] + 1 nodes
		for path in paths
			if path.size != D[i][j] + 1
				print “Geodesic incorrect length”
				stop
		return paths"""

    if D[i][j] == 1:
        return [[i, j]]
        
    if D[i][j] == float("inf"):
        return [[]]
        
    if D[i][j] == 0:
        return 'Start and end nodes are identical'
        
    paths = []
    
    for k in range(len(D)):
        
        if (k != j) and (k != i) and (D[i][k] == 1) and (D[k][j] == D[i][j] - 1):
            paths.append([i, k])
    
    flag = True
    
    while flag == True:
        
        newpaths = []
        
        for item in paths:
            
            newitems = add_node(i, j, D, item)

            for element in newitems:
                newpaths.append(element)

        paths = newpaths[:]
        flag = False
        
        for path in paths:

            if path[-1] != j:
                flag = True
                
    for path in paths:
        
        if len(path) != D[i][j] + 1:
            return 'Geodesic incorrect length'
            
    return paths
