# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 07:51:18 2023

@author: 388560
"""

#How to Access 
import arcgis
from arcgis.gis import GIS

#getpass for discrete password entry
import getpass
#use os for getting image files
import os
#use regex for numeric matching
import re
#local config
import config as cf

if cf.manual_password_entry == True:
    username = input('Username:')
    password = getpass.getpass('Password:')
else:
    username = cf.username
    password = cf.password
    


#Create portal GIS object
gis = GIS(url = cf.portal, username = username, password = password)

#Get feature layer by id
facilities = gis.content.get(cf.service_id)
#Output fl dataframe
facilities_fl = facilities.layers[cf.layer_index]
fl_df = facilities_fl.query(where = '1=1', as_df = True)


#Build Dictionary of Facility IDs and their Feature OIDs
#Facility ID : OID
dict_oid = {}
for index, row in fl_df.iterrows():
    try:
        #regex find numeric in id_row
        key = re.findall(cf.regex_string, row[cf.id_field])
        dict_oid[key[cf.regex_index]] = row[cf.oid_field]
    except:
        #No numeric in field
        print(row[cf.id_field], 'omitted')
        
        
#Match the ID from the photos to the ID in the Features

#dictionary to store OID and file paths
#OID : [Image Path1, Image Path 2,... Image path n]
oid_dict = {}



files = os.listdir(cf.path)
for file in files:
    id_key = ''
    try:
        #Pull numeric from file name and match it to feature layer
        id_key = dict_oid[re.findall(cf.regex_string, file)[cf.regex_index]]
        val = os.path.join(cf.path, file)
        
        #Collect additional images if multiple for ID
        try:
            #print(key, val)
            oid_dict[id_key].append(val)
        except:
            oid_dict[id_key] = [val]
    #print if image ID not in the feature layer
    except:
        print('no facility in feature layer', file)
    
#Create an Attachment manager
am = arcgis.features.managers.AttachmentManager(facilities_fl)

#checks if the image already exists on a feature
#if update_images bool is true, replaces the image with new file
#if filename doesn't already exist, adds file to feature

update_dict = {}
for k,v in oid_dict.items():
    attachment_list = am.get_list(k)
    for image in attachment_list:
        update_dict[image['name']] = image['id'] 
    for val in v:
        filename = os.path.basename(val)
        try:
            existing_id = update_dict[filename]
            if cf.update_images == True:
                print('Updating File: ',filename)
                am.update(k,existing_id,val)
            else:
                print(f'File {filename} already exists, Skipping')
            continue
        except:
            am.add(k, val)
            print('Adding New File: ',filename)
        