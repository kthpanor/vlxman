# Optical activity and dichroism

## Rotatory strengths

The strength of an ECD band is given by the anisotropy of the decadic molar extinction coefficient {cite}`Norman2018`

$$
\Delta\epsilon\left(\omega\right) =
\epsilon_+\left(\omega\right)-\epsilon_-\left(\omega\right) =
\frac{16\pi^2{\mathcal N}\omega}{3\times
  1000\ln\left(10\right)\left(4\pi\epsilon_0\right)\hbar
  c^2}\sum_{n}f(\omega;\omega_{n0},\gamma)\, R_{n0} 
$$

where the rotatory strength $R_{n0}$ defined as

$$
R_{n0} =
\lim_{\omega\rightarrow\omega_{n0}}
\left(\omega_{n0}-\omega\right)
\Im\langle \langle \hat{\mu}_\alpha
;\hat{m}_\alpha\rangle \rangle_\omega
= \langle 0 | \hat{\mu}_\alpha | n \rangle
\langle n | \hat{m}_\alpha | 0\rangle
$$

Note that there is an implied Einstein summation of the repeated tensor indices in the equations above as to refer to a situation of an isotropic sample.

```
@jobs
task: response
@end

@method settings
basis: def2-SVPD
dft: yes
xcfun: b3lyp
@end

@response
property: ecd
nstates: 20
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end

```

## Anisotropy of extinction coefficient

The anisotropy of the decadic molar extinction coefficient can be determined directly from the complex polarization propagator evaluated for mixed electric- and magnetic-dipole operators {cite}`Norman2018, Jiem2007`

$$
\Delta\epsilon(\omega) =
\epsilon_+(\omega) - \epsilon_-(\omega) =
\frac{
	16\pi^2{\mathcal N}\omega
}{
	3 \times 1000 \ln(10)
	(4\pi\epsilon_0)\hbar c^2
}
\Re 
\langle \langle \hat{\mu}_\alpha
;\hat{m}_\alpha\rangle \rangle_\omega^\gamma
$$

The linear response function is here complex and calculated with a damping term, $\gamma$, associated with the inverse finite lifetime of the excited states. The default program setting for this parameter is 0.124 eV (or 1000 cm$^{-1}$).

```
@jobs
task: response
@end

@method settings
basis: def2-SVPD
dft: yes
xcfun: b3lyp
@end

@response
property: ecd (cpp)
frequencies: 0.05-0.15 (0.0025)
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

## Exciton coupling model

VeloxChem implements the exciton coupling model to determine circular dichroism spectra.

```
@jobs
task: exciton
@end

@method settings
xcfun: b3lyp
basis: cc-pvdz
@end

@exciton
fragments: 40
atoms_per_fragment: 55
nstates: 5
ct_nocc: 0
ct_nvir: 0
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
XYZ coordinates for 40 x 55 atoms
...
@end
```

