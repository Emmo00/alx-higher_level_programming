#!/bin/bash
# 
# runs doctest on the files passed as command line
# arguments
#
python3 -m doctest $@ -v
