#!/bin/sh

#SBATCH --exclude=c5003 
#SBATCH --job-name=sharma_workflow
#SBATCH --output=log_sharma_workflow.slurm.log 
#SBATCH --error=log_sharma_workflow.slurm.log 
#SBATCH -p general
#SBATCH -N 1 
#SBATCH -n 20 
#SBATCH --mem=100000 

source activate rmg_env

python sharma_workflow.py
