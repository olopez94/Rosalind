grep -o . rosalind_ini.txt  | sort | uniq -c | tr -s ' ' | cut -d ' ' -f2 | paste -sd ' '
