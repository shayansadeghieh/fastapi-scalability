#!/bin/bash

# Variables
duration=5 # number of seconds to make that request for 
rate=3 # request per second
timeout=60 #timeout for a request in seconds

vegeta attack -duration=${duration}s -timeout=${timeout}s -rate=${rate} -targets=targets.list -output=results.bin
cat results.bin | vegeta plot > plot.html
open -a "Google Chrome" plot.html



