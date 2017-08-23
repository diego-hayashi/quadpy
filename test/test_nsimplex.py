# -*- coding: utf-8 -*-
#
import numpy
import pytest
import quadpy

from helpers import (
    check_degree, integrate_monomial_over_standard_simplex
    )


@pytest.mark.parametrize(
    'scheme',
    [quadpy.nsimplex.GrundmannMoeller(dim, k)
     for dim in range(3, 7)
     for k in range(5)
     ]
    #
    + [quadpy.nsimplex.Stroud(dim, index)
       for dim in range(3, 7)
       for index in [
           'Tn 1-1', 'Tn 1-2',
           'Tn 2-1a', 'Tn 2-1b', 'Tn 2-2',
           'Tn 3-1', 'Tn 3-2', 'Tn 3-3', 'Tn 3-4', 'Tn 3-5', 'Tn 3-6a',
           'Tn 3-6b', 'Tn 3-7', 'Tn 3-8', 'Tn 3-9'
           ]
       ]
    + [quadpy.nsimplex.Stroud(dim, index)
       for dim in [3, 4, 6, 7]
       for index in ['Tn 3-10', 'Tn 3-11']
       ]
    #
    + [quadpy.nsimplex.Walkington(3, k) for k in [1, 2, 3, 5, 7]]
    + [quadpy.nsimplex.Walkington(4, k)
       for dim in range(4, 7)
       for k in [1, 2, 3]
       ]
    )
def test_scheme(scheme):
    n = scheme.dim
    simplex = numpy.zeros((n+1, n))
    for k in range(n):
        simplex[k+1, k] = 1.0
    degree = check_degree(
            lambda poly: quadpy.nsimplex.integrate(poly, simplex, scheme),
            integrate_monomial_over_standard_simplex,
            lambda k: quadpy.helpers.partition(k, n),
            scheme.degree + 1
            )
    assert degree >= scheme.degree, \
        'Observed: {}, expected: {}'.format(degree, scheme.degree)
    return


if __name__ == '__main__':
    n_ = 5
    scheme_ = quadpy.nsimplex.Stroud(n_, 'Tn 3-9')
    test_scheme(scheme_)
