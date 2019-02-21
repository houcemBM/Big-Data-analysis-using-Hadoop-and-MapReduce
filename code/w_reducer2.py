//Reducer Code


import sys


oldpath=None
thishits=0
maxhits=0
maxhitspath=None
for line in sys.stdin:
  data_mapped = line.strip()
  if(data_mapped.find("?")!=-1):
     data_mapped=data_mapped[0:data_mapped.find("?")]
  thispath= data_mapped
  if oldpath and thispath!=oldpath:
    if maxhits<thishits:
        maxhits=thishits
    maxhitspath=oldpath
        thishits=0
    oldpath=thispath
    thishits+=1
  if maxhits<thishits:
     maxhits=thishits
     maxhitspath=oldpath
  print "{0}\t{1}".format(maxhits,maxhitspath)
