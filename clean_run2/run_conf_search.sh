#!/bin/sh

#SBATCH --exclude=c5003 
#SBATCH --job-name=conf_search
#SBATCH --output=conf_search.slurm.log 
#SBATCH --error=conf_search.slurm.log 
#SBATCH -p general
#SBATCH -N 1 
#SBATCH -n 20 
#SBATCH --mem=100000 

source activate rmg_env

python conf_search.py
