# Repetitive elements in the human genome compressed into an artificial chromosome

hg38.fa.align.gz was downloaded from:

http://www.repeatmasker.org/genomes/hg38/RepeatMasker-rm405-db20140131/hg38.fa.align.gz

This was unzipped to hg38.fa.align and converted to compressed.fa using parse_repeats.py

```bash
python parse_repeats.py
```

hg38.fa.align contains entries like the following two:

```ascii
261 26.78 17.19 4.69 chr1 11485 11676 (248944746) C L1ME3G_3end#LINE/L1 (510) 414 194 m_b1s551i0 3

  chr1               11485 CATATGC---TGTTTGGTCTC---AGTAGACTCCTAAATATGGGATTCCT 11528
                              i   ---    ---    ---i     iv  v i vi   i   v  
C L1ME3G_3end#L        414 CATGTGCGAGTGTT---TCTCTAGGGTAGATACCGAGAAGTGGAATTGCT 368

  chr1               11529 GGGTTTAAAAGTAAAAAATAAATATGTTTAATTTGTGA-----ACTG--- 11570
                               iv? ii  -----  ivii  -     v  v i -----    ---
C L1ME3G_3end#L        367 GGGTCANAGGGT-----ATGCGCAT-TTTAAATTTTAATAGATACTGCCA 324

  chr1               11571 -ATTACCATCAGAA----TTGTACTGTTCTGTA-TCCCACCAGCAATGTC 11614
                           -   i  v  vi  ----i     iiv i ii -           i   v
C L1ME3G_3end#L        323 AATTGCCCTCCAAAGTGGCTGTACCAATTTACACTCCCACCAGCAGTGTA 274

  chr1               11615 TAGGAATGCCTGTTTCTCCACA--------AA------GTGTT-T---AC 11646
                            ii  i i  i     i     --------  ------i i  - ---  
C L1ME3G_3end#L        273 TGAGAGTACCCGTTTCCCCACACCCTCGCCAACACTTGATATTATCAAAC 224

  chr1               11647 TTTTGGATTTTTGCCAGTCTAACAGGTGAA 11676
                               ii          i   i ii      
C L1ME3G_3end#L        223 TTTTAAATTTTTGCCAATCTGATGGGTGAA 194

Matrix = 20p45g.matrix
Kimura (with divCpGMod) = 32.68
Transitions / transversions = 3.00 (36/12)
Gap_init rate = 0.10 (20 / 191), avg. gap size = 2.35 (47 / 20)

535 20.48 15.74 2.92 chr1 11505 11675 (248944747) C L1MC5a_3end#LINE/L1 (2382) 395 199 m_b1s551i1 3

  chr1               11505 TAGACTCCTAAATATGGGATTCCTGGGTTTAAAAGTAAAAAATAAATATG 11554
                               i     i vi       v      iv  ii  ---    iv     
C L1MC5a_3end#L        395 TAGATTCCTAGAAGTGGGATTGCTGGGTCAAAGGGT---AAATGCATATG 349

  chr1               11555 TTTAA-TTTGTGA---ACTG----ATTA----CCATCAGAATTGTACTGT 11592
                           --   -    iv --- i  ----   v----    vi ii      ii 
C L1MC5a_3end#L        348 --TAATTTTGCTAGATATTGCCAAATTCCCCTCCATAGGGGTTGTACCAT 301

  chr1               11593 TCTGTA-TCCCACCAGCAATGTCTAGGAATGCCTGTTTCTCC-------- 11633
                            i  i -               v ii  i          i  --------
C L1MC5a_3end#L        300 TTTGCATTCCCACCAGCAATGTATGAGAGTGCCTGTTTCCCCACAGCCTC 251

  chr1               11634 ----ACAAAGTGTTT------ACTTTTGGATTTTTGCCAGTCTAACAGGT 11673
                           ----   i   i v ------                  i   i i    
C L1MC5a_3end#L        250 GCCAACAGAGTATGTTGTCAAACTTTTGGATTTTTGCCAATCTGATAGGT 201

  chr1               11674 GA 11675
                             
C L1MC5a_3end#L        200 GA 199

Matrix = 20p45g.matrix
Kimura (with divCpGMod) = 24.83
Transitions / transversions = 2.78 (25/9)
Gap_init rate = 0.08 (13 / 170), avg. gap size = 2.77 (36 / 13)

```

From each of these entries, parse_repeats.py takes the reference sequence 
 (like L1MC5a_3end#LINE/L1 )
  and removes any '-'. The name is taken from the head of the entry (L1MC5a_3end#LINE/L1)
  and the reference sequence is assumed to be the one with an '#' in it. If no '#' is
  found in the subsequent lines, it gets ignored (should replace this potential bug).

These lines are subsequently output to compressed.fa, with this format:

```ascii
>0_(CGTCCTC)n#Simple_repeat
CGTCCTCCGTCCTCCGTCCTCCGTCCTCCGTCCTCCGTCCTCCGTCCTCC
>0_(TACAAATG)n#Simple_repeat
TACAAATGTACAAATGTACAAATGTACAAATGTACAAATGTACAAA
>0_(TATAGAAT)n#Simple_repeat
TATAGAATTATAGAATTATAGAATTATAGAATTATAGAATTATAGAATTATAGA
>0_(AGGAAG)n#Simple_repeat
AGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAGGAAGAG
```

This file is then fed to concat_repeats.py to produce repeats.fa and repeats.gtf.

```bash
python concat_repeats.py
```

Which look like this:
```ascii
head repetitive_genome/repeats.*

==> repetitive_genome/repeats.fa <==
>repeats
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCAGTGTTTCCCAAACTTCAGTCATTCGCG
TACCACCTTCACGATTTTTGCCATATCCGCGTACCACCTGTACTATTATTTACTTAATATTTTTCTTTAAATCGACTCA
CTTTTTAAAACTTAAATACCTACTTTAGCCTCATCCTAAGCAATAATATCCGTGAAATCACGGGTTTGATGTGCTAGTT
ATATTTTTTTCTAATACACATTAAAATAAATACATAACTATTAAAATAAAAAATGTTCGTCCGTGTACCACCTAAAATC
ATCTCGCGTACCACCAGTGGTACGCGTACCACACTTTGGGAAACACTGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNACTCCCGCTGAAATCTGGGCGTGGTTGGAGAGTAGCTGGGACAGACAGGAGAGTCCCTGA
GGGCTGGGGGTGAAGACATGAGAGAGACTGGGGAGTAACTCAGTGAAATTGGTGAGTTTGGTGGTGATTCCTGGGTGCC
TGGAACTGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTGTGGGGGTTCAGTCAGGCTG
GTGGGAAAAATTTTAAGATGAAGTTATAGGAAATAGACACAAACCTTCTTGGAAGGCCGGAAGGTTTTGCAAAAGCTTC

==> repetitive_genome/repeats.gtf <==
repeats	repeats	exon	50	364	.	+	.	gene_id ">0_MER113A#DNA/hAT-Charlie"; transcript_id ">0_MER113A#DNA/hAT-Charlie"; biotype "DNA/hAT-Charlie";
repeats	repeats	exon	414	561	.	+	.	gene_id ">0_ACRO1_#Satellite/acromeric"; transcript_id ">0_ACRO1_#Satellite/acromeric"; biotype "Satellite/acromeric";
repeats	repeats	exon	611	1137	.	+	.	gene_id ">0_LTR22B1#LTR/ERVK"; transcript_id ">0_LTR22B1#LTR/ERVK"; biotype "LTR/ERVK";
repeats	repeats	exon	1187	1625	.	+	.	gene_id ">0_LTR16#LTR/ERVL"; transcript_id ">0_LTR16#LTR/ERVL"; biotype "LTR/ERVL";
repeats	repeats	exon	1675	1761	.	+	.	gene_id ">0_HSAT5_#Satellite"; transcript_id ">0_HSAT5_#Satellite"; biotype "Satellite";
repeats	repeats	exon	1811	2786	.	+	.	gene_id ">0_5_Mam#DNA/hAT-Tag1"; transcript_id ">0_5_Mam#DNA/hAT-Tag1"; biotype "DNA/hAT-Tag1";
repeats	repeats	exon	2836	3266	.	+	.	gene_id ">0_UCON17#Unknown"; transcript_id ">0_UCON17#Unknown"; biotype "Unknown";
repeats	repeats	exon	3316	3988	.	+	.	gene_id ">0_MLT1M#LTR/ERVL-MaLR"; transcript_id ">0_MLT1M#LTR/ERVL-MaLR"; biotype "LTR/ERVL-MaLR";
repeats	repeats	exon	4038	4842	.	+	.	gene_id ">0_LTR1E#LTR/ERV1"; transcript_id ">0_LTR1E#LTR/ERV1"; biotype "LTR/ERV1";
repeats	repeats	exon	4892	7638	.	+	.	gene_id ">0_2#DNA/hAT-Ac"; transcript_id ">0_2#DNA/hAT-Ac"; biotype "DNA/hAT-Ac";

```

STAR is subsequently run to generate an index:

```bash
mkdir star_repeats
STAR --genomeSAindexNbases 5 --limitGenomeGenerateRAM 100000000000 --runThreadN 10 --runMode genomeGenerate --genomeDir star_repeats --genomeFastaFiles repeats.fa --sjdbGTFfile repeats.gtf --sjdbOverhang 75
# --genomeSAindexNbases 5 is well below the default 14. It speeds up the mapping to small genomes.
```


