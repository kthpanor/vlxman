(sec:vib_spect)=
# Vibrational spectroscopies

This page presents how to calculate IR, Raman and Resonance Raman spectra by using the keyword: ```do_ir```, ```@do_raman```, ```@do_resonance_raman``` respectively in the ```@vibrational``` section. IR and calculated at the same time as Raman OR resonance Raman.

The following ```@vibrational``` section show you the default settings of the vibrational task.
```
@vibrational
do_ir: yes
do_raman: no
do_resonance_raman: no
@end
```

Calculations of normal modes are performed with the aid of geomeTRIC {cite}`geomeTRIC`.

(sec:ir)=
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

(sec:raman)=
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

(sec:rrs)=
## Resonance Raman
```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_resonance_raman: yes
frequencies: 0.05-0.25 (0.05)
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                      
@end
```
[Download](../input_files/acro-reson-raman.inp) an input file to perfom a Raman spectra calculation of the acroleine molecule at the B3LYP/def2-svp level of theory.

```{image} ../images/acro.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```