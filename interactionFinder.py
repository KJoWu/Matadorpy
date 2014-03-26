import csv
 
#Read csv file
def csv_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print line
        #find_interaction(line)
        
#access url and find interactions


if __name__ == "__main__":
    with open("items.csv") as f_obj:
        csv_reader(f_obj)