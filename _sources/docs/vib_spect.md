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
C          -7.193469896121       -0.606513185315        0.051392766908                         
C          -5.875615515175       -0.849065291590        0.042481132685                         
C          -4.889535693619        0.245221229217       -0.080553519627                         
O          -3.691300371749        0.086578691883       -0.094301147046                         
H          -5.343436560117        1.269725354663       -0.163335974501                         
H          -7.932396644059       -1.406925824035        0.141819097832                         
H          -7.577705619481        0.416356866537       -0.032850542800                         
H          -5.465794362629       -1.861160187416        0.125149091897                         
@end
```
[Download](../input_files/acro-reson-raman.inp) an input file to perfom a Raman spectra calculation of the acroleine molecule at the B3LYP/def2-svp level of theory.

```{image} ../images/acro.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```