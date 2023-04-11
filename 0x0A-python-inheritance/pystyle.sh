#!/bin/bash
#
# runs pycodestyle on files passed
#
python3 -m pycodestyle --show-source --show-pep8 $@
