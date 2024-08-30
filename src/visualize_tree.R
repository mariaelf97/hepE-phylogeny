library(treeio)
library(ggtree)
library(data.table)
library(tidyverse)

# read tree file
tree <- read.tree("mnt/hepE_seqs/mafft_outgroup_hypervariable_removed_sequences.fasta.treefile")
# Read isolate name and genotype information
tip_labels <- as.data.frame(t(fread("mnt/hepE_seqs/isolates.txt",header = FALSE)))
tip_labels <- tip_labels %>% separate(V1, into = c("genotype","label"))
tree_nodes <- as.data.frame(tree$tip.label)
# to be able to change tip names
tree_nodes <- tree_nodes%>%separate(`tree$tip.label`, into=c("V2","V3"), remove = FALSE)
joined_labels <- tip_labels %>% inner_join(tree_nodes, by = c("label"="V2"))
# create genotype, isolate name value 
joined_labels$label_genotype <- paste(joined_labels$genotype,joined_labels$`tree$tip.label`,sep = "_")
# root tree on the outgroup
rooted_tree <- root(tree, outgroup = "NC_015521.1", edgelabel = TRUE)
# remove the outgroup
reduced_tree <- drop.tip(rooted_tree, "NC_015521.1")
# get MRCA node number to highlight clades
id <- as.character(1:8)
parent_nodes <- sapply(id, function(x) ape::getMRCA(tree_renamed, tree_renamed$tip.label[str_detect(tree_renamed$tip.label, x)]))
parent_nodes_unzipped <- data.frame(do.call(rbind,parent_nodes))
colnames(parent_nodes_unzipped)[1]<-"node"
parent_nodes_unzipped$type <- rownames(parent_nodes_unzipped)
ggtree(tree_renamed, layout="daylight", branch.length = 'none') + 
  geom_hilight(data=parent_nodes_unzipped, aes(node=node, fill=type))
# rename tips to color tips
tree_renamed <- rename_taxa(reduced_tree, joined_labels,`tree$tip.label`,label_genotype) 
p <- ggtree(tree_renamed, right = TRUE)
p %<+% (joined_labels %>% select(label_genotype,genotype)) +
  geom_tippoint(aes(color=genotype), size=2)+
  scale_color_manual(values=c("#800080", "#FFFF00", "#0000FF", "#FFA500", "#FF0000", "#008000", "#FFC0CB", "#00FF00", "#008080", "#FF7F50", "#4B0082", "#FFD700", "#DC143C", "#98FF98", "#000080", "#FFDAB9",
                              "#EE82EE", "#7FFF00", "#40E0D0", "#800000", "#E6E6FA", "#8B4513", "#50C878", "#FF4500", "#00FFFF", "#FF00FF", "#DDA0DD", "#FFF44F", "#2F4F4F", "#E0115F", "#800020", "#F0E68C",
                              "#B0C4DE", "#CD7F32", "#FF6347", "#808000", "#4169E1", "#FD5E53", "#87CEEB", "#A0522D", "#36454F", "#FFFFF0", "#BC8F8F", "#4682B4", "#FF1493", "#556B2F", "#40E0D0", "#B7410E"))

meta <- fread("mnt/git_repos/hepE-phylogeny/metadata/metadata.csv")
meta %>% inner_join(joined_labels,by=c("accession"="tree$tip.label")) %>% 
  select(strain,sample_date,host,accession,country,genotype) %>%
  write_csv("Downloads/metadata.csv")
