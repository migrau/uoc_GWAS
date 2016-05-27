#!/usr/bin/python

#script to run impute2 along a whole chromosome automatically.
##how to call
#python impute2.py -m "reference/hapmap3_r2_b36/genetic_map_chr17_combined_b36.txt" -l "reference/hapmap3_r2_b36/hapmap3_r2_b36_chr17.legend" -p "reference/hapmap3_r2_b36/hapmap3_r2_b36_chr17.haps" -g "data/F1/genotypes_chr17_ASW_r27_nr.b36_fwd_noMissMask20.gen" -o "results/F1/intervals/mask20/Masked20_impute"

import sys, getopt
import os
import subprocess


def main(argv):
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hm:p:l:g:o:",["mapfile=","haplotypefile=","legendfile=","genotypefile=","outputfile="])
    except getopt.GetoptError:
        print 'test.py -m <mapfile> -p <haplotypefile> -l <legendfile> -g <genotypefile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -m <mapfile> -p <haplotypefile> -l <legendfile> -g <genotypefile> -o <outputfile>'
            sys.exit()
        elif opt in ("-m", "--mapfile"):
            mapfile = arg
        elif opt in ("-p","--haplotypefile"):
            haplotypefile = arg
        elif opt in ("-l", "--legendfile"):
            legendfile = arg
        elif opt in ("-g", "--genotypefile"):
            genotypefile = arg
        elif opt in ("-o", "--outputfile"):
            outputfile = arg    
    with open(legendfile) as f:
        max = (list(f)[-1])
        max = max[:-1].split(" ")[1]
    #set the interval for 5x10^6. From 1 to max position from the legend file        
    for i in range (1,int(max)-5000000,5000000):
        #call to impute2
        cmd="impute2 -m "+mapfile+" -h "+haplotypefile+" -l "+legendfile+" -g "+genotypefile+" -int "+str(i)+" "+str(i+int(5e6))+" -Ne 20000 -o "+outputfile+str(i)
        os.system(cmd)
    #Option to merge all the results, disabled by now
    #cmd="mv "+outputfile+"*_* info"
    #os.system(cmd)
    #cmd="cat "+outputfile+"* > "+outputfile+"_chunkAll"
    #os.system(cmd)
if __name__ == "__main__":
    main(sys.argv[1:])
