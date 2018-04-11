#!/bin/bash

cd stimuli && {
    curl -s -O 'https://gracula.psyc.virginia.edu/public/courseware/stimuli/[A-C]{0,2,6,8}.wav';
    cd -;
}
