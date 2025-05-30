import veloxchem as vlx

xyz = """
9
Ethanol
  H      1.8853     -0.0401      1.0854
  C      1.2699     -0.0477      0.1772
  H      1.5840      0.8007     -0.4449
  H      1.5089     -0.9636     -0.3791
  C     -0.2033      0.0282      0.5345
  H     -0.4993     -0.8287      1.1714
  H     -0.4235      0.9513      1.1064
  O     -0.9394      0.0157     -0.6674
  H     -1.8540      0.0626     -0.4252
"""
mol = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(mol, '6-31g*')
scf_drv = vlx.ScfRestrictedDriver()
scf_drv.solvation_model = 'cpcm'
scf_drv.cpcm_epsilon = 78.39  # Water
scf_drv.filename = 'ethanol-cpcm'

scf_results = scf_drv.compute(mol, basis)