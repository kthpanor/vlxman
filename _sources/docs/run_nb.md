# Running in a Notebook

## SCF optimization

```
import veloxchem as vlx

molecule_string = """
    O 0 0 0
    H 0 0 1.795239827225189
    H 1.693194615993441 0 -0.599043184453037"""

molecule = vlx.Molecule.read_str(molecule_string, units='angstrom')

basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_settings = {'conv_thresh': 1.0e-6}
method_settings = {'xcfun': 'b3lyp', 'grid_level': 4}

scfdrv = vlx.ScfRestrictedDriver()
scfdrv.update_settings(scf_settings, method_settings)
scfdrv.compute(molecule, basis)
```

A comprehensive presenation of how to interact and run the VeloxChem program in a Jupyter notebook is provided in the [eChem book](https://kthpanor.github.io/echem).