# Reference states

By default, the Hartree–Fock method is employed. 

To use Kohn–Sham DFT, any of the several available functionals is specified as illustrated below, see the [exchange-correlation functionals](sec:xc-functionals) page for a complete list of available functionals.

For input text files, a detailed [list of keywords](sec:text-file-keywords) is available.

(sec:rhf)=
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

Download a {download}`Python script <../input_files/biphenyl-scf.py>` type of input file to perfom a restricted closed-shell calculation for the biphenyl molecule at the HF/def2-svp level of theory.

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

Download a {download}`text format <../input_files/biphenyl-scf.inp>` type of input file to perfom a restricted closed-shell calculation for the biphenyl molecule at the HF/def2-svp level of theory.

```{image} ../images/biphenyl.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

(sec:rohf)=
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

Download a {download}`Python script <../input_files/tempo-roscf.py>` type of input file to perfom a restricted open-shell calculation for the tempo molecule at the B3LYP/6-31+G* level of theory.

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

Download a {download}`text format <../input_files/tempo-roscf.inp>` type of input file to perfom a restricted open-shell calculation for the tempo molecule at the B3LYP/6-31+G* level of theory.

```{image} ../images/tempo.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

(sec:uhf)=
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

Download a {download}`Python script <../input_files/tritylradical-uscf.py>` type of input file to perfom a unrestricted open-shell calculation for the triphenylmethyl radical molecule (also called trityl radical) at the PBE0/CC-PVDZ level of theory.

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

Download a {download}`text format <../input_files/tritylradical-uscf.inp>` type of input file to perfom a unrestricted open-shell calculation for the triphenylmethyl radical molecule (also called trityl radical) at the PBE0/CC-PVDZ level of theory.

```{image} ../images/trityl.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

(sec:rmp2)=
## Restricted MP2

to be added

(sec:romp2)=
## Restricted open-shell MP2

to be added

(sec:ump2)=
## Unrestricted MP2

to be added