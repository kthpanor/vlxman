# Reference states

A detailed list of keyword can be found in the [SCF optimization section](./keywords.ipynb#scf-optimization) of the [Input file keywords page](./keywords.ipynb).

By default, Hartree-Fock is used if not specified otherwise. To use DFT, several functionals are available and should be specified in the ```@method settings``` section by using the keyword ```xcfun```. See the [Exchange-correlation functionnals](./functionals.ipynb) page for a complete list of functionnals available.

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
...
@end
```
[Download](../input_files/biphenyl-scf.inp) an input file to perfom a restricted closed-shell calculation for the biphenyl molecule.

```{image} ../images/biphenyl.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Restricted open-shell

```
@jobs
task: roscf
@end

@method settings
basis: def2-svp
xcfun: b3lyp
@end

@molecule
charge: 1
multiplicity: 2
xyz:
...
@end
```
[Download](../input_files/tempo-roscf.inp) the input file to perfom a restricted open-shell calculation for the tempo molecule.

```{image} ../images/tempo.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Unrestricted open-shell

```
@jobs
task: uscf
@end

@method settings
basis: def2-svp
xcfun: PBE0
@end

@molecule
charge: 1
multiplicity: 2
xyz:
...
@end
```
[Download](../input_files/tritylradical-uscf.inp) the input file to perfom a unrestricted open-shell calculation for the triphenylmethyl radical molecule (also called trityl radical).

```{image} ../images/trityl.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```
