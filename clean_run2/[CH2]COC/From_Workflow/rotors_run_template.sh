#!/bin/bash

#SBATCH --job-name=AutoScript
#SBATCH --output=$1.log

## number of nodes
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --partition=general
#SBATCH --mem=120000

## export GAUSS_SCRDIR=/scratch/$USER/gaussian_scratch
## make the directory if it doesn't exist already
## mkdir -p $GAUSS_SCRDIR

## run gaussian, with the desired input file
g16 $1.com

