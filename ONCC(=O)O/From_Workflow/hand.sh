#!/bin/bash

##SBATCH --job-name=handrun
#SBATCH --output=NPWGWQRXHVJJRD-UHFFFAOYSA-N_72by10.0_tor34_a2.log
## number of nodes
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --partition=general
#SBATCH --mem=120000

# run gaussian, with the desired input file
g16 NPWGWQRXHVJJRD-UHFFFAOYSA-N_72by10.0_tor34_a2.com


