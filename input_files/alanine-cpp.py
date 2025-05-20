import veloxchem as vlx

xyz="""
13

O    1.4540   -1.0463   -0.2600    
O    1.2497    1.1182    0.4005    
N   -1.4128    1.1501   -0.1734    
C   -0.7093   -0.1115   -0.3951    
C   -1.3291   -1.2038    0.4660    
C    0.7475    0.0933   -0.0380    
H   -0.7772   -0.3698   -1.4569    
H   -2.3997   -1.3089    0.2583    
H   -0.8590   -2.1736    0.2695    
H   -1.2071   -0.9930    1.5349    
H   -0.9750    1.8923   -0.7175    
H   -1.3418    1.4251    0.8055    
H    2.4015   -0.9395   -0.0294  
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = 'cam-b3lyp'
scf_drv.filename = 'alanine-cpp'
scf_results = scf_drv.compute(molecule, basis)

cpp_drv = vlx.ComplexResponse()
cpp_drv.frequencies = np.arange(0.2, 0.35, 0.0025)
cpp_drv.damping = 0.0045563
cpp_drv.cpp_flag = "ecd"
cpp_drv.filename = 'alanine-cpp'

cpp_results = cpp_drv.compute(molecule, basis, scf_results)