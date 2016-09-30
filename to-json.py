# For converting standards spreadsheet to JSON

# rows:
# 1. Standard Set
# 2. Grade Levels
# 3. Specific Grades
# 4. Content Areas
# 5. Standards
# 6. ID 

import csv
#import itertools
import json

filename = raw_input("Enter csv filename: ")

with open(filename , 'r') as standards:
	lines = []
	for line in standards:
		lines.append(line)


	matrix = []
	projects = []

	for i in range(0, len(lines)):
		project_list = lines[i].strip().split(",")
		matrix.append(project_list)
		if i >= 6:
			project = {}
			project["name"] = project_list[0]
			print ""
			print "-------------------------"
			print matrix[i][0]
			print "-------------------------"
			for j in range(1, len(project_list)):
				temp_p = {}
				
				if project_list[j] == "X":
					temp_p["Standard_Set"] = matrix[0][j]
					temp_p["Grade_Levels"] = matrix[1][j]

					print matrix[0][j]
					print matrix[1][j]
					print matrix[2][j]
					print matrix[3][j]
					print matrix[4][j]
					print matrix[5][j]
					print ""
			print ""
			print ""



#import json

#with open('data.js', 'w') as outfile:
#	json.dump(projects, outfile)

		