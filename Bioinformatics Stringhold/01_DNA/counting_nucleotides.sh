#!/usr/bin/env bash

function nucleotidesCount {
		
	a=$(grep -o "A" < "$1" | wc -l) 
	c=$(grep -o "C" < "$1" | wc -l)
	g=$(grep -o "G" < "$1" | wc -l)
	t=$(grep -o "T" < "$1" | wc -l)
	printf "%s %s %s %s\n" "$a" "$c" "$g" "$t" > dna_count_result.txt
	printf "Result saved on dna_count_result.txt"	
}

nucleotidesCount $1

