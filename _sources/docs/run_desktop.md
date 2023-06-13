# Running on a desktop

## In a Jupyter notebook

```
import veloxchem as vlx

water_xyz_string = """
3
water
O  0.00000  0.00000  0.00000
H  0.00000  0.00000  1.79524
H  1.69319  0.00000 -0.59904
"""

molecule = vlx.Molecule.read_xyz_string(water_xyz_string)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scfdrv = vlx.ScfRestrictedDriver()
scfdrv.conv_thresh = 1.0e-6
scfdrv.xcfun = 'b3lyp'
scf_results = scfdrv.compute(molecule, basis)
```

A comprehensive presenation of how to interact and run the VeloxChem program in a Jupyter notebook is provided in the [eChem book](https://kthpanor.github.io/echem).

## Using an input file

An input file driven VeloxChem calculation can be started on the command line as follows:

```
$ vlx water.inp [water.out]
```

If the optional output file name is omitted, the output will be sent to standard output.

The input file (here assumed to be named `water.inp`) consists of multiple groups marked with `@group name` and `@end`. For example, the following input file has three groups: `jobs`, `method settings`, and `molecule`. In the `molecule` group, the default unit for Cartesian coordinates is Angstrom.

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
O  0.00000  0.00000  0.00000
H  0.00000  0.00000  1.79524
H  1.69319  0.00000 -0.59904
@end
```
