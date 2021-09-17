# Running on a cluster

A SLURM job submission script for VeloxChem can take something of the following form:

```
#!/bin/bash

#SBATCH --time=10:00:00

#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32

# setup the environemnt
module load buildtool-easybuild/3.5.3-nsc17d8ce4
module load intel/2018a
module load Python/3.6.4-nsc2-intel-2018a-eb

# activate veloxchem
source $HOME/software/VeloxChemMP/venv/bin/activate

# number of threads should match the SLURM specification
export OMP_NUM_THREADS=32

# start the calculation
job=water
mpirun python3 -m veloxchem ${job}.inp ${job}.out

# end of script
```

This script will start a job with 4 MPI ranks, each with 32 OpenMP threads. It is recommended to start one MPI rank per node, and on each node, one OpenMP thread per core.

The input file (here assumed to be named `water.inp`) consists of multiple groups marked with `@group name` and `@end`. For example, the following input file has three groups: `jobs`, `method settings`, and `molecule`.

```
@jobs
task: scf
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@molecule
charge: 0
multiplicity: 1
units: au
xyz:
O   0.0   0.0   0.0
H   0.0   1.4   1.1
H   0.0  -1.4   1.1
@end
```
