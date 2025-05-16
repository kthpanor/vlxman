import veloxchem as vlx
from veloxchem.peforcefieldgenerator import PEForceFieldGenerator

xyz_str = """
3

O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
"""

molecule = vlx.Molecule.read_xyz_string(xyz_str)
basis = vlx.MolecularBasis.read(molecule, 'ANO-S-VDZP')

scf_drv = vlx.ScfRestrictedDriver()
scf_results = scf_drv.compute(molecule, basis)

loprop_drv = vlx.PEForceFieldGenerator()
loprop_filename = 'mol-loprop'
loprop_results = loprop_drv.compute(molecule, basis, scf_results)
