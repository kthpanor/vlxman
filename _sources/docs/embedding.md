# Environment

(sec:cpcm)=
## CPCM
The conductor-like polarizable continuum model, CPCM is implemented in VeloxChem and can be activated in the scf driver. Here is an example for calculation in water.

**Python script**
```
import veloxchem as vlx

mol_xyz_string = """
...
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.solvation_model = 'cpcm'
scf_drv.cpcm_epsilon = 78.39  # Water
scf_drv.filename = 'mol-cpcm'

scf_results = scf_drv.compute(mol, basis)

```
Download a [Python script](../input_files/ethanol-cpcm.py) type of input file to perfom a scf calculation under the presence of a static electric field for the p-nitroaniline.

**Text file**
```
@jobs
task: scf
@end

@method settings
basis: def2-svp
xcfun: b3lyp
solvation model: cpcm
cpcm epsilon : 78.39
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end

```
Download a [text format](../input_files/ethanol-cpcm.inp) type of input file to perfom a scf calculation under the presence of a static electric field for the p-nitroaniline.

(sec:pe)=
## Polarizable embedding

An SCF calculation with a polarizable environment is performed in VeloxChem with an input file of the form

```
@jobs
task: scf
@end

@method settings
basis: aug-cc-pvdz
potfile: pe.pot
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

together with a potential file `pe.pot` using Isotropic LOPROP parameters.

```
@environment
units: angstrom
xyz:
O   -0.9957202   0.0160415   1.2422556  water  1
H   -1.4542703  -0.5669741   1.8472817  water  1
H   -0.9377950  -0.4817912   0.4267562  water  1
O   -0.2432343  -1.0198566  -1.1953808  water  2
H    0.4367536  -0.3759433  -0.9973297  water  2
H   -0.5031835  -0.8251492  -2.0957959  water  2
@end

@charges
O  -0.67444408  water
H   0.33722206  water
H   0.33722206  water
@end

@polarizabilities
O       5.73935090    0.00000000    0.00000000    5.73935090    0.00000000    5.73935090  water
H       2.30839051    0.00000000    0.00000000    2.30839051    0.00000000    2.30839051  water
H       2.30839051    0.00000000    0.00000000    2.30839051    0.00000000    2.30839051  water
@end
```
