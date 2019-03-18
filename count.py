import os, sys, re, HTSeq, collections, pandas

ga = HTSeq.GenomicArrayOfSets('auto', stranded=False)

samfile = sys.argv[1]

with open('repeats.gtf') as f:
	for li in f:
		if li[0] == '#':
			continue
		s = li.split('\t')
		iv = HTSeq.GenomicInterval(s[0], int(s[3]), int(s[4]), '+')
		m = re.search('gene_id "([^"]+)";', s[-1])
		#print(m.group(1))
		ga[iv] += m.group(1)
#CTGATC_CAGrand=TCTTGTT-M01339:756:000000000-C39LC:1:1101:26698:12508	99	repeats_chrom	3623391	42	20M	=	3623391	-20	TCCGGTGAGCTCTCGCTGGC	GGGGGGDCFFFFGGGGGGEF	AS:i:0	XN:i:0	XM:i:0	XO:i:0	XG:i:0	NM:i:0	MD:Z:20	YS:i:0	YT:Z:CP

counts = collections.defaultdict(int)
with open(samfile) as f:
	for li in f:
		if li[0] == '@':
			continue
		s = li.split('\t')
		loc = int(s[3])

		genes = ga[HTSeq.GenomicPosition('repeats', loc, '+')]
		if len(genes):
			counts[list(genes)[0]] += 1

df = pandas.DataFrame.from_dict(counts, orient='index')
df['Biotype'] = [x.split('#')[1] for x in df.index]
_fix = {'RNA': '7SK'}
df['Biotype'] = [_fix.get(x, x) for x in df.Biotype]
print(df.sort_values(by=[0]))
print(df[0].sum())
print(df.groupby("Biotype").sum())

