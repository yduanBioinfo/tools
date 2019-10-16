#!/usr/bin/env python3

import sys
from collections import OrderedDict as Ordic

# array, splited line.
def count_array(array, count_data):
    for w in array:
        count = count_data.get(w,0)
        count_data[w] = count+1
    return count_data

def output(data,outfile,sep,ratio=True):
    total = sum(data.values())
    for key, val in data.items():
        outfile.write(key+sep+str(val))
        if ratio:
            outfile.write(sep+str(val/total))
        outfile.write("\n")

def count_file(infile,outfile,sep,outsep="\t"):
    data = Ordic()
    for line in infile:
        la = line.strip().split(sep)
        data = count_array(la, data)
    output(data,outfile,outsep)
    
def main(argv):

    import argparse

    parser = argparse.ArgumentParser(description="Count words")
    parser.add_argument('infile',nargs='?',help="input file, \"-\" for stdin ")
    parser.add_argument('-o','--outfile',nargs='?',help="output file",default=sys.stdout,type=argparse.FileType('w'))
    parser.add_argument('-s1','--sep1',nargs='?',default="\t",help="input file sep")
    parser.add_argument('-s2','--sep2',nargs='?',default="\t",help="output file sep")
    args = parser.parse_args(argv[1:])

    sep1=args.sep1
    sep2=args.sep2
    
    if args.infile == '-':
        infile=sys.stdin
    else:
        infile=open(args.infile)
    count_file(infile,args.outfile,sep1,sep2)

if __name__ == '__main__':
    import sys
    main(sys.argv)
