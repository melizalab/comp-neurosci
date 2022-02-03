# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions to load and manipulate pprox data"""
from __future__ import print_function, division, absolute_import


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
