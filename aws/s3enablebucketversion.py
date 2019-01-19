#!/usr/bin/env python

"""
    Creating buckets using boto3
    Credential should be configured using aws configure    
    Enable versioning for all the available buckets     
"""
import boto3

session = boto3.Session()
s3_resource = boto3.resource('s3')
print "Listing of the S3 buckets which do not have versioning"
for bucket in s3_resource.buckets.all():
    bucketversion = s3_resource.BucketVersioning(bucket.name)
    bucketslist = bucketversion.status
    #Checking if the buckets are enabled or not
    if(bucketslist != 'Enabled'):
        print "Enabling versioning for bucket:" + bucket.name
        bucketversion.enable(bucket.name)
