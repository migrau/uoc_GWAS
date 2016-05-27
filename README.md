#Genome Wide Association Studies Project for UOC - UB

Code used during the realization of the project GWAS from the UOC-UB

The scripts are:

* _remove_missing.py_: Delete missing genotypes from hapMap file.

    $python remove_missing.py -i data/genotypes_chr17_ASW_r27_nr.b36_fwd.txt -o out.txt


* _density.py_: Filter by density a genotypes file from hapMap to perfom simulations.

    $python density.py -i data/genotypes_chr17_ASW_r27_nr.b36_fwd_NoMiss.txt -d 100 -o out


* _mask.py_: Mask a X percentage of genotypes from hapMap to perfom simulations.

    $python mask.py -i data/genotypes_chr17_ASW_r27_nr.b36_fwd_NoMissF100.txt -p 5 -o out.txt


* _impute2.py_: Run IMPUTE2 analysis automatically for the whole chromosome with intervals of 5 million of bases.

    $python impute2.py -m "reference/hapmap3_r2_b36/genetic_map_chr17_combined_b36.txt" -l "reference/hapmap3_r2_b36/hapmap3_r2_b36_chr17.legend" -p "reference/hapmap3_r2_b36/hapmap3_r2_b36_chr17.haps" -g "data/F1/genotypes_chr17_ASW_r27_nr.b36_fwd_noMissMask20.gen" -o out.impute


**possible improvements:

beagle.py

mach.py

plink.py

....

