# -*- coding: utf-8 -*-
#
"""
W.H. Peirce,
Numerical integration over the planar annulus,
J. Soc. Indust. Appl. Math.,
Vol. 5, No. 2, June, 1957,
<https://www.jstor.org/stable/2098722>.
"""
import numpy

from .helpers import DiskScheme


def Peirce1957(m):
    k = 4 * m + 3
    theta = 2 * numpy.pi * numpy.arange(1, k + 2) / (k + 1)
    p, w = numpy.polynomial.legendre.leggauss(m + 1)
    # scale points to [r0, r1] (where r0 = 0, r1 = 1 for now)
    p = numpy.sqrt(0.5 * (p + 1.0))
    p_theta = numpy.dstack(numpy.meshgrid(p, theta)).reshape(-1, 2).T
    points = numpy.column_stack(
        [p_theta[0] * numpy.cos(p_theta[1]), p_theta[0] * numpy.sin(p_theta[1])]
    )
    # When integrating between 0 and 1, the weights are exactly the Gauss-Legendre
    # weights, scaled according to the disk area.
    weights = numpy.tile(0.5 * numpy.pi / (k + 1) * w, k + 1)
    return DiskScheme("Peirce 1957", k, weights, points)
