import veloxchem as vlx

xyz="""
16

S    1.6198   -1.3808    0.3663    
S   -1.6198    1.3807    0.3663    
C    0.7092    0.0181   -0.0163    
C   -0.7092   -0.0181   -0.0163    
C    1.5156    1.0983   -0.3001    
C   -1.5157   -1.0982   -0.3001    
C    2.8994    0.7731   -0.2024    
C   -2.8994   -0.7731   -0.2024    
C    3.0978   -0.5430    0.1525    
C   -3.0978    0.5430    0.1525    
H    1.1553    2.0818   -0.5754    
H   -1.1553   -2.0818   -0.5753    
H    3.7083    1.4685   -0.3851    
H   -3.7083   -1.4685   -0.3851    
H    4.0400   -1.0528    0.2959    
H   -4.0401    1.0529    0.2959  
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