# Hamiltonian

## Effective-core potentials

This feature is under implementation.

## Static electric fields

A term can be added in the Hamiltonian to describe the coupling of the molecular system and a time-independent (static), homogeneous, electric field. The value specified oin the input file are for the x,y,z direction respectively given in a.u.

**Python script**
```
import veloxchem as vlx

mol_xyz_string = """
...
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-field'
scf_drv.electric_field = [0.01, 0.0, 0.0]
scf_results = scf_drv.compute(molecule, basis)
```
Download a [Python script](../input_files/pna-field.py) type of input file to perfom a scf calculation under the presence of a static electric field for the p-nitroaniline.

**Text file**
```
@jobs
task: scf
@end

@method settings
basis: def2-svp
electric field: 0, 0.001, -0.002
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```
Download a [text format](../input_files/pna-field.inp) type of input file to perfom a scf calculation under the presence of a static electric field for the p-nitroaniline.
```{image} ../images/pna.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```
