import os, sys, re, collections, random

fname = 'hg38.fa.align'
state = 'ended'
seq_name = ''
current_seq = collections.defaultdict(list)
with open(fname) as f:
	for n, li in enumerate(f):
		#print(li.rstrip('\n'))

		if not (n % 100000):
			print('{}/222840365={}%'.format(n, 100* n/222840365))

		#if n > 10000000:
		#	break

		if re.search('\AMatrix', li) is not None:
			state = 'ended'
			#print('ended')
			#print('Previous sequence:', current_seq)
			if len(current_seq[seq_name]) > 1:
				if len(current_seq[seq_name][0]) > len(current_seq[seq_name][1]):
					current_seq[seq_name] = [current_seq[seq_name][0]]
				else:
					current_seq[seq_name] = [current_seq[seq_name][1]]
#				current_seq[seq_name] = list(set(current_seq[seq_name]))
#				if len(current_seq[seq_name]) > 1:
					#print("More than one sequence for {}".format(seq_name))
					#print(current_seq[seq_name])
			continue

		if (state == 'ended') and (re.search('\A\d+', li) is not None):
			state = 'reading'
			#print('head')
			m = re.search('([\w\(\)]+#[^ ]+)', li, re.IGNORECASE)
			if m is not None:
				#print(m.group(1))
				current_seq[m.group(1)].append('')
				seq_name = m.group(1)
			continue

		if (state == 'reading'):
			#print(' ' * 27 + li[27:])
			if '#' in li:
				seq = li[27:].split(' ')[0].replace(' ', '').replace('-', '')
				#print('>>', seq)
				current_seq[seq_name][-1] += seq
			#print(seq)

with open('compressed.fa', 'w') as fh:
	for name, list_of_seqs in current_seq.items():
		for n, seq in enumerate(list_of_seqs):
			if len(seq) > 10:
				fh.write('>{}_{}\n{}\n'.format(n, name, seq))


