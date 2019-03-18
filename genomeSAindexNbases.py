# wc -c repeats.fa
# = 4355824

import numpy as np
_chars = 4355824
_chars = 1307272
print("GenomeLength={}. log2(GenomeLength)/2 -1 = ".format(_chars))
print(np.log2(_chars)/2 -1)
print("Use the minimum of [14, log2(GenomeLength)/2 -1]")
