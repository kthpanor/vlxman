# Source code structure

## Python layer

In a Jupyter notebook, the file module locatation of an object can be found with by adding "?" at the end of an object name:

```
vlx.ScfRestrictedDriver.compute?
```

In return the following information is given:

```
Signature: vlx.ScfRestrictedDriver.compute(self, molecule, ao_basis, min_basis=None)
Docstring:
Performs SCF calculation using molecular data.

:param molecule:
    The molecule.
:param ao_basis:
    The AO basis set.
:param min_basis:
    The minimal AO basis set.
File:      /opt/miniconda3/envs/vlxr02/lib/python3.9/site-packages/veloxchem/scfdriver.py
Type:      function
```

revealing, among other things, the module file name and the file location.

## C++ layer

The C++ layer implements the compute-intensive routines for the calculations of one- and two-electron integrals as well as the DFT kernel integrations. To add functionality in this layer is less straightforward but also not foreseen to be needed for the great majority of regular and advanced users.