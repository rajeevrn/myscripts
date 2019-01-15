#!/usr/bin/env python

"""
    Creating buckets using boto3
    Credential should be configured using aws configure 
"""

import boto3
import traceback

session = boto3.Session()
s3_client = session.client(service_name='s3')
try:
    s3_client.create_bucket(ACL='private',
    Bucket='mybuckettemp11289656111330911',
    CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'})       
    print "creation of the Bucket successful"
except Exception:
    traceback.print_exc()
    print "Creation of the bucket failed"
