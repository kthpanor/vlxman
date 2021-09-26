# UV/vis absorption/emission

## Generalized eigenvalue equation

The standard method to calculate UV/vis absorption and emission spectra is to solve the generalized eigenvalue equation {cite}`Norman2018`.

In the case of SCF theory, it is commonly referred to as the time-dependent density functional theory or Hartree–Fock (TDDFT or TDHF) approach. TDHF is also known as the Random Phase Approximation (RPA). 

If electron de-excitations are ignored in the formation of the electronic Hessian, then one arrives at the Tamm–Dancoff approximation and which can be invoked with a keyword in the input file.

VeloxChem implements a reduced-space Davidson algorithm to solve the equation for the *N* lowest eigenvalues (bottom-up). Based on these eigenvalues, or transition frequencies, and the associated transition moments, the dimensionless oscillator strengths are calculated according to

$$
  f_{n0} = \frac{2 m_\mathrm{e} \omega_{n0}}{3\hbar e^2}
  \sum_{\alpha = x,y,z}
  |\langle 0 | \hat{\mu}_\alpha | n \rangle |^2
  = \frac{2 m_\mathrm{e} \omega_{n0}}{3\hbar e^2}\boldsymbol{\mu}_{0n}\cdot\boldsymbol{\mu}_{n0}
$$


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
# tamm_dancoff: yes
nstates: 3
@end

@molecule
charge: 0
multiplicity: 1
units: au
xyz:  
...
@end
```

## Complex polarization propagator approach

Absorption spectra are also available from the imaginary part of the isotropic complex polarizability {cite}`Norman2018`

$$
\sigma(\omega) =
\frac{\omega}{\epsilon_0 c}
\mathrm{Im}\left\{
\overline{\alpha}(-\omega;\omega)
\right\}
$$

In this case an arbitrary frequency region is specified together with a requested frequency resolution.

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
...
@end 
```
