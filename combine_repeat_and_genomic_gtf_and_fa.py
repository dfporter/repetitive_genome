"""Combine genomic and repeat fastas/gtfs into one.
 This program mostly exists to document how this was done, and in case something more
 complicated needs to be added later.

Usage:
    combine_repeat_and_genomic_gtf_and_fa.py [--repeats_fa=<fa>] [--repeats_gtf=<gtf>] [--genome_gtf=<ggtf>] [--genome_fa=<gfa>]

Options:
    -h --help            show this message and exit.
    --genome_fa=<str>   Genomic fasta file. [default: /opt/genome/ensembl_release94_GRCh38/GRCh38.primary_assembly.genome.fa]
    --genome_gtf=FILE   Genomic [default: /opt/genome/ensembl_release94_GRCh38/gencode.v29.primary_assembly.annotation.exons_cds_only.gtf]
    --repeats_gtf=FILE   Repeats [default: repeats.gtf]
    --repeats_fa=STR   Repeats fasta file [default: repeats.fa]
"""

import re, os, sys, collections, subprocess
from docopt import docopt
args = docopt(__doc__)
print(args)


#print("USAGE: <genomic gtf> <repeats gtf>")

for label in ['--genome_fa', '--genome_gtf', '--repeats_fa', '--repeats_gtf']:
    if not os.path.exists(args[label]):
        raise IOError("Could not find file {}".format(args[label]))

with open('combined.fa', 'w') as outfile:
    with open(args['--genome_fa']) as fh:
        for li in fh:
            outfile.write(li)
    with open(args['--repeats_fa']) as fh:
        for li in fh:
            outfile.write(li)

with open('combined.gtf', 'w') as outfile:
    with open(args['--genome_gtf']) as fh:
        for li in fh:
            outfile.write(li)
    with open(args['--repeats_gtf']) as fh:
        for li in fh:
            outfile.write(li)

