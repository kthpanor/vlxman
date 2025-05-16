import veloxchem as vlx

xyz_string="""
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

molecule = vlx.Molecule.from_xyz_string(xyz_string)
basis = vlx.MolecularBasis.read(molecule,"def2-svp")

# Ground state electronic structure
scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

# TDDFT linear response
rsp_drv = vlx.LinearResponseEigenSolver()
rsp_drv.nstates = 2
rsp_results = rsp_drv.compute(molecule, basis, scf_results)

# TDDFT gradient settings and optimization
grad_drv = vlx.TddftGradientDriver(scf_drv)
grad_drv.state_deriv_index = 1

opt_drv = vlx.OptimizationDriver(grad_drv)
opt_drv.filename = "bithio-S1-opt"
opt_results = opt_drv.compute(molecule, basis, scf_drv, rsp_drv, rsp_results)