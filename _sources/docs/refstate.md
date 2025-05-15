# Reference states

A detailed list of keyword can be found in the [SCF optimization section](./keywords.ipynb#scf-optimization) of the [Input file keywords page](./keywords.ipynb).

By default, Hartree-Fock is used if not specified otherwise. To use DFT, several functionals are available and should be specified in the ```@method settings``` section by using the keyword ```xcfun```. See the [Exchange-correlation functionnals](./functionals.ipynb) page for a complete list of functionnals available.

The basis set needs to be specified in the ```@method settings``` section by using the keyword ```basis```. See the [Available basis sets section](./basis_sets.ipynb#available-basis-sets) of the [Input file keywords page](./basis_sets.ipynb).

## Restricted closed-shell

**Python script**
```
import veloxchem as vlx

mol_xyz_string = """
... 
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scfdrv = vlx.ScfRestrictedDriver()
scfdrv.filename = 'mol-scf'
scf_results = scfdrv.compute(molecule, basis)
```
Download a [Python script](../input_files/biphenyl-scf.py) type of input file to perfom a restricted closed-shell calculation for the biphenyl molecule at the HF/def2-svp level of theory.

**Text file**
```
@jobs
task: scf
@end

@method settings
basis: def2-svp
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```
Download a [text format](../input_files/biphenyl-scf.inp) type of input file to perfom a restricted closed-shell calculation for the biphenyl molecule at the HF/def2-svp level of theory.

```{image} ../images/biphenyl.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Restricted open-shell
**Python script**
```
import veloxchem as vlx

mol_xyz_string = """
...
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
molecule.set_multiplicity(2)
basis = vlx.MolecularBasis.read(molecule, '6-31+G*')

scfdrv = vlx.ScfRestrictedOpenDriver()
scfdrv.filename = 'mol-roscf'
scfdrv.xcfun = 'b3lyp'
scf_results = scfdrv.compute(molecule, basis)
```

Download a [Python script](../input_files/tempo-roscf.py) type of input file to perfom a restricted open-shell calculation for the tempo molecule at the B3LYP/6-31+G* level of theory.

**Text file**
```
@jobs
task: roscf
@end

@method settings
basis: 6-31+G*
xcfun: b3lyp
@end

@molecule
charge: 1
multiplicity: 2
xyz:
...
@end
```
Download a [text format](../input_files/tempo-roscf.inp) type of input file to perfom a restricted open-shell calculation for the tempo molecule at the B3LYP/6-31+G* level of theory.

```{image} ../images/tempo.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Unrestricted open-shell
**Python script**
```
import veloxchem as vlx

mol_xyz_string = """
...
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
molecule.set_multiplicity(2)
basis = vlx.MolecularBasis.read(molecule, 'CC-PVDZ')

scfdrv = vlx.ScfUnrestrictedDriver()
scfdrv.filename = 'mol-uscf'
scfdrv.xcfun = 'b3lyp'
scf_results = scfdrv.compute(molecule, basis)
```
Download a [Python script](../input_files/tritylradical-uscf.py) type of input file to perfom a unrestricted open-shell calculation for the triphenylmethyl radical molecule (also called trityl radical) at the PBE0/CC-PVDZ level of theory.

**Text file**
```
@jobs
task: uscf
@end

@method settings
basis: CC-PVDZ
xcfun: PBE0
@end

@molecule
charge: 1
multiplicity: 2
xyz:
...
@end
```
Download a [text format](../input_files/tritylradical-uscf.inp) type of input file to perfom a unrestricted open-shell calculation for the triphenylmethyl radical molecule (also called trityl radical) at the PBE0/CC-PVDZ level of theory.

```{image} ../images/trityl.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Restricted MP2

## Restricted open-shell MP2

## Unrestricted MP2