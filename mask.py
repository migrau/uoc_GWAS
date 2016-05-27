#!/usr/bin/python

#script to mask a specific percentage of snps from a genotypes file from hapMap
##how to call
#python mask.py -i data/genotypes_chr17_ASW_r27_nr.b36_fwd_NoMissF100.txt -p 5 -o data/genotypes_chr17_ASW_r27_nr.b36_fwd_NoMissF100Masked.txt

from random import randint
import sys, getopt
import os

def main(argv):
    res=""
    contaTotal=0
    inputfile=outputfile = ''
    lineValues=[]
    try:
        opts, args = getopt.getopt(argv,"hi:p:o:",["ifile=","--percentage=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -p <percentage> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -p <percentage> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-p","--percentage"):
            inputpercen = float(arg)
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    with open(inputfile, 'r') as f: 
        for line in f:
            if contaTotal==0:
                ##if the head has always the same structure, we can count the number of samples easily 
                samples=len(line.split(" "))-11
                num_lines = (sum(1 for line in open(inputfile)))-1
                randomN_per_line=(samples*num_lines*inputpercen/100)/num_lines
                res+=line
                contaTotal=1
                continue
            lineValues=line.split(" ")
            randomList=[randint(11,samples) for p in range(0,int(randomN_per_line))]
            for i in range(11,len(lineValues)):
                if i in randomList:
                    lineValues[i]="NN"
                    contaTotal+=1
            res+=" ".join(lineValues)
    print "Expected masked SNPs %d."%(randomN_per_line*num_lines) 
    print "Masked SNPs %d (%d%%)"%(contaTotal-1,inputpercen)
    f = open(outputfile,'w')
    f.write(res)
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
