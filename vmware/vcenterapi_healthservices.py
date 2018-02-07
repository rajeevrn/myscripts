#!/usr/bin/python

import json
import urllib3
import requests

'''
    thecloudops.com
    Text file containing the services that needs to be checked
    Report if the service is not running     
''' 
def session():   
    urllib3.disable_warnings()
    url="https://192.168.0.7/rest/com/vmware/cis/session"
    global mysession 
    mysession = requests.Session()
    #Server validating 
    serverresp = mysession.post(url,auth=('Administrator@vsphere.local','password'),verify=False)    
    if(serverresp.status_code == 200):
        print("\033[1;34;47m Connection to VCENTER succeeded \n")  
    else:
        print("\033[1;34;47m Unable to connect with vcenter \n") 
    return
session()

def vhealthcheck(url):    
    with open('/home/rajeev/vservices.txt') as f:       
        content = f.read().splitlines()    
        for vservice in content:            
            url2 =  url + vservice
            service_get = mysession.get(url2,verify=False)
            service_text = service_get.text
            service_json = json.loads(service_text)
            service_state = service_json["value"]["state"]  
            if(service_state == "STOPPED"):
                print(("\033[1;31;47m Current Status of the %s service is: %s \n") %(vservice,service_state))    
vhealthcheck('https://192.168.0.7/rest/appliance/vmon/service/')