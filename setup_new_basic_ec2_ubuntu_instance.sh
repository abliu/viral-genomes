#!/bin/bash
# comment parts depending on their necessity!
# install conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source .bashrc
# install git-lfs
wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.2/git-lfs-linux-amd64-v2.7.2.tar.gz
tar -xvzf git-lfs-linux-amd64-v2.7.2.tar.gz
sudo ./install.sh
# go through installation instructions; can change to silent mode!
sudo mkdir /working
cd /working
# full permissions
sudo chmod -R 777 .
mkdir home
cd home
git clone https://github.com/abliu/viral-genomes
cd viral-genomes
# https://wiki.rc.hms.harvard.edu/display/O2/Conda+on+O2 if on O2

# module load conda2/4.2.13

conda create -n viral-genomes
conda activate viral-genomes
conda install -y jupyter
# conda install -y pandas
# conda install -y scikit-learn=0.20.2
# pip install scikit-optimize # for Bayes optimization
conda install -y biopython
pip install slackclient  # for notifications when long jobs are done
# pip install memory-profiler
git config --global user.name "Andrew Bo Liu"
git config --global user.email "andrew.bo.liu@gmail.com"
cd data
gunzip -k nucl_gb.accession2taxid.gz
sudo apt install unzip
unzip U-RVDBv15.1.fasta.zip
