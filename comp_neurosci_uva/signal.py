# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for signal-processing"""
from __future__ import print_function, division, absolute_import

import os
import glob
import ewave
import numpy as np


def specgram(signal, sampling_rate, nfft=256, shift=128, compress=1):
    """
    Calculate a spectrogram of signal.

    Parameters:
    signal - the input signal (needs to be a 1D array)
    nfft   - the window size, in points
    shift  - how much to shift the window in each frame, in points
    sampling_rate - the number of samples per second in the signal
    compress - how much to compress the spectrogram. Effectively sets the floor of the
               spectrogram at log10(compress)

    Returns: the spectrogram, the frequency grid, and the time grid

    """
    from scipy.signal import spectrogram
    from numpy import log10
    f, t, P = spectrogram(signal, fs=sampling_rate, window='hamming', nperseg=nfft, noverlap=shift)
    return (log10(P + compress) - log10(compress), f, t)
