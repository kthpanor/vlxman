# Input files
In this section, we provide a series of input files for different task. 

## SCF calculation
This example is for a restricted closed-shell , use ```task: uscf``` for unrestricted open-shell and ```task: roscf``` for restricted open-shell 

```
@jobs
task: scf
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


## Geometry optimization
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

## UV-VIS (ECD) absorption with Linear Response
```
@jobs
task: response
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@response
property: absorption
nstates: 5
nto: yes
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

## UV-VIS absorption with Complex Polarization Propagator
```
@jobs
task: response
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@response
property: absorption (cpp)
! frequency region (and resolution)
frequencies: 0.0-0.15 (0.0025)
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

## ECD absorption with Complex Polarization Propagator
```
@jobs
task: response
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@response
property: ecd (cpp)
! frequency region (and resolution)
frequencies: 0.0-0.15 (0.0025)
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

## Vibrational spectroscopy
```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_ir: yes
do_raman: yes
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                
@end

```

## Resonance Raman
```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_ir: yes
do_raman: yes
do_resonance_raman: yes
frequencies: 0.05-0.25 (0.05)
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                  
@end

```



```

```



```

```