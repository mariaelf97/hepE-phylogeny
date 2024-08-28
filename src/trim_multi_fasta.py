from Bio import SeqIO

def trim_fasta_ids(input_fasta, output_fasta):
    # Read the input FASTA file
    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        for record in SeqIO.parse(infile, "fasta"):
            # Modify the ID to keep only the first word before the space
            record.id = record.id.split()[0]
            # Ensure the description is updated accordingly
            record.description = record.id
            # Write the modified record to the output file
            SeqIO.write(record, outfile, "fasta")

# Usage example
input_fasta = "/home/mahmadi/hepE_seqs/sequences.fasta"
output_fasta = "/home/mahmadi/hepE_seqs/organized_sequences.fasta"
trim_fasta_ids(input_fasta, output_fasta)