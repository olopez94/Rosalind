#!/usr/bin/env bash
#
# April 5, 2024
#
# Complementing a Strand of DNA
#

function reverse_dna () {
	cat "$1" | rev | tr ATCG TAGC > reverse_dna.txt
	printf "Result saved on 'reverse_dna.txt' file\n"

}

reverse_dna $1

