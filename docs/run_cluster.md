# Running on a cluster

On a supercomputer cluster, it is a common practice to submit a job script to a batch queue system such as e.g. [SLURM](https://en.wikipedia.org/wiki/Slurm_Workload_Manager). 

## Job script

In the job script, one specifies the amount of resources to be used for the calculation as well as a line launching the application across the allocated nodes using e.g. `srun` or `mpirun`. In this scenario, VeloxChem is run with an input file in the form of either a Python script or a text file. In the example job script given below, both alternatives are provided and you activate the one that you prefer using.

```bash
#!/bin/bash

#SBATCH -A project_name
#SBATCH -p partition_name
#SBATCH -J job_name
#SBATCH -t 01:00:00

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

module load veloxchem/1.0

export OMP_NUM_THREADS=16
export OMP_PLACES=cores
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

# using a Python script type of input file
srun python myjob.py > myjob.out
# using a text type of input file
#srun vlx myjob.inp myjob.out

# end of job script
```

This script will start a job on two nodes with eight MPI ranks per node (one per [NUMA](https://en.wikipedia.org/wiki/Non-uniform_memory_access) domain), each with 16 OpenMP threads.

## Input file

**Python script**

An example Python script type of input file named `myjob.py` in the job script above and and which is running an SCF optimization takes the following form.

```
import veloxchem as vlx

xyz_string = """
3
water
O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
"""

molecule = vlx.Molecule.read_xyz_string(xyz_string)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_drv.filename = "vlx_results_hdf5"

scf_results = scfdrv.compute(molecule, basis)
```

The results of the calculation are stored in an [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) file with a user specified name. This file can be directly read and analyzed with VIAMD.

**Text file**

The same SCF calculation can be performed with use of an input file in text format named `myjob.inp` in the in the job script above. Such an input file consists of multiple groups marked with `@group name` and `@end`, see the listing of [text file input keywords](sec:text-file-keywords).

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
xyz:
O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
@end
```
