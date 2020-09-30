

import os

#print (os.getcwd())

#os.chdir("C:/Users/Harish/downloads")

#print (os.getcwd())

#print (os.listdir())
import re
regex = '(<property name="(.*?)">(.*?)<\/property>)'
read_line = True

for each in os.listdir():
	path = os.path.join(os.getcwd(), each)
	folder, filename = os.path.split(path)
	file = os.path.splitext(filename)
	if file[1] == '.log':
		file_name = file[0] + file[1]
		final_path = os.path.join(os.getcwd(), file_name)
		print (final_path)
		with open(final_path, 'r') as input_file:
			match_list = []
			if read_line == True:
				for line in input_file:
					for match in re.finditer(regex, line):
						match_text = match.group()
						match_list.append(match_text)
						#print (match_text)
		# 	else:
		# 		data = f.read()
		# 		for match in re.finditer(regex, data, re.S):
		# 			match_text = match.group()
		# 			match_list.append(match_text)
		# input_file.close()




'''
with open("Sample.log", 'r') as input_file:
	for each in input_file:
		print (each)
'''