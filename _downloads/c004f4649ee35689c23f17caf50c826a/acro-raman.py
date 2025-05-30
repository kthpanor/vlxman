import veloxchem as vlx

xyz="""
8

C          -7.193469896121       -0.606513185315        0.051392766908                         
C          -5.875615515175       -0.849065291590        0.042481132685                         
C          -4.889535693619        0.245221229217       -0.080553519627                         
O          -3.691300371749        0.086578691883       -0.094301147046                         
H          -5.343436560117        1.269725354663       -0.163335974501                         
H          -7.932396644059       -1.406925824035        0.141819097832                         
H          -7.577705619481        0.416356866537       -0.032850542800                         
H          -5.465794362629       -1.861160187416        0.125149091897      
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'acro-raman'
scf_drv.xcfun = 'b3lyp'
results = scf_drv.compute(molecule, basis)

vib_drv = vlx.VibrationalAnalysis(scf_drv)
vib_drv.do_ir = False
vib_drv.do_raman = True
vib_drv.filename = 'acro-raman'
vib_results = vib_drv.compute(molecule, basis)