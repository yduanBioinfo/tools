#!/usr/bin/env python

import sys

def read_file(infile,sep="\t"):
    data = []
    for line in infile:
        line_array=line.strip().split(sep)
        data.append(line_array)
    return data

def output(data,outfile,sep="\t",hold="NA"):
    # Get how much lines
    row_length = max(map(len,data))
    line_length = len(data)
    for i in range(row_length):
        outfile.write(sep.join(map(lambda x:x[i],data))+"\n")

def tr(infile,outfile,sep1="\t",sep2="\t"):
    data = read_file(infile,sep1)
    output(data,outfile,sep2)

def main(argv):

    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Transpose file.")
    parser.add_argument('infile',nargs='?',help="File to be transposed, \"-\" for stdin")
    parser.add_argument('-o','--outfile',nargs='?',help="output file, default: stdout",default=sys.stdout,type=argparse.FileType('w'))
    parser.add_argument('-s1','--sep1',nargs='?',default="\t",help="Sep of infile")
    parser.add_argument('-s2','--sep2',nargs='?',default="\t",help="Sep of outfile")
    args = parser.parse_args(argv[1:])

    if args.infile == "-":
        infile = sys.stdin
    else:
        infile = open(args.infile)

    tr(infile,args.outfile,args.sep1,args.sep2)

if __name__ == '__main__':

    import sys
    main(sys.argv)
