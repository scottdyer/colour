from __future__ import absolute_import

from .common import get_steps, get_closest, to_ndarray, is_uniform, is_iterable, is_number, is_even_integer
from .coordinates import *
from . import coordinates
from .extrapolation import Extrapolator1d
from .interpolation import LinearInterpolator, SpragueInterpolator
from .matrix import is_identity
from .regression import linear_regression

__all__ = ["get_steps", "get_closest", "to_ndarray", "is_uniform", "is_iterable", "is_number", "is_even_integer"]
__all__ += coordinates.__all__
__all__ += ["Extrapolator1d",
            "LinearInterpolator", "SpragueInterpolator",
            "is_identity",
            "linear_regression"]