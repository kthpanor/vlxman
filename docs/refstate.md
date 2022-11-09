# Reference states

## Restricted closed-shell

```
@jobs
task: scf
@end

@method settings
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

## Restricted open-shell

```
@jobs
task: roscf
@end

@method settings
basis: def2-svp
@end

@molecule
charge: 1
multiplicity: 2
units: au
xyz:
O   0.0   0.0   0.0
H   0.0   1.4   1.1
H   0.0  -1.4   1.1
@end
```

## Unrestricted open-shell

```
@jobs
task: uscf
@end

@method settings
basis: def2-svp
@end

@molecule
charge: 1
multiplicity: 2
units: au
xyz:
O   0.0   0.0   0.0
H   0.0   1.4   1.1
H   0.0  -1.4   1.1
@end
```
