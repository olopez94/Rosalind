#!/usr/bin/env bash
#
#  April 5, 2024
# Function that transcribing DNA into RNA 
#

function dna2rna {
	cat "$1" | tr T U > dna2rna_result.txt

}

dna2rna $1
