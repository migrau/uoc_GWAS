#!/usr/bin/python


##script to filter by density of SNPs from a genotypes file from hapMap
##how to call
#python density.py -i data/genotypes_chr17_ASW_r27_nr.b36_fwd_NoMiss.txt -d 100 -o data/genotypes_chr17_ASW_r27_nr.b36_fwd_NoMissF100.txt


import sys, getopt
import os

def main(argv):
    res=""
    conta=contaTotal=0
    inputfile=outputfile=inputdensity= ''
    try:
        opts, args = getopt.getopt(argv,"hi:d:o:",["ifile=","--density=","ofile="])
    except getopt.GetoptError:
        print 'density.py -i <inputfile> -d <density> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'density.py -i <inputfile> -d <density> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-d","--density"):
            inputdensity = int(arg)
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    with open(inputfile, 'r') as f: 
        #only select a line for X group of lines.
        for line in f:
            if contaTotal==0:
                res+=line
                contaTotal=1
                continue 
            if conta==inputdensity:
                res+=line
                conta=1
            else:
                conta+=1
            contaTotal+=1           
    #Print statistics
    print "Retained 1/%d SNPs."%(inputdensity) 
    print "%d SNPs retained of a total of %d"%(contaTotal/inputdensity, contaTotal)
    f = open(outputfile,'w')
    f.write(res)
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
