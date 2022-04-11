from Bio import SeqIO
import re

# This code extracts accession numbers from the Reference Viral Database
# (https://rvdb.dbi.udel.edu/), which stores viral sequences aggregated from
# multiple virus nucleic acid databases in fasta files (the latest as of this
# writing is C-RVDBv23.0.fasta). Accession numbers are shown in these files and
# when we use SeqIO to extract the id from each sequence. A typical id extracted
# by SeqIO is as follows:
#
# acc|GENBANK|MH171300.1|Marine
#
# The accession number of interest is MH171300.1 (and the database it comes from,
# GENBANK).

# First, I found that when each id is split into fields by pipes ("|"), the third
# field reliably looks like an accession number with 1-2 letters followed by 5-6
# digits and possibly an underscore and a period followed by a digit at the end.
# I also checked there were no duplicates.
seqs = SeqIO.parse("/Users/abl19/Downloads/C-RVDBv23.0.fasta", "fasta")
strict_accession_regex = re.compile('^[A-Z]{1,2}_?[0-9]{5,6}(\.[0-9])?$')
bad_regex_count = 0
dbs = set()
accessions = set()
for seq in seqs:
  id_fields = seq.id.split("|")
  if strict_accession_regex.match(id_fields[2]) is None:
    bad_regex_count += 1
  dbs.add(id_fields[1])
  accessions.add(id_fields[2])

bad_regex_count # outputs 0, which means all ids satisfied the regex
len(dbs) # outputs 4, so there are 4 source databases
len(accessions) # outputs 873234, same as the number of sequences (no duplicates)

# Then I extracted the actual accession numbers and their source databases.
seqs = SeqIO.parse("/Users/abl19/Downloads/C-RVDBv23.0.fasta", "fasta")
with open('virus_accession_numbers_C-RVDBv23.0.txt', 'w') as accession_out_file:
  for seq in seqs:
    id_fields = seq.id.split("|")
    accession_out_file.write(f"{id_fields[1]}|{id_fields[2]}\n")
