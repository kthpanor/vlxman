import veloxchem as vlx

xyz="""
23

 C     0.000000     0.000000     0.000000
 C     0.000000     0.000000     1.372392
 C     1.315167     0.000000     1.911076
 C     2.315788     0.001031     0.954378
 S     1.603295     0.033860    -0.650359
 H    -0.854687     0.017432    -0.665190
 H    -0.900911     0.012327     1.976681
 H     1.519439     0.018972     2.976026
 C     3.758271    -0.085520     1.221926
 C     4.757912     0.378181     0.298373
 C     4.208212    -0.631060     2.421991
 C     6.149986     0.297452     0.639308
 C     5.579107    -0.697727     2.756838
 H     3.486422    -1.038667     3.122333
 C     6.546284    -0.242044     1.887128
 H     7.606314    -0.292342     2.115880
 H     5.865260    -1.131054     3.711559
 N     4.377322     0.889740    -0.902165
 N     7.111962     0.730864    -0.227724
 C     5.324149     1.295576    -1.721040
 C     6.701080     1.216907    -1.379770
 H     5.014508     1.702048    -2.682606
 H     7.461494     1.563897    -2.077711
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = 'cam-b3lyp'
scf_drv.filename = 'tq-cpp'
results = scf_drv.compute(molecule, basis)

rsp_drv = vlx.lreigensolver.LinearResponseEigenSolver()

rsp_drv.nto = True
rsp_results = rsp_drv.compute(molecule, basis, results)

