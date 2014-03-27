#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import urllib2
import sys
from BeautifulSoup import BeautifulSoup
import re
import string

#Read csv file and convert it to a dictionary
def csv_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        find_interactions(line)
        
#access url and find interactions
def find_interactions(info):
    url = "http://matador.embl.de/proteins/" + info['link'] 
    response = urllib2.urlopen(url)
    html = response.read()    
    soup = BeautifulSoup(html)
    p= soup.findAll('ul')
    print p

    exit()


    
if __name__ == "__main__":
    with open("items.csv") as f_obj:
        csv_reader(f_obj)