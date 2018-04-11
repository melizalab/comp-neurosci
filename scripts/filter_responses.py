#!/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" load starling data and massage it for easier analysis"""

import os
import nbank
import json

stimuli = ("A0", "A2", "A6", "A8",
           "B0", "B2", "B6", "B8",
           "C0", "C2", "C6", "C8",)

def rename_stimulus(s):
    return s[:2]

archive = "/home/data/starlings"
unitfile = "scripts/starling_units.tbl"

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
            stimname = rename_stimulus(pproc["stimulus"])
            if stimname not in stimuli:
                continue
            pprox.append({"events": pproc['events'],
                          "stimulus": stimname})

        if len(pprox) > 0:
            data["pprox"] = pprox
            ofp = open(outfile, "wt")
            json.dump(data, ofp)
            print("%s: wrote filtered json" % location)
        else:
            print("%s: skipped - no matching stimuli" % location)
