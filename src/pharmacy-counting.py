# This is a solution to the pharmacy counting problem for the Insight Data Science fellowship
# Author:	Aishwarya Srivastava
# Date:		Aug 4, 2018

# Libraries
import sqlite3
import sys

# Creating a database and establishing a connection
conn = sqlite3.connect('pharmacy.db')
c = conn.cursor()

# Reading user input for file names
inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

# Reading  input file and populating the database
inputfile = open('./input/' + inputfilename,'r')
c.execute("CREATE TABLE prescriber (id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost)")
i = 0
for line in inputfile:
	myLine = line
	if myLine[-1:] == '\n':
		myLine = myLine[:-1]
	values = myLine.split(',')
	# Make sure drugs with ',' in their names are handled
	if len(values) > 5:
		values[3] += values[4]
		values[4:] = values[5:]
	ID, LNAME, FNAME, DRUG, COST = values
	if i > 0:
		# Make sure names with "'" in them are handled
		LNAME = LNAME.replace("'",'.')
		FNAME = FNAME.replace("'",'.')
		c.execute("INSERT INTO prescriber VALUES ('%s','%s','%s','%s',%s)" % (ID,LNAME,FNAME,DRUG,COST))
		conn.commit()
	i = i + 1
inputfile.close()

# Fetching the result from the database and writing to output file in proper format
outputfile = open('./output/'+outputfilename,'w+')
outputfile.write('drug_name,num_prescriber,total_cost\n')
c.execute("SELECT drug_name, count(id), sum(drug_cost) FROM prescriber GROUP BY drug_name ORDER BY sum(drug_cost) desc")
result = c.fetchall()
for DRUG,NUM_CUSTOMERS,COST in result:
	outputfile.write(",".join([DRUG,str(NUM_CUSTOMERS),str(COST)])+'\n')
conn.commit()

outputfile.close()
conn.close()