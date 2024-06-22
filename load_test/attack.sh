#!/bin/bash

# duration = 1 # number of seconds to make that request for 
# rate = 1 # request per second

vegeta attack -duration=5s -rate=1 -targets=targets.list -output=results.bin
cat results.bin | vegeta plot > plot.html
open -a "Google Chrome" plot.html



