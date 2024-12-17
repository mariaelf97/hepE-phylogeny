python src/pull_fasta.py metadata/samples.txt metadata/sequences.fasta 
python src/pull_genbank.py metadata/samples.txt metadata/samples.gbk metadata/reference.gb 
python src/extract_metadata.py metadata/samples.gbk metadata/genotype.tsv metadata/metadata.tsv
mafft --6merpair --keeplength --addfragments metadata/sequences.fasta metadata/reference.fasta > metadata/aligned.fasta
python src/change_hypervariable_regions.py metadata/aligned.fasta metadata/aligned_modified.fasta 6355 6985
python src/change_hypervariable_regions.py metadata/aligned.fasta metadata/aligned_modified.fasta 8344 8347
cd tree/
iqtree2 -s ../metadata/aligned_modified.fasta -m MF