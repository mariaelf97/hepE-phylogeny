from Bio import SeqIO
import pandas as pd

# Function to extract geolocation and sample ID from a GenBank record
def extract_metadata(record):
    # Initialize variables
    sample_id = record.id
    geolocation = None
    strain = None
    host = None

    # Access the date in the LOCUS line
    date = record.annotations.get("date")

    # Iterate through features in the GenBank record
    for feature in record.features:
        if "geo_loc_name" in feature.qualifiers:
            geolocation = "; ".join(feature.qualifiers.get("geo_loc_name"))
        if "strain" in feature.qualifiers:
            strain = "; ".join(feature.qualifiers.get("strain"))
        if "host" in feature.qualifiers:
            host = "; ".join(feature.qualifiers.get("host"))

    return strain, date, host, sample_id, geolocation



# Function to parse a multi-sequence GenBank file and return a DataFrame
def parse_genbank_file(file_path):
    data = []
    
    # Parse the GenBank file
    for record in SeqIO.parse(file_path, "genbank"):
        strain, sample_date, host, sample_ID, geolocation = extract_geolocation_and_id(record)
        data.append({"strain": strain, "sample_date": sample_date,
                     "host":host,"accession":sample_ID, "country": geolocation})
    
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(data)
    
    return df

# Specify the path to your GenBank file
file_path = "/home/mahmadi/hepE_seqs/sequence.gb"

# Parse the GenBank file and get the DataFrame
df = parse_genbank_file(file_path)

# Display the DataFrame
# Optionally, save the DataFrame to a CSV file
df.to_csv("geolocations.csv", index=False)
