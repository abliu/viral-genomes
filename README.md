# viral-genomes

- `analyze_viral_genome_windows_size.ipynb` (main analysis) calculates the number of unique k-mers of DNA in the Reference Viral Database's (RVDB) set of viral genomes.
- `setup_new_basic_ec2_ubuntu_instance.sh` sets up the programming environment on a fresh AWS EC2 Ubuntu instance in which to run `analyze_viral_genome_windows_size.ipynb`.
- `full_scratchwork_analyze_viral_genome_windows_size.ipynb` performs secondary analyses such as checking that the number of unique k-mers of amino acids in RVDB-prot approximately matches the answer from the main analysis and comparing the size of the k-mer count from the main analysis with that estimated by adding sequence lengths. (Warning: this file is not so readable!)
- `data` contains `U-RVDBv15.1.fasta`, the file of RVDB sequences that is needed for the main analysis, as well as other files for secondary analyses. Cloning the github repo will not download these files since they are too large. Download `U-RVDBv15.1.fasta` at https://hive.biochemistry.gwu.edu/rvdb.
