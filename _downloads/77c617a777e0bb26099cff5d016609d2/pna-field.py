import veloxchem as vlx

pna_xyz_string = """
16
pna
O    2.7374    1.0976   -0.0007   
O    2.7373   -1.0976    0.0003   
N    2.1292    0.0000   -0.0001   
N   -3.4908   -0.0001    0.0001   
C    0.7093    0.0000    0.0005   
C   -2.0804    0.0000   -0.0005   
C    0.0120    1.2080    0.0005   
C    0.0119   -1.2080    0.0001   
C   -1.3829    1.2080    0.0000   
C   -1.3830   -1.2079   -0.0004   
H    0.5219    2.1680    0.0008   
H    0.5218   -2.1680    0.0000   
H   -1.9154    2.1558    0.0003   
H   -1.9154   -2.1557   -0.0006   
H   -3.9970    0.8755   -0.0016   
H   -3.9970   -0.8756   -0.0019 
"""

molecule = vlx.Molecule.read_xyz_string(pna_xyz_string)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'pna-field'
scf_drv.electric_field = [0.01, 0.0, 0.0]
scf_results = scf_drv.compute(molecule, basis)