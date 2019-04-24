#!/bin/bash

#SBATCH --exclude=c5003 
#SBATCH --job-name=python_auto
#SBATCH --output=python_auto.log 
#SBATCH --error=python_auto.log 
#SBATCH -p general
#SBATCH -N 1 
#SBATCH -n 20 
#SBATCH --mem=100000 

source activate rmg_env

python $1.py


