# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Functions for loading pregenerated data into the notebook """
from __future__ import print_function, division, absolute_import

import os
import numpy as np

from pathlib import Path
from typing import Tuple, List

import ewave

e2_std = 0.2
data_path = Path("data")


def mult_error_data(mu: np.number, N: int) -> np.ndarray:
    """Generate N samples from a distribution with multiplicative error"""
    from .dists import normal

    return mu * np.absolute(normal(1.0, e2_std).rvs(N)) / 5


def load_timeseries(subdir: Path) -> Tuple[np.ndarray, int]:
    wavfile = ewave.open(data_path / subdir, "r")
    return wavfile.read(memmap=False), wavfile.sampling_rate


def load_raw_responses(
    subdir: Path, *, unit: str, stimname: str, offset: float = -2
) -> Tuple[List[np.ndarray], np.ndarray]:
    r = []
    t = None
    path = data_path / subdir
    for i, f in enumerate(path.glob(f"{unit}_{stimname}*.wav")):
        with ewave.open(f) as fp:
            r.append(fp.read())
            if i == 0:
                t = (
                    np.arange(0, fp.nframes / fp.sampling_rate, 1.0 / fp.sampling_rate)
                    + offset
                )
    # assumes that all the responses are the same duration
    return r, t


def load_pprox(subdir: Path):
    """Loads pprox+json response data for unit and returns it in a Python dictionary"""
    import json

    filename = data_path / subdir.with_suffix(".json")
    with open(filename, "r") as fp:
        data = json.load(fp)
        return data


try:
    from comp_neurosci_uva.local_settings import data_path
except ImportError as e:
    pass
