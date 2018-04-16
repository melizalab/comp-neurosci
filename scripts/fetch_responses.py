#!/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" load starling data and massage it for easier analysis"""

import os
import nbank
import json

stimuli = {"A0_motifs_000": "A0",
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
           "C8_motifs_000": "C8",}

archive = "/home/data/starlings"
unitfile = "data/spikes/starling_units.tbl"

for i, line in enumerate(open(unitfile, "rU")):
    if i == 0:
        # skip header
        continue
    unit, area = line.strip().split()
    location = next(nbank.find(unit, local_only=True))
    outfile = os.path.join("data", "spikes", os.path.basename(location))

    with open(location, "rU") as fp:
        data = json.load(fp)

        # filter pprox:
        pprox = []
        for pproc in data["pprox"]:
            try:
                stimname = stimuli[pproc["stimulus"]]
            except KeyError:
                continue
            else:
                pprox.append({"events": pproc['events'],
                              "stimulus": stimname})

        if len(pprox) > 0:
            data["pprox"] = pprox
            ofp = open(outfile, "wt")
            json.dump(data, ofp)
            print("%s: wrote filtered json" % location)
        else:
            print("%s: skipped - no matching stimuli" % location)
