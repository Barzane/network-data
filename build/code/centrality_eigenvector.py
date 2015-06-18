# -*- coding: utf-8 -*-

import numpy 
from scipy import linalg

def centrality_eigenvector(g) : 
    """CENTRALITY-EIGENVECTOR(g)
		n = g.size // dimension of g (number of nodes)
		w = vector of eigenvalues of g
		U = matrix of right-hand side eigenvectors of g, corresponding to w
		<w, U = scipy.linalg.eig(g)> // the eigenvectors are the rows of <U.T>
		<numpy.testing.assert_almost_equal(w * U, g.dot(U))> // error trap, checks decomposition
		max_eigenvalue_index = index corresponding to the largest (positive) eigenvalue
		<max_eigenvalue_index = int(numpy.argmax(w))>
<http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html>
eigenvector_c = row of <U.T> corresponding to max_eigenvalue_index
<eigenvector_c = (g.dot(U)).T[max_eigenvalue_index]>
eigenvector_map = dictionary, with key = node number, value = eigenvector centrality
<eigenvector_map = dict(zip(range(n), eigenvector_c))>
		return eigenvector_map"""
    
    n = len(g)
    w, U = linalg.eig(g)
    numpy.testing.assert_almost_equal(w * U, g.dot(U))
    max_eigenvalue_index = int(numpy.argmax(w))
    eigenvector_c = (U.T)[max_eigenvalue_index]
    
    if (eigenvector_c <= 0).all():
        eigenvector_c = (-eigenvector_c)
        
    eigenvector_c = numpy.real(eigenvector_c)
    eigenvector_map = dict(zip(range(n), eigenvector_c))
    
    sumsquare = 0
    
    for element in eigenvector_c:
        sumsquare = sumsquare + element**2
    
    return eigenvector_map