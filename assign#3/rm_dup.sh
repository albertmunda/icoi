cut -d' ' -f2,3 sample1.rtf | awk '!seen[$0]++'
