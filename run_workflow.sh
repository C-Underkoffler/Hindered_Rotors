#!/bin/sh

#SBATCH --exclude=c5003 
#SBATCH --job-name=run
#SBATCH --output=run_workflow.slurm.log 
#SBATCH --error=run_workflow.slurm.log 
#SBATCH -p general
#SBATCH -N 1 
#SBATCH -n 20 
#SBATCH --mem=100000 

source activate rmg_env

python workflow.py
