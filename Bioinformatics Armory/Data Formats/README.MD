<H1>Data Formats</H1>

<P>
A number of different data presentation formats have been used to represent genetic strings. 
Three file formats are currently the most popular:

<UL>
 <LI><B>FASTA</B> (.fas, .fasta): used by practically all modern software and databases, including ClustalX, Paup, HyPhy, Rdp, and Dambe.</LI>
 <LI><B>NEXUS</B> (.nex, .nexus, .nxs): used by Paup, MrBayes, FigTree, and SplitsTree. </LI>
 <LI><B>PHYLIP</B>, or "Phylogeny Inference Package" (.phy): used by Phylip, Tree-Puzzle, PhyML, and a number of databases.</LI>
</UL>

In this problem, we will familarize ourselves with FASTA.

In FASTA format, a string is introduced by a line that begins with '>', followed by some information labeling the string. 
Subsequent lines contain the string itself; the next line beginning with '>' 
indicates that the current string is complete and begins the label of the next string in the file.

GenBank hosts its own file format for storing genome data, containing a large amount of information about each interval of DNA.
The GenBank file describes the interval's source, taxonomic position, authors, and features.
</P>

<H2> Problem </H2>

<P>
  <UL>
    <LI> <B>Given</B>: A collection of n (n≤10) GenBank entry IDs. </LI>
    <LI> <B>Return</B>: The shortest of the strings associated with the IDs in FASTA format. </LI>
  </UL>
</P>

<H2> Sample Dataset </H2>
<CODE>FJ817486 JX069768 JX469983</CODE>

<H2> Sample Output </H2>
<CODE>
>JX469983.1 Zea mays subsp. mays clone UT3343 G2-like transcription factor mRNA, partial cds
ATGATGTATCATGCGAAGAATTTTTCTGTGCCCTTTGCTCCGCAGAGGGCACAGGATAATGAGCATGCAA
GTAATATTGGAGGTATTGGTGGACCCAACATAAGCAACCCTGCTAATCCTGTAGGAAGTGGGAAACAACG
GCTACGGTGGACATCGGATCTTCATAATCGCTTTGTGGATGCCATCGCCCAGCTTGGTGGACCAGACAGA
GCTACACCTAAAGGGGTTCTCACTGTGATGGGTGTACCAGGGATCACAATTTATCATGTGAAGAGCCATC
TGCAGAAGTATCGCCTTGCAAAGTATATACCCGACTCTCCTGCTGAAGGTTCCAAGGACGAAAAGAAAGA
TTCGAGTGATTCCCTCTCGAACACGGATTCGGCACCAGGATTGCAAATCAATGAGGCACTAAAGATGCAA
ATGGAGGTTCAGAAGCGACTACATGAGCAACTCGAGGTTCAAAGACAACTGCAACTAAGAATTGAAGCAC
AAGGAAGATACTTGCAGATGATCATTGAGGAGCAACAAAAGCTTGGTGGATCAATTAAGGCTTCTGAGGA
TCAGAAGCTTTCTGATTCACCTCCAAGCTTAGATGACTACCCAGAGAGCATGCAACCTTCTCCCAAGAAA
CCAAGGATAGACGCATTATCACCAGATTCAGAGCGCGATACAACACAACCTGAATTCGAATCCCATTTGA
TCGGTCCGTGGGATCACGGCATTGCATTCCCAGTGGAGGAGTTCAAAGCAGGCCCTGCTATGAGCAAGTC
A

</CODE>

<H3>Programming Shortcut</H3>
<P>To search for particular access IDs, you can use the function <CODE><B>Bio.Entrez.efetch(db, rettype)</B></CODE>, which takes two parameters: 
 the <CODE><B>db</B></CODE> parameter takes the database to search, and the <CODE><B>rettype</B></CODE> parameter takes the data format to be returned. 

The following code illustrates <CODE><B>efetch()</B></CODE> in action. It obtains plain text records in FASTA format from NCBI's [Nucleotide] database.

<CODE>
from Bio import Entrez
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
records = handle.read()
print(records)
</CODE>

</P>
