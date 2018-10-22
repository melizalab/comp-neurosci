# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for signal-processing"""
from __future__ import print_function, division, absolute_import

import os
import glob
import ewave


def load_stimulus(stimname):
    """Loads the stimulus 'stimname'.

    Returns (osc, Fs), the sound pressure waveform and the sampling rate (in Hz)

    """
    stimfile = os.path.join("stimuli", stimname) + ".wav"
    wavfile = ewave.open(stimfile)
    return wavfile.read(), wavfile.sampling_rate


def load_raw_responses(unit, stimname):
    return [ewave.open(f).read() for f in glob.glob(os.path.join("data", "raw", "%s_%s*.wav" % (unit, stimname)))]


def specgram(signal, nfft, shift, sampling_rate, compress):
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
