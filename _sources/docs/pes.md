# Potential energy surfaces

## Ground state optimization

A detailed list of keyword can be found in the [Optimization driver section](./keywords.ipynb#optimization-driver) of the [Input file keywords page](./keywords.ipynb). Dispersion can be activated in the ```@method settings``` section by using the keyword ```dispersion```. 

```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
dispersion: yes # use dft-d4 correction
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```
[Download](../input_files/bithio-S0-opt.inp) an input file to perfom a optimization for the bithiophene molecule at the B3LYP+D4/def2-svp level of theory.

```{image} ../images/bithio-S0-opt.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Excited state optimization

To optimize an excited state, you need to use the task optimize and to specify which state you want to optimize with the ```state_deriv_index:``` keyword in the ```@gradient``` section.

```
@jobs
task: optimize
@end

@response
property: absorption
nstates: 2
@end

@gradient
state_deriv_index: 1
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

[Download](../input_files/bithio-S1-opt.inp) an input file to perfom a optimization of the first excited state of bithiophene molecule at the B3LYP/def2-svp level of theory.

```{image} ../images/bithio-S1-opt.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Constrained optimization
 
### Freeze coordinate

### Set coordinate

### Scan coordinate



