# Environment

(sec:cpcm)=
## CPCM

to be added

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
