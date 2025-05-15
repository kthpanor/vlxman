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
scfdrv = vlx.ScfUnrestrictedDriver()
scfdrv.filename = 'mol-loprop'
scfdrv.xcfun = 'b3lyp'
scf_results = scfdrv.compute(molecule, basis)


pe_ff_gen = PEForceFieldGenerator()
pe_ff_gen.filename = 'mol-loprop'
pe_ff_results = pe_ff_gen.compute(molecule, basis, scf_results)
