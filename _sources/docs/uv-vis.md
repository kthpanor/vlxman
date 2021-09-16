# UV/vis absorption/emission

## Generalized eigenvalue equation

The standard method to calculate UV/vis absorption and emission spectra is to solve the generalized eigenvalue equation.

In the case of SCF theory, it is commonly referred to as the time-dependent density functional theory or Hartree–Fock (TDDFT or TDHF) approach. TDHF is also known as the Random Phase Approximation (RPA). 

VeloxChem implements a reduced-space Davidson algorithm to solve the equation for the *N* lowest eigenvalues (bottom-up). 

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
nstates: 3
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

## Complex polarization propagator approach

Absorption spectra are also available from the imaginary part of the complex polarizability, in which case an arbitrary frequency region is specified together with a requested frequency resolution.

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
# frequency region (and resolution)
frequencies: 0-0.25 (0.05)
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
