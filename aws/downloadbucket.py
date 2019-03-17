#!/usr/bin/env python

"""
    Download buckets using boto3
    Credential should be configured using aws configure 
"""
import boto3
import traceback

def download_bucket(bucket_name):
    print "Bucket from which the objects will be downloaded: " +bucket_name
    s3_resource = boto3.resource('s3')    
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket_name)
    for obj in my_bucket.objects.all():    
        key = obj.key
        mytask = key.split('/')
        filename = mytask[1]       
        for i in filename:
            print "Files which will be downloaded: " +filename
            newfile = '/tmp/' + filename
            print "Downloaded location of the file is: " + newfile            
            try:                 
                s3_resource.Bucket(bucket_name).download_file(key, newfile)
                break
            except Exception:
                traceback.print_exc()
""" 
For downloading the files in the bucket 
"""                
download_bucket('thecloudopsbucket')