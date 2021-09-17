# Running on a desktop

## In a Jupyter notebook

```
import veloxchem as vlx

molecule_string = """
    O 0 0 0
    H 0 0 1.795239827225189
    H 1.693194615993441 0 -0.599043184453037"""

molecule = vlx.Molecule.read_str(molecule_string, units='angstrom')

basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_settings = {'conv_thresh': 1.0e-6}
method_settings = {'xcfun': 'b3lyp', 'grid_level': 4}

scfdrv = vlx.ScfRestrictedDriver()
scfdrv.update_settings(scf_settings, method_settings)
scfdrv.compute(molecule, basis)
```

A comprehensive presenation of how to interact and run the VeloxChem program in a Jupyter notebook is provided in the [eChem book](https://kthpanor.github.io/echem).

## Using an input file

An input file driven VeloxChem calculation can be started on the command line as follows:

```
export OMP_NUM_THREADS=8
mpirun -n 1 python3 -m veloxchem water.inp water.out
```

This launches a calculation on 1 MPI rank with 8 OpenMP threads. It is recommended to launch no more than one thread per available core on your desktop CPU.

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


