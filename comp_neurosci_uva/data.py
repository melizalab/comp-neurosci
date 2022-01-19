# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Some data that we import to hide it from the notebook """
from __future__ import print_function, division, absolute_import

import numpy as np

e2_std = 0.2


def mult_error_data(mu, N):
    """Generate N samples from a distribution with multiplicative error """
    from .dists import normal
    return mu * np.absolute(normal(1.0, e2_std).rvs(N)) / 5
