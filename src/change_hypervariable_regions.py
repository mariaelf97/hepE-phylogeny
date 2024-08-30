from Bio import AlignIO, SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
def modify_positions_in_fasta(input_file, output_file, start, end):

    records = list(AlignIO.read(input_file,"fasta"))
    
    # Modify each sequence
    for record in records:
        replacement = "N" * (end-start +1)
        modified_seq = str(record.seq[:start-1]) + str(replacement) + str(record.seq[end:])
        record.seq = Seq(modified_seq)
    SeqIO.write(records, output_file, "fasta")
        
 
# Usage
input_file = "/home/mahmadi/hepE_seqs/mafft_outgroup_hypervariable_removed_sequences.fasta"  # Replace with your input file path
output_file = "/home/mahmadi/hepE_seqs/mafft_outgroup_hypervariable_removed_sequences.fasta"  # Replace with your desired output file path
start_position = 6355 # 0-based index, 10th nucleotide
end_position = 6985  # 0-based index, 20th nucleotide

modify_positions_in_fasta(input_file, output_file, start_position, end_position)

