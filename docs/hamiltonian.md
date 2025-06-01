# Hamiltonian

## Effective-core potentials

ECP integrals are under implementation.

## Static electric fields

A term can be added in the Hamiltonian to describe the coupling of the molecular system and a time-independent (static), homogeneous, electric field. The vectorial electric-field strength is specified in atomic units.

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
scf_drv.electric_field = [0.01, 0.0, 0.0]  # [x, y, z] components
scf_results = scf_drv.compute(molecule, basis)
```
Download a {download}`Python script <../input_files/pna-field.py>` type of input file to perform an SCF calculation for *para*-nitroaniline in the presence of a static electric field.

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

Download a {download}`text format <../input_files/pna-field.inp>` type of input file to perform an SCF calculation for *para*-nitroaniline in the presence of a static electric field.

```{image} ../images/pna.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```
