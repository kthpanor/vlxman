# Hamiltonian

## Effective-core potentials

This feature is under implementation.

## Static electric fields

A term can be added in the Hamiltonian to describe the coupling of the molecular system and a time-independent (static), homogeneous, electric field.

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
units: au
xyz:
O   0.0   0.0   0.0
H   0.0   1.4   1.1
H   0.0  -1.4   1.1
@end
```
