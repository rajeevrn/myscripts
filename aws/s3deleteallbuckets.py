#!/usr/bin/env python

"""
    Delete ALL buckets using boto3
    Credential should be configured using aws configure 
"""

import boto3

session = boto3.Session()
s3_resource = boto3.resource('s3')

for buckets in s3_resource.buckets.all():    
    buckets.objects.all().delete()
    buckets.delete()
    print "All Buckets are deleted"