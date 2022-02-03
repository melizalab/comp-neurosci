# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Functions for loading pregenerated data into the notebook """
from __future__ import print_function, division, absolute_import

import os
import numpy as np

e2_std = 0.2
data_path = "data"

def mult_error_data(mu, N):
    """Generate N samples from a distribution with multiplicative error """
    from .dists import normal
    return mu * np.absolute(normal(1.0, e2_std).rvs(N)) / 5


def load_timeseries(*path):
    import ewave
    wavfile = ewave.open(os.path.join(data_path, *path), "r")
    return wavfile.read(memmap=False), wavfile.sampling_rate


def load_raw_responses(*path, unit, stimname, offset=-2):
    import ewave
    import glob
    r = []
    t = None
    for i, f in enumerate(glob.glob(os.path.join(data_path, *path, "%s_%s*.wav" % (unit, stimname)))):
        with ewave.open(f) as fp:
            r.append(fp.read())
            if i == 0:
                t = np.arange(0, fp.nframes / fp.sampling_rate, 1. / fp.sampling_rate) + offset
    # assumes that all the responses are the same duration
    return r, t


def load_pprox(*path):
    """ Loads pprox+json response data for unit and returns it in a Python dictionary """
    import json
    filename = os.path.join(data_path, *path) + ".json"
    with open(filename, 'rU') as fp:
        data = json.load(fp)
        return data


try:
    from comp_neurosci_uva.local_settings import *
except Exception as e:
    print(e)
    pass
