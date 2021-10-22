## Python Program to find all emails in a paragraph and write them in another text file...

import re

pattern = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
str = """Please contact human@zombocoder.com for assistance alternative is
final_coder@gmail.com  if none of them then ajak@gmail.com
or person is anonymous@yahoo.com"""
match = re.findall(pattern, str)


with open("regular-emails.txt","w+") as file:
	for i in match:
		file.write(i+"\n")


with open("regular-emails.txt","r+") as file:
	print(file.read())