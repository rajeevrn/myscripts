#!/usr/bin/python

import json
import requests
import urllib3
import requests

'''
    my Blog: thecloudops.com
    Vmware vCenter api and starting the service based using rest
    Session needs to be established 
    Cookie validation can be done to check if it is getting the response or not
    Use the session id to start the service 
    Check for the response, load in json and check for status
    Args:
        url: URL to get the session 
    Returns:
        mysession: session created 
        mycookie: cookie that is generated    
''' 

# def session():   
#     urllib3.disable_warnings()
#     url="https://192.168.0.7/rest/com/vmware/cis/session"
#     global mysession 
#     mysession = requests.Session()
#     #Server validating 
#     serverresp = mysession.post(url,auth=('Administrator@vsphere.local','password'),verify=False)
#     mycookie = serverresp.text.split(":")[1]
#     #Check if the post action was successful
#  
#     if(serverresp.status_code == 200):
#          print "Connection to the vcenter succeeded"        
#     else:
#         print "Unable to connect with vcenter"
#     return 
# session()

'''
    Start an vcenter service using REST API(vmon)    
    Args:
        url2: url of the service + action
        mysession: Value of the session, earlier created 
    Return:
        service_post: Perform on action(Start/Stop)
        service_get: Get the status of the earlier performed action        
        service_json: Json loading
        service_state: Getting the service state
    Example:
        Below example Image builder service needs to be started/stopped
        imagebuilder: Imagebuilder service to be started
'''

def vcenteraction(vurl,vservice,action):
    
#     url2 = vurl + vservice  + '/' +action
    
    print "Service update for the url: " +url2
    service_post = mysession.post(url2, auth=('Administrator@vsphere.local','password'),verify=False)
    print service_post.status_code 
    if(service_post.status_code == 200):
        print "Post action is successful"
    else:
        print "Post action is not successful"
    service_get = mysession.get('https://192.168.0.7/rest/appliance/vmon/service/imagebuilder',verify=False)
    service_text = service_get.text
    print "JSON Value of service: " +service_text 
    service_json = json.loads(service_text)
    service_state = service_json["value"]["state"]
    
    print "\nCurrent Status of the %s service is: %s " %(vservice,service_state)
    
vcenteraction('https://192.168.0.7/rest/appliance/vmon/service/','imagebuilder','start')
