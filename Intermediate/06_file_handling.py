### File handling ###

import os

c = 1
print("-" * 30)

# If you run the file directly with the "python" command in console, the root directory is the file.py directory
# If you are using the plugin in vscode for instance the root directory is the project/folder directory opened

file_name = "./my_file.txt"
file_a = open(file_name, "w+")
file_a.write("jesus\nricardo\npool\npech\npython")
file_a.seek(0)

#1 Read (read to end)
print(str(c),'- Read all the file:')
print(file_a.read())

c += 1
print("-" * 30)

#2
file_a.seek(0) # return the pointer to the beginning

print(str(c),'- Read a number of chars:')
print(file_a.read(4))

c += 1
print("-" * 30)

#3
file_a.seek(0) # return the pointer to the beginning

print(str(c),'- Read line by line(if there is additional lines a \\n will be printed):')
print(file_a.readline())

c += 1
print("-" * 30)

#4
file_a.seek(0) # return the pointer to the beginning

print(str(c),'- Read all the lines:')
for line in file_a.readlines():
	print(line)

c += 1
print("-" * 30)

#5
print(str(c),'- Write Tlaxaly at the end in new line:')

file_a.write("\nTlaxaly")
file_a.seek(0)
print(file_a.read())

c += 1
print("-" * 30)

file_a.close()
os.remove(file_name)

### JSON
import json
json_file_name = "./my_file.json"
json_file = open(json_file_name, "w+")

#6
print(str(c),'- JSON, create new file based on a dict my_file.json.')

json_test = {
	'name': 'Ricardo',
	'age': 35,
	'address': 'Calle Falsa 123',
	'languages': ['Python', 'Java', 'C++'],
	"height":1.77
}

json.dump(json_test, json_file, indent="\t")
#json.dump(json_test, json_file, indent=4) #ident using X number of spaces

c += 1
print("-" * 30)

#7
print(str(c),'- JSON, open and serialize my_file.json.')
json_file.seek(0)
json_test_load = json.load(json_file)
print(type(json_test_load))
print(json_test_load)
print(json_test_load['address'])

c += 1
print("-" * 30)

json_file.close()

### CSV
import csv
csv_file_name = "./my_file.csv"
csv_file = open(csv_file_name, "w+")


#8
print(str(c),'- CSV, create/open and write.')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'address', 'language', 'height'])
csv_writer.writerow(['Ricardo', '16x13', 'english', '1.62'])

c += 1
print("-" * 30)

#9
print(str(c),'- CSV, open and read.')
csv_file.seek(0)

csv_reader = csv.reader(csv_file)
##csv_reader.

c += 1
print("-" * 30)

csv_file.close()



### XML
#import xml

### XLSX
#import xlrd # It must be installed as third party
