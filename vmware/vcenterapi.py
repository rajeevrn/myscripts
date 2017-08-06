#!/usr/bin/python

import json
import  requests
import urllib3


#  Wanted to disable the warnings. Only for demo, do not disable the warnings. 
urllib3.disable_warnings()

#URL of the appliance 
url = "https://192.168.0.9/rest/appliance/"
#API which you want to explore 
restdata = "/health/applmgmt";
#Verify=False - This makes the SSL verification as False
rdata = requests.get(url + restdata, verify=False)

#Reading the data and loading it as JSON so that it is easy to get the value 
hdata = rdata.text
mypar = json.loads(hdata)
myvalue = mypar['value']

#Checking the value
print "The current status health status of the appliance is:", myvalue.upper()
if myvalue == "green":
    print "VCSA health status is fine"        
elif myvalue == "yellow":
    print "Please check the Health Status, It is Yellow"
else:
    print "URGENT!!, Check the HealthStatus is Red"    