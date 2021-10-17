#!/bin/sh
#SBATCH -J gpu-test-%J
#SBATCH -N 1
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem=8000
#SBATCH --gres=gpu:1
#SBATCH -o stdout.%J
#SBATCH -e stderr.%J

hostname
nvidia-smi
