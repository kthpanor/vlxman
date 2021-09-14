# Running with input files

## Structure of input file

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


The VeloxChem input file consists of multiple groups marked with `@group name` and `@end`. For example, the following input file has three groups: `jobs`, `method settings`, and `molecule`.

## Launching the calculation

```
export OMP_NUM_THREADS=6
mpirun -n 2 python3 -m veloxchem water.inp water.out
```

This launches a VeloxChem calculation on 2 MPI ranks, each with 6 OpenMP threads. The recommended way to run VeloxChem is to run 1 MPI rank per allocated cluster node and 1 OpenMP thread per CPU core on a single node.
