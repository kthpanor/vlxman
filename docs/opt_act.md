(sec:ecd)=
# Optical activity and dichroism

## Rotatory strengths

The strength of an ECD band is given by the anisotropy of the [decadic molar extinction coefficient](https://en.wikipedia.org/wiki/Molar_attenuation_coefficient) {cite}`Norman2018`

$$
\Delta\epsilon(\omega) =
\frac{
	16\pi N_\mathrm{A}
}{
  	\ln\left(10\right)
	\left(4\pi\varepsilon_0\right) c^2
}
\frac{\pi}{3 \hbar}
\sum_{n>0} f(\omega; \omega_{n0},\gamma)\, 
\omega_{n0} R_{n0} 
$$

where $N_\mathrm{A}$ is [Avogadro's constant](https://en.wikipedia.org/wiki/Avogadro_constant), $f$ is the [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution), and $R_{n0}$ is the rotatory strength defined as

$$
R_{n0} =
\sum_{\alpha = x,y,z}
\Im 
\langle 0 | \hat{\mu}_\alpha | n \rangle
\langle n | \hat{m}_\alpha | 0\rangle 
=
\sum_{\alpha = x,y,z}
\frac{-e}{m_\mathrm{e} \omega_{n0}}
\langle 0 | \hat{p}_\alpha | n \rangle
\langle n | \hat{m}_\alpha | 0\rangle
$$

In VeloxChem, the rotatory strength is evaluated in the velocity gauge as given in the second expression, and it is thereby gauge-origin independent.

**Python script**

```
import veloxchem as vlx

xyz="""
...
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = 'cam-b3lyp'
scf_drv.filename = 'mol-ecd'
results = scf_drv.compute(molecule, basis)

rsp_drv = vlx.lreigensolver.LinearResponseEigenSolver()
rsp_drv.nstates=10
rsp_drv.nto = True
rsp_drv.filename = 'mol-ecd'
results = rsp_drv.compute(molecule, basis, results)
```

Download a {download}`Python script <../input_files/alanine-ecd.py>` type of input file to calculate the the ECD spectra for the ten lowest singlet excited states of the alanine molecule at the CAM-B3LYP/def2-svp level of theory.

**Text file**

```
@jobs
task: response
@end

@method settings
basis: def2-svpd
xcfun: b3lyp
@end

@response
property: ecd
nstates: 10
nto: yes
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end

```

Download a {download}`text file <../input_files/alanine-ecd.inp>` type of input file to calculate the ECD spectra for the ten lowest singlet excited state of the alanine molecule at the CAM-B3LYP/def2-svp level of theory.

## Extinction coefficient

The anisotropy of the decadic molar extinction coefficient can be determined directly from the complex polarization propagator evaluated for mixed electric- and magnetic-dipole operators {cite}` Jiem2007`

$$
\Delta\epsilon(\omega) =
\frac{
	16 \pi N_\mathrm{A}
	\omega^2
}{
  	\ln(10)
	\left(4\pi\varepsilon_0\right) c^2
}
\,
\beta(\omega)
$$

where the molecular response property, $\beta(\omega)$, is defined as

$$
\beta(\omega) = -\frac{1}{3 \omega} (G_{xx} + G_{yy} + G_{zz})
$$

and

$$
G_{\alpha\beta} = - \Re\langle\langle\hat{\mu}_\alpha;\hat{m}_\beta
\rangle\rangle_\omega^\gamma = -
\frac{e}{\omega m_e}
\Im 
\langle\langle\hat{p}_\alpha;
\hat{m}_\beta
\rangle\rangle_\omega^\gamma
$$

The mixed electric–magnetic dipole tensor, $G$, is evaluated in the velocity gauge as given in the second expression. Furthermore, it is complex and calculated with a damping term, $\hbar \gamma$, associated with the inverse finite lifetime of the excited states. The default program setting for this parameter is 0.124 eV (or 0.004556 a.u.).

The resulting values for $\Delta \epsilon(\omega)$ 
are converted  from atomic units to units of L mol$^{-1}$ cm$^{-1}$ by multiplying with a factor of $10\, a_0^2$.

**Python script**

```
import veloxchem as vlx

xyz="""
....
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = 'cam-b3lyp'
scf_drv.filename = 'mol-cpp'
scf_results = scf_drv.compute(molecule, basis)

cpp_drv = vlx.ComplexResponse()
cpp_drv.frequencies = np.arange(0.2, 0.35, 0.0025)
cpp_drv.damping = 0.0045563
cpp_drv.cpp_flag = "ecd"
cpp_drv.filename = 'mol-cpp'

cpp_results = cpp_drv.compute(molecule, basis, scf_results)
```

Download a {download}`Python script <../input_files/alanine-cpp.py>` type of input file to calculate the the ECD spectra with the CPP approach for the alanine molecule at the CAM-B3LYP/def2-svp level of theory.

**Text file**

```
@jobs
task: response
@end

@method settings
basis: def2-svpd
xcfun: b3lyp
@end

@response
property: ecd (cpp)
! frequency region (and resolution)
frequencies: 0.05-0.15 (0.0025)
damping: 0.0045563  ! this is the default value
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

Download a {download}`text file <../input_files/alanine-cpp.inp>` type of input file to calculate the the ECD spectra with the CPP approach for the alanine molecule at the CAM-B3LYP/def2-svp level of theory.

(sec:ecm)=
## Exciton coupling model

VeloxChem implements the exciton coupling model to determine circular dichroism spectra.

**Python script**

```
to be added.
```

**Text file**

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
! XYZ coordinates for 40 x 55 atoms
...
@end
```

