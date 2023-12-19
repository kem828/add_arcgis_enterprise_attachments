# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 07:47:57 2023

@author: Keinan Marks
keinan@keinanmarks.com
"""



#Log in to Portal
portal = 'https://www.arcgis.com'

#username = 'USERNAME'
#password = 'P@SSW0RD'
manual_password_entry = True

#Id of feature service
service_id = '' #eg'7d1b813995a94990b592f8df242716ee'
#index of layer at service
layer_index = 0

#path to images
path = r'\\PATH\\TO\\FILES\\'


#Define field in feature layer with the facility ID numeric
id_field = 'ID FIeld'
#Define field in feature layer with oid
oid_field = 'OBJECTID'

#regex string to match between file names and field
#default (r'\d+') is first grouped numeric
#eg any feature where the first grouped numeric = the first grouped numeric of 
#a filename, will have that file attached
regex_string = r'\d+'
#index of regex return to use. eg first numeric group in value
regex_index = 0


#bool to decide if images with same name on feature should be replaced
#if true, files replaced, if False, files skipped
update_images = False


