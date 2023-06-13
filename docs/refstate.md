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
xyz:
O  0.00000  0.00000  0.00000
H  0.00000  0.00000  1.79524
H  1.69319  0.00000 -0.59904
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
xyz:
O  0.00000  0.00000  0.00000
H  0.00000  0.00000  1.79524
H  1.69319  0.00000 -0.59904
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
xyz:
O  0.00000  0.00000  0.00000
H  0.00000  0.00000  1.79524
H  1.69319  0.00000 -0.59904
@end
```
