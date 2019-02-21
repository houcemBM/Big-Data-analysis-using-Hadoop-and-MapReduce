import sys
count=0


for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
     continue
  thisip, thisuripath = data_mapped
  if(thisip=="10.223.157.186"):
     count=count+1
print count
