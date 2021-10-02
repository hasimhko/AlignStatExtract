# AlignStatExtract
Python scripts that extract alignment statistics from the output text files of HISAT2 and Samtools, and organize them into CSV files. One of these scripts is intended to be used in my MSc project which requires alingment of RNA-seq reads from whole honey bees (<i>Apis mellifera anatolica</i>) to 14 viral genomes as means to quantify viral infections in honey bees. That script will therefore be used extract the total number of RNA-seq reads aligned to each of the 14 viral genomes for each sample from the output of samtools stats used on BAM files. The number of reads aligned to viral genomes will be organized in a table (exported as a CSV file), where sample IDs will be row names and names of viruses will be column names. 

The other script will be used to extract all alignment statistics of RNA-seq reads aligned to the <i>Apis mellifera genome</i> from the HISAT2's output for each sample, and organize all of the statistics into a table (exported as a CSV file) where sample IDs will be row names and statistics types will be column names.

