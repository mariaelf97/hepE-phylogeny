# hepE-phylogeny

## Summary of the steps to create the phylogenetic tree
1. Download sequences listed in [Smith et al. publication](https://www.microbiologyresearch.org/content/journal/jgv/10.1099/jgv.0.001435#).
This ended in 587 sequences including the reference (M73218) and NC_015521.1 Cutthroat trout virus as an outgroup.
2. Rename IDs in the multifasta file to include only the accession ID (causes error in iqtree)
3. Remove reference sequence from the multifasta file
4. Perform MSA using MAFFT and M73218 as reference sequence.
5. Mask sites 6355-6985 and 8344 to 8347 included in the publication due to hyper variability.
6. Create a maximum likelihood tree with MF mode using iqtree.
7. Visualize tree (ggtree) while using NC_015521.1 and remove the outgroup.
8. Generate metadata information using from sequences' gbk file.