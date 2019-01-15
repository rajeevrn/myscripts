#!/usr/bin/env python

"""
    Listing of buckets using boto3
    Credential should be configured using aws configure 
"""

import boto3

session = boto3.Session()
s3_resource = boto3.resource('s3')

for bucket in s3_resource.buckets.all():
    print ("List of buckets" +bucket.name)