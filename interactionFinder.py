#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import nltk
import urllib
import sys


#Read csv file and convert it to a dictionary
def csv_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        find_interactions(line)
        
#access url and find interactions
#by accessing url online and reading text. 
def find_interactions(info):
    url = "http://matador.embl.de/drugs/" + info['link']     
    html = urllib.urlopen(url).read()

    
if __name__ == "__main__":
    with open("items.csv") as f_obj:
        csv_reader(f_obj)