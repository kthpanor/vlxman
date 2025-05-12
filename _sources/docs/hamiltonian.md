# Hamiltonian

## Effective-core potentials

This feature is under implementation.

## Static electric fields

A term can be added in the Hamiltonian to describe the coupling of the molecular system and a time-independent (static), homogeneous, electric field. The value specified oin the input file are for the x,y,z direction respectively given in a.u.

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
[Download](../input_files/pna-field.inp) or [Python script](../input_files/pna-field.py) type of input file  to perfom a scf calculation under the presence of a static electric field for the p-nitroaniline.

```{image} ../images/pna.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```
