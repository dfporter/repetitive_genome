import re

concat = ''
chr_len = 0
gft_info = []
simple_repeats = 0
with open('compressed.fa') as f:
	while True:
		try:
			name = next(f).rstrip('\n')
			seq = next(f).rstrip('\n')
			if len(seq) < 20:
				continue

			if re.search('n#Simple_repeat', name):
				simple_repeats += 1
				continue

			concat += 'N' * 50 + seq
			chr_len += len(seq) + 50
			gft_info.append({
				'Gene': name, 'Start': chr_len - len(seq), 'End': chr_len
				})
#			break
		except:
			print("Failed to advance. Finished file.")
			break

print("Skipped {} simple repeats".format(simple_repeats))
print(chr_len)
with open('single_chr.fa', 'w') as f:
	f.write('>repeats\n')
	for _index in range(0, chr_len, 79):
		if _index+79>chr_len:
			f.write(concat[_index:] + '\n')
		else:
			f.write(concat[_index:_index+79] + '\n')

with open('repeats.gtf', 'w') as f:
	for li in gft_info:
		f.write(
			'repeats\trepeats\texon\t{}\t{}\t.\t+\t.\tgene_id "{}"; transcript_id "{}"; biotype "{}";\n'.format(
				li['Start'], li['End'], li['Gene'], li['Gene'], li['Gene'].split('#')[1]))


