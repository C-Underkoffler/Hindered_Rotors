#!/bin/sh

#SBATCH --exclude=c5003 
#SBATCH --job-name=sharma_conf
#SBATCH --output=log_v2_conf_sharma.slurm.log 
#SBATCH --error=log_v2_conf_sharma.slurm.log 
#SBATCH -p general
#SBATCH -N 1 
#SBATCH -n 20 
#SBATCH --mem=100000 

source activate rmg_env

python sharma_conf.py
