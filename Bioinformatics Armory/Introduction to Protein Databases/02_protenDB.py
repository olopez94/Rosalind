from Bio import ExPASy
from Bio import SwissProt
'''
with open("") as input_data:
    UniProt_ID = input_data.read().strip()
'''
UniProt_ID = "B5ZC00"

with ExPASy.get_sprot_raw(UniProt_ID) as handle:
    record = SwissProt.read(handle)


bio_proc= []
for item in record.cross_references:
    if item[0] == 'GO' and item[2][0] == 'P':
        bio_proc.append(item[2].lstrip('P:'))


print('\n'.join(bio_proc))
print("Saving file...")
with open('prueba.txt', 'w') as output_data:
    output_data.write('\n'.join(bio_proc))
