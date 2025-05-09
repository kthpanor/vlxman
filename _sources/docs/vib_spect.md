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

## Resonance raman
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
