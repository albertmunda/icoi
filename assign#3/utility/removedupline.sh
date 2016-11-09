#!/bin/bash
cut -d' ' -f2,3 "$1" | awk '!seen[$0]++'
