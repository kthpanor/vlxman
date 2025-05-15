import veloxchem as vlx

xyz_str = """
3

O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
"""

molecule = vlx.Molecule.read_xyz_string(xyz_str)
basis = vlx.MolecularBasis.read(molecule, '6-31g*')

resp_drv = vlx.RespChargesDriver()
resp_drv.update_settings({
    'equal_charges': '2 = 3'
})

resp_drv.filename = 'h2o-resp'
resp_charges = resp_drv.compute(molecule, basis, 'resp')