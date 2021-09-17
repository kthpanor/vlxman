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

## DFT settings

The choice of functional and related settings are performed in the input file section `method settings`:

```
@method settings
dft: yes
grid_level: 4
xcfun: b3lyp
basis: def2-svp
@end
```

Grid densities are available up to level 6. Level 4 (default) is recommended for production calculations.