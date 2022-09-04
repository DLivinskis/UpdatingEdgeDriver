# -*- coding: utf-8 -*-
"""
Created by Dmitrijs Livinskis; 03.09.2022

Supporting material taken from:
    https://www.youtube.com/watch?v=HDEvWfSk2So "How to download files from Web using Python and requests library"
    https://pynative.com/python-list-files-in-a-directory/ 
    https://stackoverflow.com/questions/3451111/unzipping-files-in-python "Unarchiving files"
    
"""

#libraries
import requests, os, zipfile

#/libraries

#Get Current Edge Version;There is a folder that is named exactly as Version of Edge. Name example "105.0.1343.25"
z = os.listdir('C:\Program Files (x86)\Microsoft\Edge\Application')
EdgeVersion = (z[0])
#/Get Current Edge Version

#Download the File; use "f" to put a variable inside a hyperlink; EdgeVersion is a variable that contains Current Edge Version
downloadUrl = f"https://msedgedriver.azureedge.net/{EdgeVersion}/edgedriver_win64.zip"


req = requests.get(downloadUrl)
filename = req.url[downloadUrl.rfind('/')+1:]

with open(filename, 'wb') as f: 
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
#/Download the File

#Unzip archive
with zipfile.ZipFile("W:\Coding\PythonProjects\DownloadFile\edgedriver_win64.zip", 'r') as zip_ref:
    zip_ref.extractall("W:\Coding\PythonProjects\DownloadFile")
#/Unzip archive   

#Delete Old Edgedriver
#/Delete Old Edgedriver

#Rename msedgedrive to edgedriver
#/Rename msedgedrive to edgedriver

#Move new edgedriver to folder
#/Move new edgedriver to folder


