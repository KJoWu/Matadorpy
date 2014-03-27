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
    print("\n")    
    url = "http://matador.embl.de/proteins/" + info['link'] 
    response = urllib2.urlopen(url)
    html = response.read()    
    soup = BeautifulSoup(html)
    p=soup.findAll('li')
    clean_html = cleaned(p)
    check_html(clean_html)
    
#Cleaning the code to be easier to parse
def cleaned(line):
    newline = unicode.join(u'\n',map(unicode,line))
    newline = unicode(newline).encode('ascii','replace') 
    newline = newline.translate(string.maketrans("\n\t\r", "   "))  
    newline=newline.replace("  ", "").replace("<li>", "").replace("<ul>", "")
    newline = newline.replace("</li>", "").replace("</ul>", "")
    newline= newline = newline.split('<a href="../../drugs')
    return newline


def check_html(line):
    for words in line:
        word= words.strip()    
        
        #Check to See interaction type
        if ("Direct interaction" in word):
            interaction_type = "Direct"
        elif ("Indirect interaction" in word):
            interaction_type = "Indirect"
        elif("Direct or indirect" in word):
            interaction_type= "Both"
            
        #check to see pubmed and extract articles and drugs
        if ("pubmed" in word):
            print word            
           # regular expression for protein
            #regular expression for pmid's
            pass
        

if __name__ == "__main__":
    with open("items.csv") as f_obj:
        csv_reader(f_obj)