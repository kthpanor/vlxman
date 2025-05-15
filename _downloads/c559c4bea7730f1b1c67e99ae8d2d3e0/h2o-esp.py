import veloxchem as vlx

xyz_str = """
3

O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
"""

molecule = vlx.Molecule.read_xyz_string(xyz_str)
basis = vlx.MolecularBasis.read(molecule, '6-31g')

esp_drv = vlx.RespChargesDriver()
esp_drv.update_settings({
    'number_layers': 5,
    'density': 10.0,
})
esp_drv.filename = 'h2o-esp'
esp_charges = esp_drv.compute(molecule, basis, 'esp')