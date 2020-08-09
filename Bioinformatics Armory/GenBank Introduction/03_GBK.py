from Bio import Entrez

with open('dataset/rosalind_gbk.txt') as input_data:
    genus, start_date, end_date = [line.strip() for line in input_data.readlines()]


Entrez.email="oscar.lopez94@protonmail.com"

handle= Entrez.esearch(db="nucleotide", term=genus+"[ORGN]", mindate=start_date, maxdate=end_date, datetype="pdat")

record = Entrez.read(handle)

print(record["Count"])

with open("dataset/rosalind_gbk_ans.txt", "w") as output_data:
    output_data.write(record['Count'])
