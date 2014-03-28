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
    check_html(clean_html, info)
    
#Cleaning the code to be easier to parse
def cleaned(line):
    newline = unicode.join(u'\n',map(unicode,line))
    newline = unicode(newline).encode('ascii','replace') 
    newline = newline.translate(string.maketrans("\n\t\r", "   "))  
    newline=newline.replace("  ", "").replace("<li>", "").replace("<ul>", "")
    newline = newline.replace("</li>", "").replace("</ul>", "")
    newline= newline = newline.split('<a href="../../drugs')
    return newline


def check_html(line, info):
    count=0;
    for words in line:
        word= words.strip()    
        
        #Check to See interaction type
        if("interaction" in word):
            count=1;
            if ("Direct interaction" in word):
                interaction_type = "Direct"
            elif ("Indirect interaction" in word):
                interaction_type = "Indirect"
            elif("Direct or indirect" in word):
                interaction_type= "Both"
            continue;
        
        #check to see pubmed and extract articles and drugs
        if ("pubmed" in word):
            Find1 = re.compile(r'\/\d{4}/">\w+</a>')
            Find2 =  re.compile(r'>\w+<')
            Find_id = re.compile(r'uids=\d*')
            drugPath = re.search(Find1, word)
            
            #Get Drug
            if (drugPath):
                d_line= drugPath.group()
                drug = re.search(Find2, d_line)
                drug = drug.group().replace(">","").replace("<","")
                #needed if Beautiful soup has duplicates
                if (count==1):
                    first_drug = drug;
                    count=2;
                elif (count==2):
                    if(first_drug==drug):
                        break;
            #Get PMID
                pmid= Find_id.findall(word)
                for url in pmid:
                    url =url.replace("uids=","")
                    print "drug: " + drug + " pmid: " + url + " interaction: " + interaction_type + "protein: " + info['proteinName']
               
            
            

if __name__ == "__main__":
    with open("items.csv") as f_obj:
        csv_reader(f_obj)