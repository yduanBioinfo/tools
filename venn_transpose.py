#!/usr/bin/env python

import sys

'''
combine files for venn plot.
[Usage] venn_transpose.py file1 file2 file3 > outfile

eg.
file1:
aaa
bbb
ccc
ddd

file2:
mmm
nnnn
bbbbb

file3:
ppp
o
iii
uuu

outfile:
aaa	bbb	ccc	ddd
mmm	nnnn	bbbbb
ppp	o	iii	uuu
'''

def trs(names,outfile,with_header,sep):
    #names: infile names

    files=map(open,names)
    for i in range(len(files)):
        if not with_header:
            #if infile without header,
            #add infile name as header.
            outfile.write(names[i]+sep)
        outfile.write(sep.join(files[i].read().split("\n")))
        outfile.write("\n")

def main(argv):

    import argparse

    parser = argparse.ArgumentParser(description="Combine and transpose files for venn plotting.")
    parser.add_argument('files',nargs='+',help="infiles")
    parser.add_argument('-o','--outfile',nargs='?',help="output file",default=sys.stdout,type=argparse.FileType('w'))
    parser.add_argument('-s','--sep',nargs='?',default="\t")
    parser.add_argument('-n','--has_header',action='store_true',default=False,help="If files has header,set this option.")
    args = parser.parse_args(argv[1:])

    #with_header = False
    #sep="\t"

#    outfile=sys.stdout
    trs(args.files,args.outfile,args.has_header,args.sep)

if __name__ == '__main__':

    import sys
    main(sys.argv)
