//Reducer Code

import sys

count=0

for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
    continue
  thisip, thisuripath = data_mapped
  if(thisuripath=="/assets/js/the-associates.js"):
    count=count+1
print count
