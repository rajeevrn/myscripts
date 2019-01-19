#!/usr/bin/env python

"""
    Creating buckets using boto3
    Credential should be configured using aws configure    
    List all the buckets that do not have versioning     
"""

import boto3

session = boto3.Session()
s3_resource = boto3.resource('s3')

print "Listing of the S3 buckets which do not have versioning"
for bucket in s3_resource.buckets.all():
    bucketversion = s3_resource.BucketVersioning(bucket.name)
    bucketslist = bucketversion.status
    if(bucketslist != 'Enabled'):
        nonversionbuckets = []
        nonversionbuckets.append(bucket.name)
        #Listing the buckets without version(bvname)
        for bvname in nonversionbuckets:
            print bvname
