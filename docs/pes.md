# Potential energy surfaces
Structure optimizations are performed with the aid of geomeTRIC {cite}`geomeTRIC`.

## Ground state optimization

A detailed list of keyword can be found in the [Optimization driver section](./keywords.ipynb#optimization-driver) of the [Input file keywords page](./keywords.ipynb). Dispersion can be activated in the ```@method settings``` section by using the keyword ```dispersion```.

**Python script**
```
import veloxchem as vlx

xyz="""
... 
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-opt'
scf_drv.xcfun = 'b3lyp'
scf_drv.dispersion = 'd4'
results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.filename = 'mol-opt'
opt_results = opt_drv.compute(molecule, basis, results)
```

Download a [Python script](../input_files/bithio-S0-opt.py) type of input file to perfom an optimization for the bithiophene molecule at the B3LYP+D4/def2-svp level of theory.

**Text file**
```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
dispersion: yes # use dft-d4 correction
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```
Download a [text file](../input_files/bithio-S0-opt.inp) type of input file to perfom an optimization for the bithiophene molecule at the B3LYP+D4/def2-svp level of theory.

```{image} ../images/bithio-S0-opt.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Excited state optimization

To optimize an excited state, you need to use the task optimize and to specify which state you want to optimize with the ```state_deriv_index:``` keyword in the ```@gradient``` section.

**Python script**
```
import veloxchem as vlx

xyz="""
... 
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-opt'
scf_drv.xcfun = 'b3lyp'
scf_drv.dispersion = 'd4'
results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.filename = 'mol-opt'
opt_results = opt_drv.compute(molecule, basis, results)
```
Download a [Python script](../input_files/bithio-S1-opt.py) type of input file to perfom an optimization of the first excited state of bithiophene molecule at the B3LYP/def2-svp level of theory.

**Text file**
```
@jobs
task: optimize
@end

@response
property: absorption
nstates: 2
@end

@gradient
state_deriv_index: 1
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

Download a [text file](../input_files/bithio-S1-opt.inp) type of input file to perfom an optimization of the first excited state of bithiophene molecule at the B3LYP/def2-svp level of theory.

```{image} ../images/bithio-S1-opt.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Constrained optimization
A selection of internal coordinate can be ```constraints:``` to ```set```, ```freeze``` or ```scan``` during the molecular structure optimization. It needs to be specified in the ```@optimize``` section. These option apply to the following coordinate:
* ```distance```
* ```angle```
* ```dihedral```

### Set or freeze internal coordinate

```set``` will aim at converge the following internal coordinate to the desired value while ```freeze``` will keep the internal coordinate to the value given in the initial structure. These options are used as 


**Python script**
```
import veloxchem as vlx

xyz="""
...
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'bithio-freeze'
scf_drv.xcfun = 'b3lyp'
results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.constraints = [ "set dihedral 1 3 4 2 90.0", "freeze distance 3 4"]
opt_drv.filename = 'bithio-freeze'
opt_results = opt_drv.compute(molecule, basis, results)
```

Download a [Python script](../input_files/bithio-freeze.py) type of input file to perfom a optimization of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring distance has been frozen to the initial geometry and where the inter-ring dihedral (S-C-C-S) has been constrained to 90°.

**Text file**

```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@optimize
set dihedral 1 3 4 2 90.0
freeze distance 3 4
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end

```

Download a [text file](../input_files/bithio-freeze.inp) type of input file to perfom a optimization of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring distance has been frozen to the initial geometry and where the inter-ring dihedral (S-C-C-S) has been constrained to 90°.

```{image} ../images/bithio-freeze.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

### Scan coordinate

```scan``` will scan an internal coordinate from an initial to a final value in a given number of steps. 
```
scan distance 6 1 1.4 1.5 9
scan angle    6 1 2 100 110 9
scan dihedral 6 1 2 3 0 360 19
```

**Python script**
```
import veloxchem as vlx

xyz="""
...
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'bithio-scan'
scf_drv.xcfun = 'b3lyp'
results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.constraints = ["scan dihedral 1 3 4 2 180 0 9"]
opt_drv.filename = 'bithio-scan'
opt_results = opt_drv.compute(molecule, basis, results)
```

Download a [Python script](../input_files/bithio-scan.py) type of input file to perfom a relaxed scan of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring dihedral (S-C-C-S) is scanned from 180° to 0° in 9 steps.

**Text file**
```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@optimize
scan dihedral 1 3 4 2 180 0 9
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end

```
Download a [text file](../input_files/bithio-scan.inp) type of input file to perfom a relaxed scan of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring dihedral (S-C-C-S) is scanned from 180° to 0° in 9 steps.

```{image} ../images/bithio-scan.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```
