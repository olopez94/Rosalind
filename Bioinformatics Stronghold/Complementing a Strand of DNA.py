'''
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
  Given: A DNA string s of length at most 1000 bp.
  Return: The reverse complement sc of s.
  AAAACCCGGT
  ACCGGGTTTT
'''
dnaFile = open('./rosalind.txt','r')
reverseDna = dnaFile[::-1]

reverseDna = list(reverseDna)

for n, i in enumerate(reverseDna):
  if i == 'A':
    reverseDna[n] = 'T'
  elif i == 'G':
    reverseDna[n] = 'C'
  elif i == 'C':
    reverseDna[n] = 'G'
  elif i == 'T':
    reverseDna[n] = 'A'

reverseDna = ''.join(reverseDna)
