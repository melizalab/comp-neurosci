#!/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Extract raw extracellular recordings from arf files and output in WAV format """

# python 3 compatibility
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys
import nbank
import h5py as h5

stimuli = {
    "A0_motifs_000": "A0",
    "A2_motifs_000": "A2",
    "A6_motifs_000": "A6",
    "A8_motifs_000": "A8",
    "B0_motifs_000": "B0",
    "B2_motifs_000": "B2",
    "B6_motifs_000": "B6",
    "B8_motifs_000": "B8",
    "C0_motifs_000": "C0",
    "C2_motifs_000": "C2",
    "C6_motifs_000": "C6",
    "C8_motifs_000": "C8",
}

archive = "/home/data/starlings"

if __name__ == "__main__":

    import argparse

    p = argparse.ArgumentParser(description="extract raw extracellular recordings from arf files""")
    p.add_argument("unit", help="the name of the unit")
    p.add_argument("channel", help="the name of the channel(s) to extract", nargs="+")

    opts = p.parse_args()
