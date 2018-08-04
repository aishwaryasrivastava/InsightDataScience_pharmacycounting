# This is part 1 of a solution to the pharmacy counting problem for the Insight Data Science fellowship.
# Running this script will create a database called pharmacy.db which will contain all the information parsed from the input file.
# Author:	Aishwarya Srivastava
# Date:		Aug 4, 2018

# Libraries
import sqlite3
import sys

# Creating a database and establishing a connection
conn = sqlite3.connect(sys.argv[2])
c = conn.cursor()

# Fetching input file name
inputfilename = sys.argv[1]

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
conn.close()