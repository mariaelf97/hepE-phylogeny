# hepE-phylogeny

## Summary of the Steps to Create the Phylogenetic Tree

1. **Download Sequences**:
   - Obtain sequences listed in the [Smith et al. publication](https://www.microbiologyresearch.org/content/journal/jgv/10.1099/jgv.0.001435#).
   - This includes a total of 588 sequences, with the reference sequence (M73218) and NC_015521.1 (Cutthroat trout virus) as an outgroup.

2. **Rename IDs**:
   - Modify the IDs in the multifasta file to include only the accession ID. This is necessary to avoid errors in IQ-TREE.

3. **Remove Reference Sequence**:
   - Exclude the reference sequence from the multifasta file.

4. **Perform Multiple Sequence Alignment (MSA)**:
   - Use **MAFFT** for alignment, with M73218 as the reference sequence.

5. **Mask Hypervariable Sites**:
   - Mask sites 6355-6985 and 8344-8347 as specified in the publication due to hypervariability.

6. **Create Maximum Likelihood Tree**:
   - Generate the phylogenetic tree using **IQ-TREE** with the **MF** mode.

7. **Visualize the Tree**:
   - Use **ggtree** to visualize the tree. Initially include NC_015521.1 as an outgroup and remove it later if necessary.

8. **Generate Metadata**:
   - Extract metadata information from the sequences' GenBank files (`.gbk`).

### Phylogenetic Tree

[![Tree](https://github.com/mariaelf97/hepE-phylogeny/blob/main/tree/tree.png)