#!/usr/bin/python

#script to remove missing genotypes from a genotypes file from hapMap. Missing genotypes typed as NN
##how to call
##python remove_missing.py -i data/genotypes_chr17_ASW_r27_nr.b36_fwd.txt -o data/genotypes_chr17_ASW_r27_nr.b36_fwd_NoMiss.txt

import sys, getopt
import os

def main(argv):
    res=""
    contaSi=contaNo=0
    inputfile = outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    with open(inputfile, 'r') as f: 
        for line in f: 
            if "NN" not in line.split(" "):
                res+=line
                contaSi+=1
            else:
                contaNo+=1
    print "%d of %d SNPs have been deleted because they contain some missing values.\nPercentage of SNPs with missing calls: %.2f"%(contaNo,contaSi+contaNo,contaNo*100/(contaSi+contaNo)) 
    print "Number of SNPs without missing calls: %d."%(contaSi)
    f = open(outputfile,'w')
    f.write(res)
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
