#!/usr/bin/python

import json
import requests
import urllib3

def apidata(url,restdata):
#  Wanted to disable the warnings. Only for demo, do not disable the warnings. 
   urllib3.disable_warnings()    
   rdata = requests.get(url + restdata, verify=False)
   hdata = rdata.text 
   mypar = json.loads(hdata)   
   myvalue = mypar['value']
   print "Current Status:", myvalue.upper()
   if myvalue == "green":
        print "VCSA Status is fine"
   elif myvalue == "yellow":
        print "Check the Status, It is Yellow"
   else:
        print "URGENT!!, Check the Status is Red"     
   return
   
#Example to get the health status 
  #1. URL of the VCSA Appliance
  #2. restdata= Health status of the appliance
   
apidata("https://192.168.0.7/rest/appliance/","/health/applmgmt")