# Exchange–correlation functionals

## Available functionals

- Exchange functional
	- SLATER
	- BECKE88
	- B88X

- Correlation functional
	- VWN3
	- LYP

- Exchange-correlation functional
	- SLDA
	- BLYP
	- B3LYP
	- BHANDH
	- BHANDHLYP

More functionals are being implemented and range-separated hybrids are a priority.

## DFT settings

The choice of functional and related settings are performed in the input file section `method settings`:

```
@method settings
dft: yes
xcfun: b3lyp
grid_level: 4
@end
```

To change to another functional, replace `b3lyp` with any of the others (as spelled in the list above). 

Grid densities are available up to level 6. Level 4 (default) is recommended for production calculations.