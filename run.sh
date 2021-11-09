#!/bin/bash

BASEDIR=$(dirname $(readlink -f "$0"))
cd "$BASEDIR/src"
python3 main.py
