# Vibrational spectroscopies

This page presents how to calculate IR, Raman and Resonance Raman spectra by using the keyword: ```do_ir```, ```@do_raman```, ```@do_resonance_raman``` respectively in the ```@vibrational``` section. Note that one can perform all three spectrosocopies at the time. 
```
@vibrational
do_ir: yes
do_raman: yes
do_resonance_raman: yes
frequencies: 0.05-0.25 (0.05)
@end
```

## Infra-red

```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_ir: yes
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                     
@end
```
[Download](../input_files/acro-ir.inp) an input file to perfom an IR spectra calculation of the acroleine molecule at the B3LYP/def2-svp level of theory.

## Raman
```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_raman: yes
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                     
@end
```
[Download](../input_files/acro-raman.inp) an input file to perfom a Raman spectra calculation of the acroleine molecule at the B3LYP/def2-svp level of theory.

## Resonance raman

This is under construction

```{image} ../images/acro.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```