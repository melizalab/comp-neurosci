# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Helpful functions for plotting"""
from __future__ import division
from __future__ import print_function

import numpy as np


def plot_some_spikes(ax, waveforms, n_max=20, **kwargs):
    """Plot up to n_max waveforms in ax"""
    from numpy import random
    N = waveforms.shape[0]
    sample = random.choice(N, min(N, n_max), replace=False)
    ax.cla()
    ax.plot(waveforms[sample].T, **kwargs)


def spike_detector(ax1, ax2, data, time):
    from IPython.display import display
    import ipywidgets as ipyw
    import quickspikes as qs

    osc = data.astype('d')

    thresh = r_max = osc.max() * 1.2
    thresh_w = ipyw.FloatSlider(value=thresh, min=0, max=r_max, step=r_max / 100,
                                description="Threshold:", continuous_update=False)
    display(thresh_w)

    ax1.plot(time, osc)
    line, = ax1.plot((time[0], time[-1]), (thresh, thresh), 'k')
    points, = ax1.plot([], [], 'ro')

    def update(thresh):
        from quickspikes.tools import filter_times
        line.set_ydata((thresh, thresh))
        det = qs.detector(thresh, 40)
        spike_t = filter_times(det.send(osc), 10, osc.size - 20)
        if spike_t:
            spike_t = np.asarray(spike_t)
            spike_w = np.asarray(qs.peaks(osc, spike_t, 10, 20))
            plot_some_spikes(ax2, spike_w, color='k', alpha=0.2)
            points.set_xdata(time[spike_t])
            points.set_ydata(osc[spike_t])
        ax1.figure.canvas.draw()

    ipyw.interactive_output(update, {"thresh": thresh_w})


def plot_raster(ax, trials):
    i = 0
    for i, trial in enumerate(trials):
        ax.vlines(trial, i, i + 0.5)
        i = i + 1


def spectrogram_explorer(ax, signal):
    from IPython.display import display
    import ipywidgets as ipyw

    NFFT = ipyw.IntSlider(value=256, min=8, max=1024, step=1, description="NFFT:")
    shift = ipyw.IntSlider(value=128, min=8, max=1024, step=1, description="shift:")
    compress = ipyw.FloatLogSlider(value=0, base=10, min=-2, max=5, step=0.2, description="compress:")
    thresh = r_max = osc.max() * 1.2
    thresh_w = ipyw.FloatSlider(value=thresh, min=0, max=r_max, step=r_max / 100,
                                description="Threshold:", continuous_update=False)
    display(thresh_w)

    ax1.plot(time, osc)
    line, = ax1.plot((time[0], time[-1]), (thresh, thresh), 'k')
    points, = ax1.plot([], [], 'ro')

    def update(thresh):
        from quickspikes.tools import filter_times
        line.set_ydata((thresh, thresh))
        det = qs.detector(thresh, 40)
        spike_t = filter_times(det.send(osc), 10, osc.size - 20)
        if spike_t:
            spike_t = np.asarray(spike_t)
            spike_w = np.asarray(qs.peaks(osc, spike_t, 10, 20))
            plot_some_spikes(ax2, spike_w, color='k', alpha=0.2)
            points.set_xdata(time[spike_t])
            points.set_ydata(osc[spike_t])
        ax1.figure.canvas.draw()

    ipyw.interactive_output(update, {"thresh": thresh_w})
