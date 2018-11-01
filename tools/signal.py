# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for signal-processing"""
from __future__ import print_function, division, absolute_import

import os
import glob
import ewave
import numpy as np


def load_stimulus(stimname):
    """Loads the stimulus 'stimname'.

    Returns (osc, Fs), the sound pressure waveform and the sampling rate (in Hz)

    """
    stimfile = os.path.join("data", "stimuli", stimname) + ".wav"
    wavfile = ewave.open(stimfile)
    return wavfile.read(memmap=False), wavfile.sampling_rate


def load_raw_responses(unit, stimname, offset=-2):
    r = []
    t = None
    for i, f in enumerate(glob.glob(os.path.join("data", "raw", "%s_%s*.wav" % (unit, stimname)))):
        with ewave.open(f) as fp:
            r.append(fp.read())
            if i == 0:
                t = np.arange(0, fp.nframes / fp.sampling_rate, 1. / fp.sampling_rate) + offset
    # assumes that all the responses are the same duration
    return r, t


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
    from numpy import log10
    import libtfr
    # generate a transform object
    D = libtfr.mfft_dpss(nfft, 3, 5, nfft)
    # calculate the power spectrogram
    P = D.mtspec(signal, shift)
    freq, find = libtfr.fgrid(sampling_rate, nfft)
    bins = libtfr.tgrid(P, sampling_rate, shift)
    return (log10(P + compress) - log10(compress), freq, bins)
