# add_arcgis_enterprise_attachments
<div id="top"></div>




<!-- ABOUT THE PROJECT -->
## About The Project


This is a simple script attaches files to features in a arcgis hosted feature layer based on a regex match between a field and filename



<!-- GETTING STARTED -->
## Getting Started

Change the run.bat file to point to your ArcGIS Pro python environment

### Prerequisites


* ArcGIS Pro


### Installation

2. Set the portal location and username and password (or use manual entry)
   ```
   portal = 'https://www.arcgis.com'
   username = 'userNAME'
   password = 'P@$$w0Rd!'
   ```
3. Set path of the files to attach
   ```
   path = '\\PATH\TO\FILES\'
   
   ```

4. Set the field containing the match string and the OID field of the layer
   ```
   id_field = 'ID FIeld'
   oid_field = 'OBJECTID'
   ```
5. Set the regex matching string\index to return
   ```
   #Default will match the first numeric grouping in a string
   regex_string = r'\d+'
   regex_index = 0
   ```
   
   
6. Set whether you want to update existing files or ignore (pass) files with the same filename
   ```
   update_images = False
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the run.bat file








<!-- CONTACT -->
## Contact

Keinan Marks -  keinan@keinanmarks.com


<p align="right">(<a href="#top">back to top</a>)</p>

