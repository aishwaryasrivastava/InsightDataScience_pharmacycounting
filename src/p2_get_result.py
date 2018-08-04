# This is part 2 of a solution to the pharmacy counting problem for the Insight Data Science fellowship.
# Running this script will read pharmacy.db and write the desired result in an output file.
# Author:	Aishwarya Srivastava
# Date:		Aug 4, 2018

# Libraries
import sqlite3
import sys

# Creating a database and establishing a connection
conn = sqlite3.connect(sys.argv[2])
c = conn.cursor()

# Fetching input file name
outputfilename = sys.argv[1]

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