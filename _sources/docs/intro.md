# Home

## Next-generation quantum chemistry software for molecular properties

VeloxChem {cite}`veloxchem` is a Python-based open source quantum chemistry software developed for the calculation of molecular properties and simulation of a variety of spectroscopies.

VeloxChem features interactive program access through Jupyter notebooks as well as large-scale calculations in contemporary high-performance computing (HPC) environments. A comprehensive presentation of the former desktop aspect is provided in the [eChem](https://kthpanor.github.io/echem) book and this manual will focus on the latter HPC aspect.

### Key capabilities

- Kohn–Sham Density Functional Theory (DFT)
- Time-dependent DFT (TDDFT)
- Optical and X-ray absorption
- Electronic circular dichroism (ECD)
- Polarizabilities and dispersion coefficients
- Complex polarization propagator (CPP)
- Response theory for pulses

```{image} ../images/swedish_moebius.jpg
:alt: cover
:class: bg-primary mb-1
:width: 800px
:align: center
```

### Scaling
#### laptop
#### Desktop
#### HPC-CPU
#### HPC-GPU
**GPU-Accelerated Fock Matrix Construction**

Two separate scaling aspects of the GPU implementation of the ERI-part of the Fock matrix construction can be shown: (a) a system size scaling illustrated by the wall times (in seconds) on a single GPU node obtained for spherical water clusters of varying sizes (the inset shows the largest cluster). (b) a strong scaling with respect to the number of GPUs (each with two GCDs), illustrated here by a G-quadruplex including all nucleotides where the phosphate group has been neutralized by adding a hydrogen.
```{image} ../images/hpc-gpu-scaling.jpeg
:alt: cover
:class: bg-primary mb-1
:width: 800px
:align: center
```
Read more in our article [*J. Phys. Chem. A*, **2025**, 129, 2, 633-642](https://doi.org/10.1021/acs.jpca.4c07510) {cite}`veloxchem-gpu`