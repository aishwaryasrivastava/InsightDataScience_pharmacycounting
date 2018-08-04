# Introduction
Hello! This is my submission for the Insight Data Science coding challenge. 

# Usage
This solution is made of two parts. Part 1 reads the input file and builds a SQLite database using user input, containing all the information in the input file. Part 2 simply queries the database provided by the user and writes the result in the desired format in the specified output file. The program will look for the input and output files in the `input` and `output` directories of the root folder, respectively. To run this program, use the following commands:

`python p1_create_db.py inputfilename.txt pharmacy.db`

`python p2_get_result.py outputfilename.txt pharmacy.db`

The programs do not print anything to the console.

