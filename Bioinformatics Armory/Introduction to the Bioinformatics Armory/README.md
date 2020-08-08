<h1> Introduction to the Bioinformatics Armory </h1>

<p> 
 This initial problem is aimed at familiarizing you with Rosalind's task-solving pipeline. 
To solve it, you merely have to take a given DNA sequence and find its nucleotide counts; 
this problem is equivalent to “Counting DNA Nucleotides” in the Stronghold. 
</p>

<p>
  Of the many tools for DNA sequence analysis, one of the most popular is the Sequence Manipulation Suite. 
  Commonly known as SMS 2, it comprises a collection of programs for generating, formatting, and analyzing short strands of DNA and polypeptides.
</p>

<p>
One of the simplest SMS 2 programs, called <b>DNA stats</b>, counts the number of occurrences of each nucleotide in a given strand of DNA. 
</p>

<ul>
  <li> Given: A DNA string s of length at most 1000 bp.</li>
  
  <li> Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. 
  Note: You must provide your answer in the format shown in the sample output below.</li>
</ul>


<H2> Sample Dataset </H2>
<CODE><P> AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC</P> </CODE>

<H2> Sample Output </H2>
<CODE><P> 20 12 17 21 </P></CODE>

<H3> Programming Shortcut</H3>

<P> Our default choice for existing functions and modules to analyze biological data is BioPython, 
a set of freely available tools for computational biology that are written in Python. </P>

<P> 
BioPython offers a specific data structure called <B>Seq</B> for representing sequences.
<B>Seq</B> represents an extension of the "str" (string) object type that is built into Python by supporting additional biologically relevant methods like <B>translate()</B> and <B>reverse_complement()</B>.
</P>

<P> In this problem, you can easily use the built-in Python method <B>.count()</B> for strings. Here's how you could count the occurrences of 'A' found in a <B>Seq</B> object.</P>

<CODE>
from Bio.Seq import Seq

 my_seq = Seq("AGTACACTGGT")
 
  my_seq.count("A")
</CODE>

