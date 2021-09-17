# Linear response

## Polarizability

The linear electric-dipole polarizabilty is determined from the linear response function {cite}`Norman2018`

$$
\alpha_{\alpha\beta}(\omega) =
- 
\langle\langle \hat{\mu}_\alpha; \hat{\mu}_\beta 
\rangle \rangle_\omega
$$

The frequencies of the perturbing electric field is specfied as a `list` or in terms of a frequency region with a frequency point sepation in parenthesis.

```
@jobs
task: response
@end

@method settings
basis: aug-cc-pvdz
@end

@response
property: polarizability
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

## C6 dispersion coefficients

The $C_6$ dispersion coefficient relates to the electric-dipole polarizability according to

$$
C_6 = \frac{3\hbar}{\pi}
\int^{\infty}_0 \bar{\alpha}_A(i\omega) \bar{\alpha}_B(i\omega) 
d\omega
$$

where $\bar{\alpha}_A{i\omega}$ is the isotropic average of the polarizability tensor for molecular system $A$.

The integral over the positive imaginary frequency axis is performed in VeloxChem using a Gauss–Legendre quadrature after substituting the integration variables according to

$$
    i\omega^I = i\omega_0 \frac{1-t}{1+t},\quad d\omega^I = \frac{-2\omega_0 dt}{(1+t)^2},
$$

where a transformation factor of $\omega_0 = 0.3$ a.u. is used. The user may specified the number of frequency grid points used in the quadrature, or otherwise a default value is adopted. The polarizabilities are calculated from the complex polarization propagator (CPP), or complex linear response function {cite}`Norman2018`.

```
@jobs
task: response
@end

@method settings
basis: DEF2-SVPD
dft: yes
grid_level: 4     # this is the default grid density
xcfun: b3lyp
@end

@response
property: C6
conv_thresh: 1.0e-3
n_points: 7
@end

@molecule
charge: 0
multiplicity: 1
units: ang
xyz:
C -5.8575354 3.6359158 -1.6619244
...
@end
```

## Laser pulse propagation

VeloxChem allows for calculation of the linear electric dipole response for the frequency region of a single Gaussian-envelope pulse deemed sufficiently large (using the @pulses module).

The time-domain shape parameters for this pulse may be specified by the user, optionally storing a collection of pertinent results in an HDF5-formatted file or a plaintext ASCII file whose name may be specified by the user.

An example of an input file that when run will carry out such a calculation is given below. For more documentation about the available keywords, please consult the source file whose path from the VeloxChem root folder is src/pymodule/pulsedrsp.py. Note in particular that the default of carrier envelope phase may need adjustment to match your desired setup.

```
@jobs
task: hf
@end

@method settings
basis: aug-cc-pvdz
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

@pulses
envelope: gaussian
field_max : 1.0e-5
number_pulses: 1
centers: 300 
field_cutoff_ratio: 1e-5
frequency_range : 0.2-0.4(0.001)
carrier_frequencies: 0.325
pulse_widths: 50 
pol_dir: xyz
h5 : pulsed
ascii : pulsed
@end
```

If HDF5-formatted data was produced during this calculation, that data may used for plot generation using the script located at `utils/pulsed_response_plot.py` from the VeloxChem root folder.

Also note that other standard python modules such as `matplotlib` must be installed on the system from which this script is run. The script will take the HDF5-formatted data produced during the VeloxChem calculation and generate a plot of the real and imaginary frequency-domain electric dipole polarizability, a representation of the perturbing field in the frequency domain, the resulting (real-valued) first-order dipole moment correction in the time domain and a representation of the perturbing field in the time domain.

For more information and further description of how to run this script, please consult the documentation written inside it.

