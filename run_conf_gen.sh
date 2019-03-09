#!/bin/sh

#SBATCH --exclude=c5003 
#SBATCH --job-name=conf_run
#SBATCH --output=run_conf_gen.slurm.log 
#SBATCH --error=run_conf_gen.slurm.log 
#SBATCH -p general
#SBATCH -N 1 
#SBATCH -n 20 
#SBATCH --mem=100000 

source activate rmg_env

python conf_gen.py
