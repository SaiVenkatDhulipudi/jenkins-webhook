#!/bin/bash
#create dir
mkdir -p build
#copy files
cp lambda_handler.py build
cp requirements.txt build
#change directory
cd build
#install requirements.txt
pip install -r requirements.txt -t .
#remove files
rm -rf *.dist-info
#zip files
zip -r ../jenkins_webhook.zip  ./  -x  "*/__pycache__/*"
