# -*- coding: utf-8 -*-
#
import numpy
from .helpers import _s3


class HammerMarloweStroud(object):
    '''
    P.C. Hammer, O.J. Marlowe and A.H. Stroud,
    Numerical Integration Over Simplexes and Cones,
    Mathematical Tables and Other Aids to Computation,
    Vol. 10, No. 55, Jul. 1956, pp. 130-137,
    <https://doi.org/10.1090/S0025-5718-1956-0086389-6>.

    Abstract:
    In this paper we develop numerical integration formulas for simplexes and
    cones in n-space for n>=2. While several papers have been written on
    numerical integration in higher spaces, most of these have dealt with
    hyperrectangular regions. For certain exceptions see [3]. Hammer and Wymore
    [1] have given a first general type theory designed through systematic use
    of cartesian product regions and affine transformations to extend the
    possible usefulness of formulas for each region.

    Two of the schemes also appear in

    P.C. Hammer, Arthur H. Stroud,
    Numerical Evaluation of Multiple Integrals II,
    Mathematical Tables and Other Aids to Computation.
    Vol. 12, No. 64 (Oct., 1958), pp. 272-280,
    <http://www.jstor.org/stable/2002370>
    '''
    def __init__(self, index):
        self.name = 'HMS(%d)' % index
        if index == 1:
            self.weights = numpy.concatenate([
                numpy.full(1, 1.0),
                ])
            self.bary = numpy.concatenate([
                _s3(),
                ])
            self.degree = 1
        elif index == 2:
            self.weights = numpy.concatenate([
                numpy.full(3, 1.0/3.0),
                ])
            self.bary = numpy.concatenate([
                _r(0.5),
                ])
            self.degree = 2
        elif index == 3:
            self.weights = numpy.concatenate([
                numpy.full(3, 1.0/3.0),
                ])
            self.bary = numpy.concatenate([
                _r(-0.5),
                ])
            self.degree = 2
        elif index == 4:
            self.weights = numpy.concatenate([
                numpy.full(1, -9.0/16.0),
                numpy.full(3, 25.0/48.0),
                ])
            self.bary = numpy.concatenate([
                _s3(),
                _r(0.4),
                ])
            self.degree = 3
        else:
            assert index == 5
            self.weights = numpy.concatenate([
                numpy.full(1, 9.0/40.0),
                (155.0 - numpy.sqrt(15.0)) / numpy.full(3, 1200.0),
                (155.0 + numpy.sqrt(15.0)) / numpy.full(3, 1200.0),
                ])
            self.bary = numpy.concatenate([
                _s3(),
                _r((1 + numpy.sqrt(15)) / 7.0),
                _r((1 - numpy.sqrt(15)) / 7.0),
                ])
            self.degree = 5

        self.points = self.bary[:, 1:]
        return


def _r(r):
    '''Given $r$ (as appearing in the article), it returns the barycentric
    coordinates of the three points.
    '''
    a = r + (1.0-r) / 3.0
    b = 0.5 * (1.0 - a)
    return numpy.array([
        [a, b, b],
        [b, a, b],
        [b, b, a],
        ])
