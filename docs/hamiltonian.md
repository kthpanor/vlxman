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
xyz:
O  0.00000  0.00000  0.00000
H  0.00000  0.00000  1.79524
H  1.69319  0.00000 -0.59904
@end
```
