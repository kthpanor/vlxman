# Linear response

## Polarizability

The linear electric-dipole polarizabilty is determined from the linear response function

$$
\alpha_{\alpha\beta}(\omega) =
- 
\langle\langle \hat{\mu}_\alpha; \hat{\mu}_\beta 
\rangle \rangle
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

