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

where the rotatory strength $R_{n0}$ is defined as

\begin{align*}
R_{n0} & =
\lim_{\omega\rightarrow\omega_{n0}}
\left(\omega_{n0}-\omega\right)
\Im\langle \langle \hat{\mu}_\alpha
;\hat{m}_\alpha\rangle \rangle_\omega
= \langle 0 | \hat{\mu}_\alpha | n \rangle
\langle n | \hat{m}_\alpha | 0\rangle 
\\ & =
\frac{i}{m_\mathrm{e} \omega_{n0}}
\langle 0 | \hat{p}_\alpha | n \rangle
\langle n | \hat{m}_\alpha | 0\rangle
\end{align*}

In VeloxChem, the rotatory strength is evaluated in the velocity gauge as given in the final expression.

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
\Delta\epsilon(\omega) = \epsilon_+(\omega) - \epsilon_-(\omega) = \frac{288\times10^{-30}\pi^2 \cal{N} a_0^4}{100}\frac{\pi}{4.5\mathrm{ln}(10)1000}
\, \beta  \tilde{\nu}^2 
$$

where 

$$
\beta = -\frac{1}{3 \omega} (G_{xx} + G_{yy} + G_{zz})
$$

and 

$$
G_{\alpha\alpha} = \Re\langle\langle\hat{\mu}_\alpha;\hat{m}_\alpha
\rangle\rangle_\omega = 
\frac{e}{\omega m_e}
\Im 
\langle\langle\hat{p}_\alpha;
\hat{m}_\alpha
\rangle\rangle_\omega
$$

The mixed electric–magnetic dipole tensor, $G$, is evaluated in the velocity gauge as given in the final expression. Furthermore, it is complex and calculated with a damping term, $\gamma$, associated with the inverse finite lifetime of the excited states. The default program setting for this parameter is 0.124 eV (or 0.004556 a.u.).

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
damping: 0.0045563  # this is the default value
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

