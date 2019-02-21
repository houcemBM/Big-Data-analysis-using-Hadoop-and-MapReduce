#Reducer Code
#!/usr/bin/python
import sys
totalSale = 0
noOfSales=0
for line in sys.stdin:
 data_mapped = line.strip().split("\t")
 if len(data_mapped) != 2:
  continue
 thisKey, thisSale = data_mapped
 noOfSales=noOfSales+1
 totalSale+=float(thisSale)
print ("{0}\t{1}".format(noOfSales,totalSale))
