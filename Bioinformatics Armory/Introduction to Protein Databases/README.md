<H1>Introduction to Protein Databases</H1>

<P>
Proteins are identified in different labs around the world, and data about them is gathered into freely accessible databases.
A central repository for protein data is UniProt, a comprehensive high-quality database established by an international consortium. 
</P>

<H2> Problem </H2>
<P> 
You can see a complete description of a protein by entering its UniProt access ID into the site's query field.
Equivalently, you may simply insert its ID (<B>uniprot_id</B>) directly into a UniProt hyperlink.
</P>

<P> For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00 </P>

<P> Swiss-Prot holds protein data as a structured .txt file. You can obtain it by simply adding <B>.txt</B>- to the link </P>

<UL>
  <LI> <B>Given:</B> The UniProt ID of a protein. </LI>
  <LI> <B>Return: </B> A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).</LI>
</UL>


<H3> Programming Shortcut </H3>

<P> ExPASy databases can be accessed automatically via Biopython’s <B>Bio.ExPASy</B> module. The function <B>.get_sprot_raw</B> will find a target protein by its ID. </P>
<P> We can obtain data from an entry by using the <B>SwissProt</B> module. The <B>read()</B> function will handle one SwissProt record and <B>parse</B> will allow you to read multiple records at a time. </P>

<P>Let's get the data for the B5ZC00 protein:</P>
<CODE> 
from Bio import ExPASy

from Bio import SwissProt

handle = ExPASy.get_sprot_raw('B5ZC00') #you can give several IDs separated by commas

record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins

</CODE>

<P>We now can check the list of attributes for the obtained Swiss-Prot record:</P>

<CODE>dir(record)</CODE>

<P>To see the list of references to other databases, we can check the <B>.cross_references</B> attribute of our record:</P>
<CODE>record.cross_refereces[0]</CODE>
