# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions to load and manipulate pprox data"""
from __future__ import print_function, division, absolute_import


def load(unit):
    """ Loads pprox+json response data for unit and returns it in a Python dictionary """
    import os
    import json
    filename = os.path.join("data", "spikes", unit) + ".json"
    with open(filename, 'rU') as fp:
        data = json.load(fp)
        return data


def select_stimulus(pprox, stim, max_repeats=10):
    """ Returns a list of arrays corresponding to the trials in which 'stim' was presented """
    from numpy import asarray
    return [asarray(d["events"]) for d in pprox["pprox"] if d["stimulus"] == stim]


def rasterplot(axis, trials):
    """ Makes a rasterplot of trials on matplotlib axis """
    for i, trial in enumerate(trials):
        axis.vlines(trial, i, i + 0.5)


def get_stimuli(pprox):
    """ Returns the set of all stimuli in the pprox object """
    return {d["stimulus"] for d in pprox["pprox"]}
