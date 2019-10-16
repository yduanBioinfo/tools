#!/usr/bin/env python

import sys,string

def readGenome(fa):

	try:fa=open(fa)
	except:pass
	data = {}
	
	#currseq = ''
	currseq = []
	for eachline in fa:
		eachline = eachline.strip()
		if not eachline:
			continue
		if eachline[0] == ">":
			if currseq:
				currseq = "".join(currseq)
				data[currchr] = currseq
				currseq = []
			currchr = eachline.lstrip(">")
		else:
			currseq.append(eachline)
		#last chr
		currseq = "".join(currseq)
                data[currchr] = currseq
	fa.close()
	return data

def getRC(seq):

	'''
	get reverse compliment sequence
	'''

	intab = 'AaTtGgCc'
	outtab = 'TtAaCcGg'
	transtab = string.maketrans(intab,outtab)
	return seq[::-1].translate(transtab)

if len(sys.argv) !=4:

        print "fasta.extract.py <position.list> <genome> <sequence.fasta>"
else:
	genome = readGenome(sys.argv[2])
	out=open(sys.argv[3],"w")
        with open (sys.argv[1]) as position:
                for eachline in position:
                        sp=eachline.strip().split('\t')
                        Chr=sp[1]
                        start=int(sp[2])-1
                        end=int(sp[3])
			out.write(">%s\n"%sp[0])
			sequence = genome.get(Chr)
			sequence = sequence[start:end] if sequence else ""
			out.write(sequence+"\n")
