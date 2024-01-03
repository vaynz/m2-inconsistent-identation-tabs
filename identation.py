# -*- coding: utf-8 -*-
import re
import os

def fix_indentation(file_path):
	with open(file_path, 'r') as file:
		content = file.read()

	fixed_content = re.sub(r'\t', '    ', content) 
#	fixed_content = re.sub(r'\t', '	', content) can be changed like that too

	with open(file_path, 'w') as file:
		file.write(fixed_content)

def fix_directory(directory):
	for subdir, _, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(subdir, file)
			if file_path.endswith('.py'):
				fix_indentation(file_path)

check_dir = 'C:\Users\Vaynz\Desktop\test' ## change with urs
fix_directory(check_dir)
