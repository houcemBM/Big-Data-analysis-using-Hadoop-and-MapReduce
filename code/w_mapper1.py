Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> #!/usr/bin/python
# 10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
import sys


for line in sys.stdin:
   data = line.strip().split(" ")
   if len(data) == 10:
      ip, client, user, date, zone, method,uripath, protocol, statusCode, object      size = data
      print "{0}\t{1}".format(ip, uripath)
