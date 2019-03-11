#!/bin/bash

##SBATCH --job-name=handrun
#SBATCH --output=VMPUAIZSESMILD-UHFFFAOYSA-N_GeoFreq.log
## number of nodes
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --partition=general
#SBATCH --mem=120000

# run gaussian, with the desired input file
g16 VMPUAIZSESMILD-UHFFFAOYSA-N_GeoFreq.com


