import argparse
from Bio import AlignIO, SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def modify_positions_in_fasta(input_file, output_file, start, end):
    # Read the input FASTA file
    records = list(AlignIO.read(input_file, "fasta"))
    
    # Modify each sequence
    for record in records:
        replacement = "N" * (end - start + 1)
        modified_seq = str(record.seq[:start - 1]) + replacement + str(record.seq[end:])
        record.seq = Seq(modified_seq)
    
    # Write the modified sequences to the output file
    SeqIO.write(records, output_file, "fasta")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Modify positions in a FASTA file by replacing a range with Ns.')
    parser.add_argument('input_file', type=str, help='Path to the input FASTA file')
    parser.add_argument('output_file', type=str, help='Path to the output FASTA file')
    parser.add_argument('start', type=int, help='Start position (1-based index)')
    parser.add_argument('end', type=int, help='End position (1-based index)')

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to modify the positions in the FASTA file
    modify_positions_in_fasta(args.input_file, args.output_file, args.start, args.end)

if __name__ == '__main__':
    main()
