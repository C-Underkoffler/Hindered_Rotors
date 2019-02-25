#!/bin/bash

#SBATCH --job-name=AutoTor
#SBATCH --output=$1.log

## number of nodes
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --partition=general
#SBATCH --mem=120000

## set the gaussian scratch directory to a fast drive
## note that /tmp/ may be even faster than /gss_gpfs_scratch/
## export GAUSS_SCRDIR=/scratch/$USER/gaussian_scratch
## make the directory if it doesn't exist already
## mkdir -p $GAUSS_SCRDIR

# run gaussian, with the desired input file
g16 $1.com

