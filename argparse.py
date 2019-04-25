import sys, getopt

def parse_args(argv):
	sequence = ''
	k = 0
	d = 0
	
	try:
		opts, args = getopt.getopt(argv, "s:k:d:", ["sequence=", "kmer-length=", "hamming-distance="])
	except getopt.GetoptError:
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-s' or opt == '--sequence':
			sequence = arg
		if opt == '-k' or opt == '--kmer-length':
			k = int(arg)
		if opt == '-d' or opt == '--hamming-distance':
			d = int(arg)
	return sequence, k, d
