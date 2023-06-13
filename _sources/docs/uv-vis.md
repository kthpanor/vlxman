# UV/vis absorption/emission

## Generalized eigenvalue equation

The standard method to calculate UV/vis absorption and emission spectra is to solve the generalized eigenvalue equation {cite}`Norman2018`.

In the case of SCF theory, it is commonly referred to as the time-dependent density functional theory or Hartree–Fock (TDDFT or TDHF) approach. TDHF is also known as the Random Phase Approximation (RPA). 

If electron de-excitations are ignored in the formation of the electronic Hessian, then one arrives at the Tamm–[Dancoff](https://en.wikipedia.org/wiki/Sidney_Dancoff) approximation and which can be invoked with a keyword in the input file.

VeloxChem implements a reduced-space Davidson algorithm to solve the equation for the *N* lowest eigenvalues (bottom-up). Based on these eigenvalues, or transition frequencies, and the associated transition moments, the dimensionless [oscillator strengths](https://en.wikipedia.org/wiki/Oscillator_strength#:~:text=In%20spectroscopy%2C%20oscillator%20strength%20is,of%20an%20atom%20or%20molecule.) are calculated according to

$$
  f_{n0} = \frac{2 m_\mathrm{e} \omega_{n0}}{3\hbar e^2}
  \sum_{\alpha = x,y,z}
  |\langle 0 | \hat{\mu}_\alpha | n \rangle |^2
$$

With oscillator strengths and transition frequencies, the [linear absorption cross section](https://en.wikipedia.org/wiki/Absorption_cross_section) can be determined from the expression {cite}`Norman2018`

$$
\sigma(\omega) =
\frac{2\pi^2 e^2 \omega}{(4\pi\varepsilon_0) m_\mathrm{e} c} 
\sum_{n > 0}
f(\omega; \omega_{n0}, \gamma) 
\frac{
f_{n0}
}{ 
\omega_{n0}
}
$$

where $f$ is the [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution).

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
! tamm_dancoff: yes
nstates: 3
@end

@molecule
charge: 0
multiplicity: 1
xyz:  
...
@end
```

## Complex polarization propagator approach

The linear absorption cross section can be determined directly from the imaginary part of the [polarizability](https://en.wikipedia.org/wiki/Polarizability) {cite}`Norman2018`

$$
\sigma(\omega) =
\frac{\omega}{\epsilon_0 c}
\mathrm{Im}\left\{
\overline{\alpha}(-\omega;\omega)
\right\}
$$

where 

$$
\overline{\alpha} =
\frac{1}{3}
\big(
\alpha_{xx} + 
\alpha_{yy} + 
\alpha_{zz}
\big)
$$

and 

$$
\alpha_{\alpha\beta}(-\omega;\omega) =
- \langle \langle 
\hat{\mu}_\alpha ; \hat{\mu}_\beta
\rangle \rangle^\gamma_\omega
$$

The polarizability is complex and calculated with a damping term, $\hbar \gamma$, associated with the inverse finite lifetime of the excited states. The default program setting for this parameter is 0.124 eV (or 0.004556 a.u.).

The resulting values for $\sigma(\omega)$ are presented in atomic units and can be converted to the SI unit of m$^2$ by multiplying with a factor of $a_0^2$.


The arbitrary frequency region is specified in the input file together with a requested frequency resolution.

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
damping: 0.0045563  ! this is the default value
@end

@molecule
charge: 0
multiplicity: 1
xyz:  
...
@end 
```
