#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CIE UCS Colourspace
===================

Defines the *CIE UCS* colourspace transformations:

-   :func:`XYZ_to_UCS`
-   :func:`UCS_to_XYZ`
-   :func:`UCS_to_uv`
-   :func:`UCS_uv_to_xy`

See Also
--------
`CIE UCS Colourspace IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/blob/master/notebooks/models/cie_ucs.ipynb>`_  # noqa

References
----------
.. [1]  Wikipedia. (n.d.). CIE 1960 color space. Retrieved February 24, 2014,
        from http://en.wikipedia.org/wiki/CIE_1960_color_space
.. [2]  Wikipedia. (n.d.). Relation to CIE XYZ. Retrieved February 24, 2014,
        from
        http://en.wikipedia.org/wiki/CIE_1960_color_space#Relation_to_CIE_XYZ
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.utilities import tsplit, tstack

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['XYZ_to_UCS',
           'UCS_to_XYZ',
           'UCS_to_uv',
           'UCS_uv_to_xy']


def XYZ_to_UCS(XYZ):
    """
    Converts from *CIE XYZ* tristimulus values to *CIE UCS* colourspace.

    Parameters
    ----------
    XYZ : array_like
        *CIE XYZ* tristimulus values.

    Returns
    -------
    ndarray
        *CIE UCS* colourspace array.

    Notes
    -----
    -   Input *CIE XYZ* tristimulus values are in domain [0, 1].
    -   Output *CIE UCS* colourspace array is in domain [0, 1].

    Examples
    --------
    >>> XYZ = np.array([0.07049534, 0.10080000, 0.09558313])
    >>> XYZ_to_UCS(XYZ)  # doctest: +ELLIPSIS
    array([ 0.0469968...,  0.1008    ,  0.1637439...])
    """

    X, Y, Z = tsplit(XYZ)

    UVW = tstack((2 / 3 * X, Y, 1 / 2 * (-X + 3 * Y + Z)))

    return UVW


def UCS_to_XYZ(UVW):
    """
    Converts from *CIE UCS* colourspace to *CIE XYZ* tristimulus values.

    Parameters
    ----------
    UVW : array_like
        *CIE UCS* colourspace array.

    Returns
    -------
    ndarray
        *CIE XYZ* tristimulus values.

    Notes
    -----
    -   Input *CIE UCS* colourspace array is in domain [0, 1].
    -   Output *CIE XYZ* tristimulus values are in domain [0, 1].

    Examples
    --------
    >>> UVW = np.array([0.04699689, 0.10080000, 0.16374390])
    >>> UCS_to_XYZ(UVW)  # doctest: +ELLIPSIS
    array([ 0.0704953...,  0.1008    ,  0.0955831...])
    """

    U, V, W = tsplit(UVW)

    XYZ = tstack((3 / 2 * U, V, 3 / 2 * U - (3 * V) + (2 * W)))

    return XYZ


def UCS_to_uv(UVW):
    """
    Returns the *uv* chromaticity coordinates from given *CIE UCS* colourspace
    array.

    Parameters
    ----------
    UVW : array_like
        *CIE UCS* colourspace array.

    Returns
    -------
    ndarray
        *uv* chromaticity coordinates.

    Notes
    -----
    -   Input *CIE UCS* colourspace array is in domain [0, 1].
    -   Output *uv* chromaticity coordinates are in domain [0, 1].

    Examples
    --------
    >>> UCS = np.array([0.04699689, 0.10080000, 0.16374390])
    >>> UCS_to_uv(UCS)  # doctest: +ELLIPSIS
    array([ 0.1508530...,  0.3235531...])
    """

    U, V, W = tsplit(UVW)

    uv = tstack((U / (U + V + W), V / (U + V + W)))

    return uv


def UCS_uv_to_xy(uv):
    """
    Returns the *xy* chromaticity coordinates from given *CIE UCS* colourspace
    *uv* chromaticity coordinates.

    Parameters
    ----------
    uv : array_like
        *CIE UCS uv* chromaticity coordinates.

    Returns
    -------
    ndarray
        *xy* chromaticity coordinates.

    Notes
    -----
    -   Input *uv* chromaticity coordinates are in domain [0, 1].
    -   Output *xy* chromaticity coordinates are in domain [0, 1].

    Examples
    --------
    >>> uv = np.array([0.15085308732766581, 0.3235531372954405])
    >>> UCS_uv_to_xy(uv)  # doctest: +ELLIPSIS
    array([ 0.2641477...,  0.3777000...])
    """

    u, v = tsplit(uv)

    xy = tstack((3 * u / (2 * u - 8 * v + 4), 2 * v / (2 * u - 8 * v + 4)))

    return xy
