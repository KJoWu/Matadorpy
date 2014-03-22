import csv
filtered_list=[]
csvread = list(csv.reader(open('interactions.csv', 'rb'), delimiter='\t'))
for row in csvread:
    if row[2]=="DrugBank":
        continue;
    else:
        print row[2]
        
