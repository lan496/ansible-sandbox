#!/bin/sh
#SBATCH -J cpu-test-%J
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:0
#SBATCH --cpus-per-task=1
#SBATCH --mem=8000
#SBATCH -o stdout.%J
#SBATCH -e stderr.%J

hostname
sleep 1
