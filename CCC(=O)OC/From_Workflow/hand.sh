#!/bin/bash

#SBATCH --job-name=hand
#SBATCH --output=RJUFJBKOKNCXHH-UHFFFAOYSA-N_72by10.0_tor23_a1.log

## number of nodes
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --partition=general
#SBATCH --mem=120000

## export GAUSS_SCRDIR=/scratch/$USER/gaussian_scratch
## make the directory if it doesn't exist already
## mkdir -p $GAUSS_SCRDIR

## run gaussian, with the desired input file
g16 RJUFJBKOKNCXHH-UHFFFAOYSA-N_72by10.0_tor23_a1.com

