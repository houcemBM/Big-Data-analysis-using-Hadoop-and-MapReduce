// Find the web page with maximum hits
//Mapper Code

import sys

for line in sys.stdin:
   data = line.strip().split(" ")
   if len(data) == 10:
     ip, client, user, date, zone, method,uripath, protocol, statusCode, objectsize = data
     print "{0}".format(uripath)
