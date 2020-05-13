'''

Problem
  Given: A file containing at most 1000 lines.
  Return: A file containing all the even-numbered lines from the original file.  Assume 1-based numbering of lines.
'''
i = 1

readFile = open('rosalind_ini5.txt', 'r')   
outFile = open('output.txt', 'w')      
for line in readFile.readlines():
	if i % 2 == 0 :
		outFile.write(line)
	i+= 1
