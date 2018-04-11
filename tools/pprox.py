# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions to load pprox data"""
from __future__ import print_function, division, absolute_import


def load(unit):
    """ Loads pprox+json response data for unit and returns it in a Python dictionary """
    import os
    import json
    filename = os.path.join("data", "spikes", unit) + ".json"
    with open(filename, 'rU') as fp:
        data = json.load(fp)
        return data


def select_stimulus(pprox, stim):
    """ Returns a list of arrays corresponding to the trials in which 'stim' was presented """
    from numpy import asarray
    return [asarray(d["events"]) for d in pprox["pprox"] if d["stimulus"] == stim]
