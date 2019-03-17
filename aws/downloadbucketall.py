#!/usr/bin/env python

"""
    Download buckets using boto3
    Credential should be configured using aws configure 
"""

import boto3
import traceback
import subprocess
import os
import mysession
#import 
# 
mysession.transsession()
# s3_resource = boto3.resource('s3')
# bucket_name ="mytesting19501950"
# files_list = ['myfolder1', 'myfolder3']

#List all the buckets 
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('mytesting19501950')
print my_bucket
# conn = mysession.transsession() # assumes boto.cfg setup
# bucket = mysession.transsession()
# 
for obj in my_bucket.objects.all():
    print "--->" +obj.key

# 
# for i in s3_resource.buckets.all():
#     if (i.name == bucket_name):        
#         print "bucket is available for download"
#         print i
#         key = "myfolder1/myfolderaws1.txt"
#         mytask = key.split('/')
#         bucketdownload =  mytask[0]
#         filename = mytask[1]
#         print filename
#         folder =  '/tmp/' + bucketdownload
#         
#         print folder
#         os.mkdir(folder, 0755)
#         filename1 = '/tmp/' + bucketdownload + '/' + filename
#         print filename1
#         s3_resource.Bucket(bucket_name).download_file(key, filename1)
#         
#     else:
#         print "The file already exists" 












###

     print newfile
#     
     
#     s3_resource.Bucket(bucket_name).download_file(key, newfile)
#         
    
        
#     myfile = '/tmp/filename/' +  filename
#     print myfile
   # )
#     for i in filename:
#             print folders
#             filename1 = '/tmp/' + i + "/mytesting"
#             print filename1
#             s3_resource.Bucket(bucket_name).download_file(folders, filename1)
#             break
#     myfile = uuid.uuid4().hex
#     print "THE FILE NAME IS -----------------> " +myfile
#     folder =  '/tmp/awsdownloads'    
    #os.mkdir(folder, 0755)
#    print bucket_name
    
   

    #mysession.resource('s3').Bucket(bucket_name).download_file(folders, filename)
    
#print tempfile.gettempdir()

#  
#     #for i in s3_resource.buckets.all():
# #     if (i.name == bucket_name):        
# #         print "bucket is avadilable for download"
# #         print i
# #         key = "myfolder1/myfolderaws1.txt"
# #         mytask = key.split('/')
# #         bucketdownload =  mytask[0]
# #         filename = mytask[1]
# #         print filename
# #         folder =  '/tmp/' + bucketdownload
# #          
# #         print folder
# #         os.mkdir(folder, 0755)
# #         filename1 = '/tmp/' + bucketdownload + '/' + filename
# #         print filename1
# #         s3_resource.Bucket(bucket_name).download_file(key, filename1)
# #          
# #     else:
# #         print "The file already exists"