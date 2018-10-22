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
import arf
import h5py as h5
import ewave
import collections

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
    p.add_argument("channel", help="the name of the channel to extract")

    args = p.parse_args()

    location = nbank.get(args.unit, local_only=True)
    stim_counter = collections.defaultdict(int)
    with h5.File(location, "r") as fp:
        for entry_name in arf.keys_by_creation(fp):
            entry = fp[entry_name]
            stim = entry['stimuli']['name', 0].decode('utf-8')
            if stim not in stimuli:
                print("%s -> skipping (%s)" % (entry_name, stim))
            else:
                stim_counter[stim] += 1
                outfile = "%s_%s_%d.wav" % (args.unit, stimuli[stim], stim_counter[stim])
                print("%s -> %s" % (entry_name, outfile))
                dset = entry[args.channel]
                sampling_rate = dset.attrs['sampling_rate']
                with ewave.open(outfile, mode='w', sampling_rate=sampling_rate, dtype=dset.dtype) as ofp:
                    ofp.write(dset[:])
