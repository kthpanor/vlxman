(sec:vib_spect)=
# Vibrational spectroscopies

Calculations of normal modes are performed with the aid of geomeTRIC {cite}`geomeTRIC`.

The associated IR spectrum is calculated by default also when Raman or resonance Raman calculations are requested.

(sec:ir)=
## Infra-red

**Python script**

to be added

**Text file**

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

Download a {download}`text file <../input_files/acro-ir.inp>` type of input file to perform an IR spectrum calculation of the acroleine molecule at the B3LYP/def2-svp level of theory.

(sec:raman)=
## Raman

**Python script**

to be added

**Text file**

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
Download a {download}`text file <../input_files/acro-raman.inp>` type of input file to perform a Raman spectrum calculation of the acroleine molecule at the B3LYP/def2-svp level of theory.

(sec:rrs)=
## Resonance Raman

**Python script**

to be added

**Text file**

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

Download a {download}`text file <../input_files/acro-reson-raman.inp>` type of input file to perform a Raman spectrum calculation of the acroleine molecule at the B3LYP/def2-svp level of theory.

```{image} ../images/acro.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```