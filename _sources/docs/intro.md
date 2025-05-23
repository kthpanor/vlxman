# Next-generation quantum chemistry software

VeloxChem {cite}`veloxchem` is a Python-based open source quantum chemistry software for contemporary and future hardware architectures. It features interactive program access through Jupyter notebooks as well as massively parallel calculations in high-performance computing (HPC) environments. 

VeloxChem offers modeling of complex molecular systems by means of force-field molecular dynamics and polarizable embedding in combination with user-friendly support for automatized solvation and force-field derivations. It is an ideal platform for building simulation workflows and data-driven research {cite}`vlx_workflow`.

VeloxChem is education enabling, providing a means to explain and explore the theory underlying computational chemistry in a highly interactive manner {cite}`echem_edu`. It is science enabling, providing a means for accelerated method development in quantum chemistry {cite}`echem_dev`.

This manual gives a description of the installation process and basic usage of VeloxChem. A more comprehensive view of the ample opportunities for Python software interactions is provided in the [eChem](https://kthpanor.github.io/echem) book {cite}`echem_book`.

```{image} ../images/swedish_moebius.jpg
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: right
```

## Selected functionalities

- Kohn–Sham Density Functional Theory (DFT)
- Time-dependent DFT (TDDFT)
- Complex polarization propagator (CPP)
    - [linear response functions](sec:cpp_lrf)
    - [quadratic response functions](sec:cpp_qrf)
    - [cubic response functions](sec:cpp_crf)
- [Potential energy surface](sec:pes) (PES) exploration for ground and excited states
- [Optical](sec:uv_vis) (UV/vis) and [X-ray absorption](sec:xray) (XAS, XPS)
- [Two-photon absorption](sec:tpa) (TPA)
- [Electronic circular dichroism](sec:ecd) (ECD)
- [Polarizabilities](sec:alpha) and [dispersion coefficients](sec:c6)
- [Vibrational spectroscopies](sec:vib_spect)
    - [Infrared absorption](sec:ir) (IR)
    - [Raman spectroscopy](sec:raman)
    - [Resonance Raman spectroscopy](sec:rrs) (RRS)
- Classical methods
    - [Molecular mechanics](sec:mm) (MM)
    - [Interpolation mechanics](sec:im) (IM)
    - [Molecular dynamics](md) (MD)
    - [Conformational search](sec:conf_search)
    - [Polarizable embedding](sec:pe) (PE)
    - [Localized properties](sec:loc_prop) (LoProp, RESP)
    - [Empirical valence bond](sec:evb) (EVB)