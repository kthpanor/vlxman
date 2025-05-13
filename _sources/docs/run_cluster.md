# Running on a cluster

On a supercomputer cluster, it is a common practice to submit a job script to a batch queue system such as e.g. [SLURM](https://en.wikipedia.org/wiki/Slurm_Workload_Manager). 

## Job script

In the job script, one specifies the amount of resources to be used for the calculation as well as a line launching the application across the allocated nodes using e.g. `srun` or `mpirun`. In this scenario, VeloxChem is run with an input file in the form of either a Python script or a text file. In the example job script given below, both alternatives are provided and you activate the one that you prefer using.

```bash
#!/bin/bash

#SBATCH -A project_name
#SBATCH -p partition_name
#SBATCH -J job_name
#SBATCH -t 01:00:00

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

module load veloxchem/1.0

export OMP_NUM_THREADS=16
export OMP_PLACES=cores
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

# using a Python script type of input file
srun python myjob.py > myjob.out
# using a text type of input file
#srun vlx myjob.inp myjob.out

# end of job script
```

This script will start a job on two nodes with eight MPI ranks per node (one per [NUMA](https://en.wikipedia.org/wiki/Non-uniform_memory_access) domain), each with 16 OpenMP threads.

## Input file

**Python script**

An example Python script type of input file named `myjob.py` in the job script above and and which is running an SCF optimization takes the following form.

```
import veloxchem as vlx

xyz_string = """
3
water
O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
"""

molecule = vlx.Molecule.read_xyz_string(xyz_string)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_drv.filename = "vlx_results_hdf5"

scf_results = scfdrv.compute(molecule, basis)
```

The results of the calculation are stored in an [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) file with a user specified name. This file can be directly read and analyzed with VIAMD.

**Text file**

The same SCF calculation can be performed with use of an input file in text format named `myjob.inp` in the in the job script above--such an input file consists of multiple groups marked with `@group name` and `@end`.

```
@jobs
task: scf
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@molecule
charge: 0
multiplicity: 1
xyz:
O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
@end
```

## Benchmark reference

In order to ensure that your installation of the VeloxChem program performs well and that you are correctly launching the program on your cluster hardware, you may wish to reproduce the following benchmark calculation. With a different hardware execution times will be different, but with use of the same *total number of cores* (i.e. 128) you should expect a similar wall time.

* Property: ECD response
* Level: B3LYP/def2-SVP
* Number basis functions: 1,252
* Number of atoms: 137
* Number states: 20
* Nodes: Intel Xeon Gold 6130 (dual socket)
* Number nodes (MPI ranks): 4
* Number cores per node (OpenMP threads): 32


Wall time:

* SCF optimization: 456 sec
* Total: 7,992 sec

Input file:
```
@jobs
task: response
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@response
property: ecd
nstates: 20
@end

@molecule
charge: 0
multiplicity: 1
xyz:
O          2.85983        0.91384       -2.06648
O          2.91766       -0.59967        2.31158
O          1.61081        0.79775       -3.95288
O         -4.58216       -0.30147        0.12976
O          1.62210       -0.61859        4.16984
N         -1.11048        3.88801        0.35683
N         -0.63092       -4.03594       -0.15586
C          5.00779       -0.21419       -3.50111
H          5.24972        0.69745       -4.05413
H          5.68771       -1.00035       -3.84164
H          5.19764       -0.03389       -2.44288
C          3.55267       -0.65541       -3.74857
C          2.55785        0.42871       -3.31478
C          1.92055        1.74531       -1.42078
C          0.74077        1.14696       -1.01169
H          0.57622        0.10409       -1.24098
C         -0.22639        1.90065       -0.34253
C         -1.57199        1.65326        0.12541
C         -2.45868        0.55250        0.18347
C         -2.37232       -0.88729        0.01986
C         -1.35711       -1.87091        0.06195
C          0.00606       -1.95307        0.53626
C          0.86586       -1.08638        1.21404
H          0.57579       -0.06842        1.43014
C          2.09678       -1.54122        1.65565
C          2.52970       -0.14129        3.54660
C          3.37021        1.06449        3.98536
C          3.10010        1.33208        5.47400
H          2.03707        1.49093        5.65902
H          3.64937        2.22145        5.79507
H          3.42032        0.48984        6.09202
C          3.33537       -0.94841       -5.24102
H          2.30441       -1.24449       -5.43864
H          3.99992       -1.75634       -5.55939
H          3.54847       -0.06816       -5.85217
C          2.22749        3.10559       -1.16986
C          1.23860        3.86135       -0.53304
H          1.40064        4.91344       -0.35616
C          0.02444        3.28388       -0.16181
C         -1.28159        5.30180        0.66153
H         -0.29064        5.72259        0.84850
H         -1.83086        5.37812        1.60516
C         -2.00463        6.11677       -0.42433
H         -2.99521        5.68458       -0.59435
H         -2.17136        7.12153       -0.01845
C         -1.25313        6.21272       -1.75383
H         -0.28196        6.70112       -1.62818
H         -1.82509        6.79720       -2.47898
H         -1.07770        5.22551       -2.18678
C         -2.10242        2.91752        0.47884
C         -3.45109        3.12316        0.79878
H         -3.78652        4.11251        1.07136
C         -4.37348        2.08188        0.70112
C         -3.82759        0.83232        0.34748
C         -3.69994       -1.33478       -0.10683
C          2.56297       -2.85918        1.42730
C          3.95892       -3.34562        1.87411
C          4.22560       -4.80472        1.45033
H          5.23357       -5.08757        1.76435
H          4.17108       -4.93400        0.36609
H          3.52939       -5.50474        1.92023
C          5.05764       -2.47469        1.21982
H          4.94867       -1.42349        1.47873
H          5.01820       -2.56389        0.13049
H          6.04627       -2.81051        1.54878
C          4.08159       -3.29526        3.41532
H          4.01133       -2.28170        3.80388
H          5.04868       -3.70466        3.72400
H          3.29434       -3.88933        3.88635
C          1.68478       -3.72769        0.77107
H          1.97936       -4.75016        0.59135
C          0.41953       -3.29825        0.37096
C         -0.67050       -5.48091       -0.32996
H         -1.58305       -5.85856        0.14323
H          0.16594       -5.90662        0.22858
C         -0.61307       -5.94218       -1.79429
H         -1.45748       -5.50877       -2.33943
H         -0.76201       -7.02814       -1.80441
C          0.69496       -5.58870       -2.50452
H          0.86470       -4.50955       -2.50524
H          0.67794       -5.92440       -3.54438
H          1.55256       -6.06262       -2.01678
C         -1.73373       -3.19231       -0.27806
C         -3.05493       -3.56567       -0.55799
H         -3.27315       -4.59058       -0.81809
C         -4.09645       -2.64596       -0.43530
C         -5.56764       -3.03569       -0.65751
C         -6.37978       -2.78714        0.63503
H         -5.97686       -3.37564        1.46401
H         -7.42243       -3.08375        0.48414
H         -6.36462       -1.73752        0.92433
C         -6.15542       -2.20030       -1.81931
H         -6.10183       -1.13146       -1.61493
H         -7.20539       -2.46473       -1.97890
H         -5.61191       -2.39547       -2.74792
C         -5.71941       -4.52344       -1.02679
H         -5.19133       -4.77195       -1.95145
H         -6.77761       -4.74843       -1.18271
H         -5.35728       -5.18167       -0.23222
C          4.87296        0.81676        3.75451
H          5.22631       -0.05348        4.31427
H          5.44074        1.68628        4.09790
H          5.09559        0.65890        2.69907
C          2.90639        2.27251        3.13880
H          3.06952        2.09716        2.07417
H          3.46898        3.16318        3.43345
H          1.84391        2.47762        3.29396
C         -5.87374        2.28423        0.97290
C         -6.19729        3.73994        1.35896
H         -5.67367        4.04877        2.26785
H         -7.26947        3.83051        1.55120
H         -5.94693        4.44149        0.55837
C         -6.69059        1.94125       -0.29481
H         -6.39226        2.57924       -1.13144
H         -7.75663        2.10402       -0.10799
H         -6.55357        0.90307       -0.59332
C         -6.31439        1.37772        2.14642
H         -6.13516        0.32470        1.93193
H         -7.38322        1.50879        2.34198
H         -5.76887        1.63539        3.05843
C          3.56795        3.75404       -1.57934
C          3.72848        3.73961       -3.11775
H          2.89180        4.25223       -3.59918
H          3.77626        2.73025       -3.52021
H          4.65188        4.25548       -3.39949
C          3.65734        5.22802       -1.13299
H          4.63428        5.62696       -1.41774
H          3.56166        5.33562       -0.04923
H          2.89851        5.85156       -1.61346
C          4.74460        3.00550       -0.90928
H          4.76131        1.95188       -1.18011
H          4.67241        3.07672        0.17963
H          5.69526        3.45529       -1.21301
C          3.24304       -1.91769       -2.91145
H          3.37067       -1.72815       -1.84443
H          3.91926       -2.72629       -3.20357
H          2.21795       -2.25829       -3.07923
@end
```

Output file:

```
!========================================================================================================================!
!                                                                                                                        !
!                                                       VELOXCHEM                                                        !
!                                              AN ELECTRONIC STRUCTURE CODE                                              !
!                                                                                                                        !
!                                     Copyright (C) 2018-2022 VeloxChem developers.                                      !
!                                                  All rights reserved.                                                  !
!========================================================================================================================!
!                      VeloxChem execution started on 4 compute nodes at Wed Nov  9 20:32:41 2022.                       !
!========================================================================================================================!

* Info * Using 32 OpenMP threads per compute node.

* Info * Reading input file ecd-benchmark.inp...

* Info * @jobs
* Info * task: response
* Info * @end

* Info * @method_settings
* Info * xcfun: b3lyp
* Info * basis: def2-svp
* Info * @end

* Info * @response
* Info * property: ecd
* Info * nstates: 20
* Info * @end

                                              Molecular Geometry (Angstroms)
                                             ================================

                          Atom         Coordinate X          Coordinate Y          Coordinate Z

                           O           2.859830000000        0.913840000000       -2.066480000000
                           O           2.917660000000       -0.599670000000        2.311580000000
                           O           1.610810000000        0.797750000000       -3.952880000000
                           O          -4.582160000000       -0.301470000000        0.129760000000
                           O           1.622100000000       -0.618590000000        4.169840000000
                           N          -1.110480000000        3.888010000000        0.356830000000
                           N          -0.630920000000       -4.035940000000       -0.155860000000
                           C           5.007790000000       -0.214190000000       -3.501110000000
                           H           5.249720000000        0.697450000000       -4.054130000000
                           H           5.687710000000       -1.000350000000       -3.841640000000
                           H           5.197640000000       -0.033890000000       -2.442880000000
                           C           3.552670000000       -0.655410000000       -3.748570000000
                           C           2.557850000000        0.428710000000       -3.314780000000
                           C           1.920550000000        1.745310000000       -1.420780000000
                           C           0.740770000000        1.146960000000       -1.011690000000
                           H           0.576220000000        0.104090000000       -1.240980000000
                           C          -0.226390000000        1.900650000000       -0.342530000000
                           C          -1.571990000000        1.653260000000        0.125410000000
                           C          -2.458680000000        0.552500000000        0.183470000000
                           C          -2.372320000000       -0.887290000000        0.019860000000
                           C          -1.357110000000       -1.870910000000        0.061950000000
                           C           0.006060000000       -1.953070000000        0.536260000000
                           C           0.865860000000       -1.086380000000        1.214040000000
                           H           0.575790000000       -0.068420000000        1.430140000000
                           C           2.096780000000       -1.541220000000        1.655650000000
                           C           2.529700000000       -0.141290000000        3.546600000000
                           C           3.370210000000        1.064490000000        3.985360000000
                           C           3.100100000000        1.332080000000        5.474000000000
                           H           2.037070000000        1.490930000000        5.659020000000
                           H           3.649370000000        2.221450000000        5.795070000000
                           H           3.420320000000        0.489840000000        6.092020000000
                           C           3.335370000000       -0.948410000000       -5.241020000000
                           H           2.304410000000       -1.244490000000       -5.438640000000
                           H           3.999920000000       -1.756340000000       -5.559390000000
                           H           3.548470000000       -0.068160000000       -5.852170000000
                           C           2.227490000000        3.105590000000       -1.169860000000
                           C           1.238600000000        3.861350000000       -0.533040000000
                           H           1.400640000000        4.913440000000       -0.356160000000
                           C           0.024440000000        3.283880000000       -0.161810000000
                           C          -1.281590000000        5.301800000000        0.661530000000
                           H          -0.290640000000        5.722590000000        0.848500000000
                           H          -1.830860000000        5.378120000000        1.605160000000
                           C          -2.004630000000        6.116770000000       -0.424330000000
                           H          -2.995210000000        5.684580000000       -0.594350000000
                           H          -2.171360000000        7.121530000000       -0.018450000000
                           C          -1.253130000000        6.212720000000       -1.753830000000
                           H          -0.281960000000        6.701120000000       -1.628180000000
                           H          -1.825090000000        6.797200000000       -2.478980000000
                           H          -1.077700000000        5.225510000000       -2.186780000000
                           C          -2.102420000000        2.917520000000        0.478840000000
                           C          -3.451090000000        3.123160000000        0.798780000000
                           H          -3.786520000000        4.112510000000        1.071360000000
                           C          -4.373480000000        2.081880000000        0.701120000000
                           C          -3.827590000000        0.832320000000        0.347480000000
                           C          -3.699940000000       -1.334780000000       -0.106830000000
                           C           2.562970000000       -2.859180000000        1.427300000000
                           C           3.958920000000       -3.345620000000        1.874110000000
                           C           4.225600000000       -4.804720000000        1.450330000000
                           H           5.233570000000       -5.087570000000        1.764350000000
                           H           4.171080000000       -4.934000000000        0.366090000000
                           H           3.529390000000       -5.504740000000        1.920230000000
                           C           5.057640000000       -2.474690000000        1.219820000000
                           H           4.948670000000       -1.423490000000        1.478730000000
                           H           5.018200000000       -2.563890000000        0.130490000000
                           H           6.046270000000       -2.810510000000        1.548780000000
                           C           4.081590000000       -3.295260000000        3.415320000000
                           H           4.011330000000       -2.281700000000        3.803880000000
                           H           5.048680000000       -3.704660000000        3.724000000000
                           H           3.294340000000       -3.889330000000        3.886350000000
                           C           1.684780000000       -3.727690000000        0.771070000000
                           H           1.979360000000       -4.750160000000        0.591350000000
                           C           0.419530000000       -3.298250000000        0.370960000000
                           C          -0.670500000000       -5.480910000000       -0.329960000000
                           H          -1.583050000000       -5.858560000000        0.143230000000
                           H           0.165940000000       -5.906620000000        0.228580000000
                           C          -0.613070000000       -5.942180000000       -1.794290000000
                           H          -1.457480000000       -5.508770000000       -2.339430000000
                           H          -0.762010000000       -7.028140000000       -1.804410000000
                           C           0.694960000000       -5.588700000000       -2.504520000000
                           H           0.864700000000       -4.509550000000       -2.505240000000
                           H           0.677940000000       -5.924400000000       -3.544380000000
                           H           1.552560000000       -6.062620000000       -2.016780000000
                           C          -1.733730000000       -3.192310000000       -0.278060000000
                           C          -3.054930000000       -3.565670000000       -0.557990000000
                           H          -3.273150000000       -4.590580000000       -0.818090000000
                           C          -4.096450000000       -2.645960000000       -0.435300000000
                           C          -5.567640000000       -3.035690000000       -0.657510000000
                           C          -6.379780000000       -2.787140000000        0.635030000000
                           H          -5.976860000000       -3.375640000000        1.464010000000
                           H          -7.422430000000       -3.083750000000        0.484140000000
                           H          -6.364620000000       -1.737520000000        0.924330000000
                           C          -6.155420000000       -2.200300000000       -1.819310000000
                           H          -6.101830000000       -1.131460000000       -1.614930000000
                           H          -7.205390000000       -2.464730000000       -1.978900000000
                           H          -5.611910000000       -2.395470000000       -2.747920000000
                           C          -5.719410000000       -4.523440000000       -1.026790000000
                           H          -5.191330000000       -4.771950000000       -1.951450000000
                           H          -6.777610000000       -4.748430000000       -1.182710000000
                           H          -5.357280000000       -5.181670000000       -0.232220000000
                           C           4.872960000000        0.816760000000        3.754510000000
                           H           5.226310000000       -0.053480000000        4.314270000000
                           H           5.440740000000        1.686280000000        4.097900000000
                           H           5.095590000000        0.658900000000        2.699070000000
                           C           2.906390000000        2.272510000000        3.138800000000
                           H           3.069520000000        2.097160000000        2.074170000000
                           H           3.468980000000        3.163180000000        3.433450000000
                           H           1.843910000000        2.477620000000        3.293960000000
                           C          -5.873740000000        2.284230000000        0.972900000000
                           C          -6.197290000000        3.739940000000        1.358960000000
                           H          -5.673670000000        4.048770000000        2.267850000000
                           H          -7.269470000000        3.830510000000        1.551200000000
                           H          -5.946930000000        4.441490000000        0.558370000000
                           C          -6.690590000000        1.941250000000       -0.294810000000
                           H          -6.392260000000        2.579240000000       -1.131440000000
                           H          -7.756630000000        2.104020000000       -0.107990000000
                           H          -6.553570000000        0.903070000000       -0.593320000000
                           C          -6.314390000000        1.377720000000        2.146420000000
                           H          -6.135160000000        0.324700000000        1.931930000000
                           H          -7.383220000000        1.508790000000        2.341980000000
                           H          -5.768870000000        1.635390000000        3.058430000000
                           C           3.567950000000        3.754040000000       -1.579340000000
                           C           3.728480000000        3.739610000000       -3.117750000000
                           H           2.891800000000        4.252230000000       -3.599180000000
                           H           3.776260000000        2.730250000000       -3.520210000000
                           H           4.651880000000        4.255480000000       -3.399490000000
                           C           3.657340000000        5.228020000000       -1.132990000000
                           H           4.634280000000        5.626960000000       -1.417740000000
                           H           3.561660000000        5.335620000000       -0.049230000000
                           H           2.898510000000        5.851560000000       -1.613460000000
                           C           4.744600000000        3.005500000000       -0.909280000000
                           H           4.761310000000        1.951880000000       -1.180110000000
                           H           4.672410000000        3.076720000000        0.179630000000
                           H           5.695260000000        3.455290000000       -1.213010000000
                           C           3.243040000000       -1.917690000000       -2.911450000000
                           H           3.370670000000       -1.728150000000       -1.844430000000
                           H           3.919260000000       -2.726290000000       -3.203570000000
                           H           2.217950000000       -2.258290000000       -3.079230000000

                          Molecular charge            : 0
                          Spin multiplicity           : 1
                          Number of atoms             : 137
                          Number of alpha electrons   : 232
                          Number of beta  electrons   : 232

* Info * Reading basis set from file: /proj/panor/users/x_lixin/gitlab/VeloxChemMP/venv/lib/python3.8/site-packages/veloxchem/basis/DEF2-SVP

                                              Molecular Basis (Atomic Basis)
                                             ================================

                                  Basis: DEF2-SVP

                                  Atom Contracted GTOs          Primitive GTOs

                                   O   (3S,2P,1D)               (7S,4P,1D)
                                   H   (2S,1P)                  (4S,1P)
                                   C   (3S,2P,1D)               (7S,4P,1D)
                                   N   (3S,2P,1D)               (7S,4P,1D)

                                  Contracted Basis Functions : 1252
                                  Primitive Basis Functions  : 2030


                                            Self Consistent Field Driver Setup
                                           ====================================

                   Wave Function Model             : Spin-Restricted Kohn-Sham
                   Initial Guess Model             : Superposition of Atomic Densities
                   Convergence Accelerator         : Two Level Direct Inversion of Iterative Subspace
                   Max. Number of Iterations       : 50
                   Max. Number of Error Vectors    : 10
                   Convergence Threshold           : 1.0e-06
                   ERI Screening Scheme            : Cauchy Schwarz + Density
                   ERI Screening Mode              : Dynamic
                   ERI Screening Threshold         : 1.0e-12
                   Linear Dependence Threshold     : 1.0e-06
                   Exchange-Correlation Functional : B3LYP
                   Molecular Grid Level            : 4

* Info * Nuclear repulsion energy: 10340.6482081688 a.u.

* Info * Molecular grid with 1558984 points generated in 2.52 sec.

* Info * Overlap matrix computed in 0.01 sec.

* Info * Kinetic energy matrix computed in 0.01 sec.

* Info * Nuclear potential matrix computed in 0.39 sec.

* Info * Orthogonalization matrix computed in 0.24 sec.

* Info * SAD initial guess computed in 0.04 sec.

* Info * Starting Reduced Basis SCF calculation...
* Info * ...done. SCF energy in reduced basis set: -2643.778886664923 a.u. Time: 32.95 sec.

* Info * Overlap matrix computed in 0.01 sec.

* Info * Kinetic energy matrix computed in 0.01 sec.

* Info * Nuclear potential matrix computed in 0.39 sec.

* Info * Orthogonalization matrix computed in 0.29 sec.


               Iter. |    Kohn-Sham Energy | Energy Change | Gradient Norm | Max. Gradient | Density Change
               --------------------------------------------------------------------------------------------
                  1     -2662.242575977716    0.0000000000      0.92638287      0.03265315      0.00000000
                  2     -2662.226028248542    0.0165477292      1.02213918      0.02906963      0.94002206
                  3     -2662.338901683494   -0.1128734350      0.31423891      0.00774929      0.52847674
                  4     -2662.347949700810   -0.0090480173      0.10014039      0.00202751      0.17287238
                  5     -2662.348971905070   -0.0010222043      0.03417167      0.00052653      0.06063523
                  6     -2662.349100914202   -0.0001290091      0.00858497      0.00011362      0.02036779
                  7     -2662.349108127131   -0.0000072129      0.00460381      0.00007065      0.00596992
                  8     -2662.349110477306   -0.0000023502      0.00121290      0.00002151      0.00247467
                  9     -2662.349110638947   -0.0000001616      0.00042706      0.00000581      0.00077898
                 10     -2662.349110659790   -0.0000000208      0.00013542      0.00000164      0.00025880
                 11     -2662.349110661773   -0.0000000020      0.00005981      0.00000089      0.00009203
                 12     -2662.349110662193   -0.0000000004      0.00002265      0.00000037      0.00003744
                 13     -2662.349110662259   -0.0000000001      0.00000686      0.00000011      0.00001432
                 14     -2662.349110662257    0.0000000000      0.00000318      0.00000007      0.00000507
                 15     -2662.349110662266   -0.0000000000      0.00000183      0.00000004      0.00000227
                 16     -2662.349110662264    0.0000000000      0.00000046      0.00000001      0.00000089

* Info * Checkpoint written to file: ecd-benchmark.scf.h5

* Info * SCF tensors written to file: ecd-benchmark.scf.tensors.h5

               *** SCF converged in 16 iterations. Time: 455.52 sec.

               Spin-Restricted Kohn-Sham:
               --------------------------
               Total Energy                       :    -2662.3491106623 a.u.
               Electronic Energy                  :   -13002.9973188311 a.u.
               Nuclear Repulsion Energy           :    10340.6482081688 a.u.
               ------------------------------------
               Gradient Norm                      :        0.0000004636 a.u.


               Ground State Information
               ------------------------
               Charge of Molecule            :  0.0
               Multiplicity (2S+1)           :  1.0
               Magnetic Quantum Number (M_S) :  0.0


                                                 Spin Restricted Orbitals
                                                 ------------------------

               Molecular Orbital No. 228:
               --------------------------
               Occupation: 2.000 Energy:   -0.23864 a.u.
               (  54 C   1p0 :     0.17) (  55 C   1p0 :    -0.17) (  84 C   1p0 :     0.15)

               Molecular Orbital No. 229:
               --------------------------
               Occupation: 2.000 Energy:   -0.21366 a.u.
               (  18 C   1p0 :    -0.19) (  21 C   1p0 :     0.19) (  36 C   1p0 :    -0.15)
               (  50 C   1p0 :    -0.15)

               Molecular Orbital No. 230:
               --------------------------
               Occupation: 2.000 Energy:   -0.21184 a.u.
               (  14 C   1p0 :    -0.16) (  25 C   1p0 :    -0.17) (  39 C   1p0 :     0.16)
               (  72 C   1p0 :     0.17) (  86 C   1p0 :     0.16)

               Molecular Orbital No. 231:
               --------------------------
               Occupation: 2.000 Energy:   -0.19103 a.u.
               (   7 N   1p0 :    -0.24) (   7 N   2p0 :     0.21) (  20 C   1p0 :     0.17)
               (  25 C   1p0 :     0.15) (  51 C   1p0 :     0.16) (  55 C   1p0 :     0.21)
               (  55 C   2p0 :     0.15) (  84 C   1p0 :    -0.20) (  84 C   2p0 :    -0.16)

               Molecular Orbital No. 232:
               --------------------------
               Occupation: 2.000 Energy:   -0.19042 a.u.
               (   4 O   1p0 :    -0.18) (   4 O   2p0 :    -0.15) (   6 N   1p0 :    -0.24)
               (   6 N   2p0 :     0.21) (  21 C   1p0 :    -0.17) (  54 C   1p0 :     0.19)

               Molecular Orbital No. 233:
               --------------------------
               Occupation: 0.000 Energy:   -0.05120 a.u.
               (  18 C   1p0 :    -0.16) (  18 C   2p0 :    -0.18) (  19 C   1p0 :     0.16)
               (  19 C   2p0 :     0.18) (  20 C   1p0 :     0.17) (  20 C   2p0 :     0.19)
               (  21 C   1p0 :    -0.17) (  21 C   2p0 :    -0.19) (  51 C   1p0 :     0.20)
               (  51 C   2p0 :     0.24) (  53 C   1p0 :    -0.17) (  53 C   2p0 :    -0.21)
               (  84 C   1p0 :     0.20) (  84 C   2p0 :     0.25) (  86 C   1p0 :    -0.18)
               (  86 C   2p0 :    -0.22)

               Molecular Orbital No. 234:
               --------------------------
               Occupation: 0.000 Energy:   -0.02578 a.u.
               (  15 C   1p0 :    -0.17) (  15 C   2p0 :    -0.22) (  23 C   1p0 :     0.17)
               (  23 C   2p0 :     0.22) (  36 C   1p0 :     0.16) (  36 C   2p0 :     0.18)
               (  37 C   1p0 :    -0.17) (  37 C   2p0 :    -0.22) (  53 C   1p0 :     0.17)
               (  53 C   2p0 :     0.18) (  56 C   1p0 :    -0.15) (  56 C   2p0 :    -0.16)
               (  70 C   1p0 :     0.16) (  70 C   2p0 :     0.23) (  86 C   1p0 :    -0.17)
               (  86 C   2p0 :    -0.18)

               Molecular Orbital No. 235:
               --------------------------
               Occupation: 0.000 Energy:   -0.00042 a.u.
               (   8 C   3s  :     0.17) (  13 C   1p+1:    -0.15) (  13 C   1p-1:    -0.20)
               (  13 C   2p-1:    -0.16) (  14 C   1p0 :    -0.17) (  14 C   2p-1:     0.15)
               (  14 C   2p0 :    -0.22) (  25 C   1p0 :     0.16) (  25 C   2p0 :     0.20)
               (  26 C   1p+1:    -0.15) (  26 C   1p-1:     0.16) (  39 C   1p0 :    -0.19)
               (  39 C   2p0 :    -0.22) (  62 C   3s  :    -0.19) (  66 C   3s  :     0.17)
               (  72 C   1p0 :     0.18) (  72 C   2p0 :     0.20) ( 104 C   3s  :    -0.19)
               ( 122 C   3s  :     0.19) ( 130 C   3s  :    -0.19) ( 134 C   3s  :    -0.23)
               ( 136 H   2s  :     0.15)

               Molecular Orbital No. 236:
               --------------------------
               Occupation: 0.000 Energy:    0.00417 a.u.
               (   8 C   3s  :    -0.16) (  13 C   1p-1:     0.17) (  15 C   1p0 :    -0.15)
               (  15 C   2p0 :    -0.18) (  17 C   3s  :     0.18) (  18 C   2p+1:    -0.24)
               (  19 C   2p-1:    -0.27) (  20 C   2p-1:    -0.24) (  21 C   2p+1:     0.23)
               (  22 C   3s  :    -0.17) (  23 C   1p0 :    -0.16) (  23 C   2p0 :    -0.19)
               (  25 C   2p0 :     0.16) (  26 C   1p+1:    -0.17) (  26 C   1p-1:     0.17)
               (  37 C   2p0 :    -0.19) (  50 C   2p0 :    -0.17) (  70 C   2p0 :    -0.21)
               (  72 C   2p0 :     0.16) (  83 C   2p0 :    -0.17) ( 100 C   3s  :     0.18)
               ( 104 C   3s  :    -0.23) ( 134 C   3s  :     0.20)

               Molecular Orbital No. 237:
               --------------------------
               Occupation: 0.000 Energy:    0.00828 a.u.
               (   8 C   3s  :     0.21) (  13 C   1p+1:    -0.15) (  13 C   1p-1:    -0.20)
               (  13 C   2p+1:    -0.16) (  13 C   2p-1:    -0.15) (  26 C   1p+1:     0.17)
               (  26 C   1p-1:    -0.17) (  26 C   2p+1:     0.17) (  36 C   2p0 :     0.18)
               (  50 C   2p0 :    -0.16) (  51 C   2p0 :     0.16) (  54 C   2p0 :    -0.15)
               (  56 C   2p0 :     0.17) (  83 C   2p0 :    -0.15) (  84 C   2p0 :     0.15)
               ( 100 C   3s  :    -0.21) ( 104 C   3s  :     0.24) ( 134 C   3s  :    -0.24)
               ( 136 H   2s  :     0.15)


                                                Ground State Dipole Moment
                                               ----------------------------

                                   X   :         0.308184 a.u.         0.783327 Debye
                                   Y   :         0.064665 a.u.         0.164362 Debye
                                   Z   :        -0.090140 a.u.        -0.229112 Debye
                                 Total :         0.327543 a.u.         0.832531 Debye


                                            Linear Response EigenSolver Setup
                                           ===================================

                               Number of States                : 20
                               Max. Number of Iterations       : 150
                               Convergence Threshold           : 1.0e-04
                               ERI Screening Scheme            : Cauchy Schwarz + Density
                               ERI Screening Threshold         : 1.0e-12
                               Exchange-Correlation Functional : B3LYP
                               Molecular Grid Level            : 4

* Info * Molecular grid with 1558984 points generated in 2.52 sec.

* Info * Processing Fock builds... (batch size: 40)
* Info *   batch 1/1

* Info * 20 gerade trial vectors in reduced space
* Info * 20 ungerade trial vectors in reduced space

* Info * 56.80 MB of memory used for subspace procedure on the master node
* Info * 391.98 GB of memory available for the solver on the master node

               *** Iteration:   1 * Residuals (Max,Min): 4.17e-01 and 8.84e-02

               Excitation 1   :      0.13033266 Residual Norm: 0.19613854
               Excitation 2   :      0.13320099 Residual Norm: 0.22392055
               Excitation 3   :      0.14347647 Residual Norm: 0.11870081
               Excitation 4   :      0.14925556 Residual Norm: 0.16248920
               Excitation 5   :      0.15945472 Residual Norm: 0.31060978
               Excitation 6   :      0.16086205 Residual Norm: 0.19162686
               Excitation 7   :      0.16942790 Residual Norm: 0.15886175
               Excitation 8   :      0.17285311 Residual Norm: 0.18135310
               Excitation 9   :      0.17340954 Residual Norm: 0.20762713
               Excitation 10  :      0.17681249 Residual Norm: 0.17945445
               Excitation 11  :      0.17995680 Residual Norm: 0.08841273
               Excitation 12  :      0.18112263 Residual Norm: 0.11382604
               Excitation 13  :      0.18279847 Residual Norm: 0.15998199
               Excitation 14  :      0.18873528 Residual Norm: 0.15212015
               Excitation 15  :      0.19604375 Residual Norm: 0.33349769
               Excitation 16  :      0.19988548 Residual Norm: 0.33961500
               Excitation 17  :      0.20736174 Residual Norm: 0.31056260
               Excitation 18  :      0.20907844 Residual Norm: 0.32327910
               Excitation 19  :      0.21337144 Residual Norm: 0.39527896
               Excitation 20  :      0.21709980 Residual Norm: 0.41732457

* Info * Processing Fock builds... (batch size: 40)
* Info *   batch 1/1

* Info * 40 gerade trial vectors in reduced space
* Info * 40 ungerade trial vectors in reduced space

* Info * 94.66 MB of memory used for subspace procedure on the master node
* Info * 391.79 GB of memory available for the solver on the master node

               *** Iteration:   2 * Residuals (Max,Min): 1.72e-01 and 2.93e-02

               Excitation 1   :      0.12160922 Residual Norm: 0.04923387
               Excitation 2   :      0.12235354 Residual Norm: 0.04830939
               Excitation 3   :      0.14108655 Residual Norm: 0.02927080
               Excitation 4   :      0.14366434 Residual Norm: 0.04684290
               Excitation 5   :      0.14483891 Residual Norm: 0.03135435
               Excitation 6   :      0.14837241 Residual Norm: 0.05635861
               Excitation 7   :      0.16562054 Residual Norm: 0.04165709
               Excitation 8   :      0.16714102 Residual Norm: 0.04563057
               Excitation 9   :      0.16741056 Residual Norm: 0.04806691
               Excitation 10  :      0.17240281 Residual Norm: 0.03942706
               Excitation 11  :      0.17465187 Residual Norm: 0.04615649
               Excitation 12  :      0.17732385 Residual Norm: 0.05793698
               Excitation 13  :      0.17828199 Residual Norm: 0.05449660
               Excitation 14  :      0.17985246 Residual Norm: 0.06121538
               Excitation 15  :      0.18309612 Residual Norm: 0.06239554
               Excitation 16  :      0.18529496 Residual Norm: 0.06484046
               Excitation 17  :      0.18986076 Residual Norm: 0.05448292
               Excitation 18  :      0.19234592 Residual Norm: 0.06445423
               Excitation 19  :      0.19352345 Residual Norm: 0.17196434
               Excitation 20  :      0.19457679 Residual Norm: 0.13861418

* Info * Processing Fock builds... (batch size: 40)
* Info *   batch 1/1

* Info * 60 gerade trial vectors in reduced space
* Info * 60 ungerade trial vectors in reduced space

* Info * 132.52 MB of memory used for subspace procedure on the master node
* Info * 391.68 GB of memory available for the solver on the master node

               *** Iteration:   3 * Residuals (Max,Min): 5.22e-02 and 1.00e-02

               Excitation 1   :      0.12110998 Residual Norm: 0.01583366
               Excitation 2   :      0.12187471 Residual Norm: 0.01280313
               Excitation 3   :      0.14084117 Residual Norm: 0.01003671
               Excitation 4   :      0.14304447 Residual Norm: 0.01725390
               Excitation 5   :      0.14457468 Residual Norm: 0.01105887
               Excitation 6   :      0.14763306 Residual Norm: 0.02396478
               Excitation 7   :      0.16484555 Residual Norm: 0.02266424
               Excitation 8   :      0.16649337 Residual Norm: 0.02047214
               Excitation 9   :      0.16680486 Residual Norm: 0.01641009
               Excitation 10  :      0.17173446 Residual Norm: 0.01803541
               Excitation 11  :      0.17396045 Residual Norm: 0.01941097
               Excitation 12  :      0.17655273 Residual Norm: 0.01961186
               Excitation 13  :      0.17711393 Residual Norm: 0.02802955
               Excitation 14  :      0.17885719 Residual Norm: 0.02941240
               Excitation 15  :      0.18212395 Residual Norm: 0.02325323
               Excitation 16  :      0.18312916 Residual Norm: 0.04769070
               Excitation 17  :      0.18705386 Residual Norm: 0.05216528
               Excitation 18  :      0.18867704 Residual Norm: 0.03357612
               Excitation 19  :      0.19109590 Residual Norm: 0.04596829
               Excitation 20  :      0.19182244 Residual Norm: 0.02204692

* Info * Processing Fock builds... (batch size: 40)
* Info *   batch 1/1

* Info * 80 gerade trial vectors in reduced space
* Info * 80 ungerade trial vectors in reduced space

* Info * 170.38 MB of memory used for subspace procedure on the master node
* Info * 391.62 GB of memory available for the solver on the master node

               *** Iteration:   4 * Residuals (Max,Min): 3.51e-02 and 3.54e-03

               Excitation 1   :      0.12105119 Residual Norm: 0.00462055
               Excitation 2   :      0.12182749 Residual Norm: 0.00378566
               Excitation 3   :      0.14081529 Residual Norm: 0.00353598
               Excitation 4   :      0.14296513 Residual Norm: 0.00586438
               Excitation 5   :      0.14454075 Residual Norm: 0.00361273
               Excitation 6   :      0.14748550 Residual Norm: 0.00723494
               Excitation 7   :      0.16468271 Residual Norm: 0.00817131
               Excitation 8   :      0.16637815 Residual Norm: 0.00751213
               Excitation 9   :      0.16669807 Residual Norm: 0.00630764
               Excitation 10  :      0.17161972 Residual Norm: 0.00761473
               Excitation 11  :      0.17385746 Residual Norm: 0.00790401
               Excitation 12  :      0.17641975 Residual Norm: 0.00752459
               Excitation 13  :      0.17679160 Residual Norm: 0.01329193
               Excitation 14  :      0.17864550 Residual Norm: 0.00920918
               Excitation 15  :      0.18196125 Residual Norm: 0.01075848
               Excitation 16  :      0.18210665 Residual Norm: 0.02146274
               Excitation 17  :      0.18613490 Residual Norm: 0.01841145
               Excitation 18  :      0.18828820 Residual Norm: 0.01671084
               Excitation 19  :      0.18966636 Residual Norm: 0.03514442
               Excitation 20  :      0.19153276 Residual Norm: 0.00978198

* Info * Processing Fock builds... (batch size: 40)
* Info *   batch 1/1

* Info * 100 gerade trial vectors in reduced space
* Info * 100 ungerade trial vectors in reduced space

* Info * 208.25 MB of memory used for subspace procedure on the master node
* Info * 391.56 GB of memory available for the solver on the master node

               *** Iteration:   5 * Residuals (Max,Min): 2.34e-02 and 8.46e-04

               Excitation 1   :      0.12104734 Residual Norm: 0.00120012
               Excitation 2   :      0.12182489 Residual Norm: 0.00103561
               Excitation 3   :      0.14081334 Residual Norm: 0.00084626
               Excitation 4   :      0.14295871 Residual Norm: 0.00194089
               Excitation 5   :      0.14453748 Residual Norm: 0.00093716
               Excitation 6   :      0.14747427 Residual Norm: 0.00225384
               Excitation 7   :      0.16466573 Residual Norm: 0.00269901
               Excitation 8   :      0.16636631 Residual Norm: 0.00232648
               Excitation 9   :      0.16668836 Residual Norm: 0.00261626
               Excitation 10  :      0.17160051 Residual Norm: 0.00299483
               Excitation 11  :      0.17384023 Residual Norm: 0.00307246
               Excitation 12  :      0.17640570 Residual Norm: 0.00287375
               Excitation 13  :      0.17673281 Residual Norm: 0.00515117
               Excitation 14  :      0.17862012 Residual Norm: 0.00350815
               Excitation 15  :      0.18187683 Residual Norm: 0.00819055
               Excitation 16  :      0.18197389 Residual Norm: 0.00505157
               Excitation 17  :      0.18598132 Residual Norm: 0.00791368
               Excitation 18  :      0.18817922 Residual Norm: 0.00954742
               Excitation 19  :      0.18891624 Residual Norm: 0.02339161
               Excitation 20  :      0.19148178 Residual Norm: 0.00659184

* Info * Processing Fock builds... (batch size: 40)
* Info *   batch 1/1

* Info * 120 gerade trial vectors in reduced space
* Info * 120 ungerade trial vectors in reduced space

* Info * 246.11 MB of memory used for subspace procedure on the master node
* Info * 393.74 GB of memory available for the solver on the master node

               *** Iteration:   6 * Residuals (Max,Min): 9.03e-03 and 2.37e-04

               Excitation 1   :      0.12104708 Residual Norm: 0.00028887
               Excitation 2   :      0.12182469 Residual Norm: 0.00023679
               Excitation 3   :      0.14081321 Residual Norm: 0.00026049
               Excitation 4   :      0.14295802 Residual Norm: 0.00044913
               Excitation 5   :      0.14453729 Residual Norm: 0.00028239
               Excitation 6   :      0.14747323 Residual Norm: 0.00068851
               Excitation 7   :      0.16466415 Residual Norm: 0.00083148
               Excitation 8   :      0.16636510 Residual Norm: 0.00070186
               Excitation 9   :      0.16668686 Residual Norm: 0.00079593
               Excitation 10  :      0.17159828 Residual Norm: 0.00097736
               Excitation 11  :      0.17383776 Residual Norm: 0.00093133
               Excitation 12  :      0.17640314 Residual Norm: 0.00126852
               Excitation 13  :      0.17672554 Residual Norm: 0.00194139
               Excitation 14  :      0.17861712 Residual Norm: 0.00138356
               Excitation 15  :      0.18185966 Residual Norm: 0.00327673
               Excitation 16  :      0.18196817 Residual Norm: 0.00182236
               Excitation 17  :      0.18596447 Residual Norm: 0.00313921
               Excitation 18  :      0.18815306 Residual Norm: 0.00388805
               Excitation 19  :      0.18876042 Residual Norm: 0.00902828
               Excitation 20  :      0.19146331 Residual Norm: 0.00455100

* Info * Processing Fock builds... (batch size: 40)
* Info *   batch 1/1

* Info * 140 gerade trial vectors in reduced space
* Info * 140 ungerade trial vectors in reduced space

* Info * 283.97 MB of memory used for subspace procedure on the master node
* Info * 393.68 GB of memory available for the solver on the master node

               *** Iteration:   7 * Residuals (Max,Min): 4.26e-03 and 6.59e-05

               Excitation 1   :      0.12104706 Residual Norm: 0.00007394   converged
               Excitation 2   :      0.12182468 Residual Norm: 0.00006593   converged
               Excitation 3   :      0.14081320 Residual Norm: 0.00007725   converged
               Excitation 4   :      0.14295798 Residual Norm: 0.00012069
               Excitation 5   :      0.14453728 Residual Norm: 0.00007750   converged
               Excitation 6   :      0.14747314 Residual Norm: 0.00020056
               Excitation 7   :      0.16466402 Residual Norm: 0.00021010
               Excitation 8   :      0.16636499 Residual Norm: 0.00021249
               Excitation 9   :      0.16668670 Residual Norm: 0.00024658
               Excitation 10  :      0.17159806 Residual Norm: 0.00032417
               Excitation 11  :      0.17383753 Residual Norm: 0.00034740
               Excitation 12  :      0.17640272 Residual Norm: 0.00050313
               Excitation 13  :      0.17672461 Residual Norm: 0.00071376
               Excitation 14  :      0.17861661 Residual Norm: 0.00049523
               Excitation 15  :      0.18185711 Residual Norm: 0.00105765
               Excitation 16  :      0.18196731 Residual Norm: 0.00069000
               Excitation 17  :      0.18596131 Residual Norm: 0.00126685
               Excitation 18  :      0.18814862 Residual Norm: 0.00160995
               Excitation 19  :      0.18873263 Residual Norm: 0.00425947
               Excitation 20  :      0.19145566 Residual Norm: 0.00242505

* Info * Processing Fock builds... (batch size: 32)
* Info *   batch 1/1

* Info * 156 gerade trial vectors in reduced space
* Info * 156 ungerade trial vectors in reduced space

* Info * 314.26 MB of memory used for subspace procedure on the master node
* Info * 393.68 GB of memory available for the solver on the master node

               *** Iteration:   8 * Residuals (Max,Min): 1.48e-03 and 3.50e-05

               Excitation 1   :      0.12104706 Residual Norm: 0.00005912   converged
               Excitation 2   :      0.12182468 Residual Norm: 0.00005207   converged
               Excitation 3   :      0.14081320 Residual Norm: 0.00004370   converged
               Excitation 4   :      0.14295798 Residual Norm: 0.00003501   converged
               Excitation 5   :      0.14453728 Residual Norm: 0.00005344   converged
               Excitation 6   :      0.14747313 Residual Norm: 0.00005315   converged
               Excitation 7   :      0.16466401 Residual Norm: 0.00005383   converged
               Excitation 8   :      0.16636498 Residual Norm: 0.00006222   converged
               Excitation 9   :      0.16668669 Residual Norm: 0.00007091   converged
               Excitation 10  :      0.17159804 Residual Norm: 0.00007988   converged
               Excitation 11  :      0.17383750 Residual Norm: 0.00012101
               Excitation 12  :      0.17640266 Residual Norm: 0.00018794
               Excitation 13  :      0.17672448 Residual Norm: 0.00023439
               Excitation 14  :      0.17861655 Residual Norm: 0.00017081
               Excitation 15  :      0.18185684 Residual Norm: 0.00034546
               Excitation 16  :      0.18196719 Residual Norm: 0.00021212
               Excitation 17  :      0.18596088 Residual Norm: 0.00047638
               Excitation 18  :      0.18814793 Residual Norm: 0.00066457
               Excitation 19  :      0.18872753 Residual Norm: 0.00148306
               Excitation 20  :      0.19145379 Residual Norm: 0.00099349

* Info * Processing Fock builds... (batch size: 20)
* Info *   batch 1/1

* Info * 166 gerade trial vectors in reduced space
* Info * 166 ungerade trial vectors in reduced space

* Info * 333.19 MB of memory used for subspace procedure on the master node
* Info * 393.66 GB of memory available for the solver on the master node

               *** Iteration:   9 * Residuals (Max,Min): 5.78e-04 and 2.81e-05

               Excitation 1   :      0.12104706 Residual Norm: 0.00005373   converged
               Excitation 2   :      0.12182468 Residual Norm: 0.00004951   converged
               Excitation 3   :      0.14081320 Residual Norm: 0.00004097   converged
               Excitation 4   :      0.14295798 Residual Norm: 0.00002942   converged
               Excitation 5   :      0.14453728 Residual Norm: 0.00005204   converged
               Excitation 6   :      0.14747313 Residual Norm: 0.00002807   converged
               Excitation 7   :      0.16466401 Residual Norm: 0.00003744   converged
               Excitation 8   :      0.16636498 Residual Norm: 0.00004496   converged
               Excitation 9   :      0.16668669 Residual Norm: 0.00004637   converged
               Excitation 10  :      0.17159803 Residual Norm: 0.00005108   converged
               Excitation 11  :      0.17383750 Residual Norm: 0.00003716   converged
               Excitation 12  :      0.17640265 Residual Norm: 0.00005854   converged
               Excitation 13  :      0.17672447 Residual Norm: 0.00007358   converged
               Excitation 14  :      0.17861654 Residual Norm: 0.00006098   converged
               Excitation 15  :      0.18185681 Residual Norm: 0.00011412
               Excitation 16  :      0.18196717 Residual Norm: 0.00007418   converged
               Excitation 17  :      0.18596082 Residual Norm: 0.00018033
               Excitation 18  :      0.18814780 Residual Norm: 0.00026941
               Excitation 19  :      0.18872687 Residual Norm: 0.00057769
               Excitation 20  :      0.19145348 Residual Norm: 0.00046677

* Info * Processing Fock builds... (batch size: 10)
* Info *   batch 1/1

* Info * 171 gerade trial vectors in reduced space
* Info * 171 ungerade trial vectors in reduced space

* Info * 342.66 MB of memory used for subspace procedure on the master node
* Info * 393.65 GB of memory available for the solver on the master node

               *** Iteration:   10 * Residuals (Max,Min): 2.64e-04 and 2.75e-05

               Excitation 1   :      0.12104706 Residual Norm: 0.00005216   converged
               Excitation 2   :      0.12182468 Residual Norm: 0.00004820   converged
               Excitation 3   :      0.14081320 Residual Norm: 0.00004080   converged
               Excitation 4   :      0.14295798 Residual Norm: 0.00002879   converged
               Excitation 5   :      0.14453728 Residual Norm: 0.00005085   converged
               Excitation 6   :      0.14747313 Residual Norm: 0.00002750   converged
               Excitation 7   :      0.16466401 Residual Norm: 0.00003436   converged
               Excitation 8   :      0.16636498 Residual Norm: 0.00004216   converged
               Excitation 9   :      0.16668669 Residual Norm: 0.00004272   converged
               Excitation 10  :      0.17159803 Residual Norm: 0.00004922   converged
               Excitation 11  :      0.17383750 Residual Norm: 0.00003073   converged
               Excitation 12  :      0.17640265 Residual Norm: 0.00004903   converged
               Excitation 13  :      0.17672447 Residual Norm: 0.00005056   converged
               Excitation 14  :      0.17861654 Residual Norm: 0.00003833   converged
               Excitation 15  :      0.18185681 Residual Norm: 0.00004298   converged
               Excitation 16  :      0.18196717 Residual Norm: 0.00005415   converged
               Excitation 17  :      0.18596082 Residual Norm: 0.00006091   converged
               Excitation 18  :      0.18814778 Residual Norm: 0.00009800   converged
               Excitation 19  :      0.18872678 Residual Norm: 0.00018875
               Excitation 20  :      0.19145341 Residual Norm: 0.00026379

* Info * Processing Fock builds... (batch size: 4)
* Info *   batch 1/1

* Info * 173 gerade trial vectors in reduced space
* Info * 173 ungerade trial vectors in reduced space

* Info * 346.44 MB of memory used for subspace procedure on the master node
* Info * 393.65 GB of memory available for the solver on the master node

               *** Iteration:   11 * Residuals (Max,Min): 1.17e-04 and 2.74e-05

               Excitation 1   :      0.12104706 Residual Norm: 0.00005212   converged
               Excitation 2   :      0.12182468 Residual Norm: 0.00004818   converged
               Excitation 3   :      0.14081320 Residual Norm: 0.00004076   converged
               Excitation 4   :      0.14295798 Residual Norm: 0.00002878   converged
               Excitation 5   :      0.14453728 Residual Norm: 0.00005020   converged
               Excitation 6   :      0.14747313 Residual Norm: 0.00002742   converged
               Excitation 7   :      0.16466401 Residual Norm: 0.00003423   converged
               Excitation 8   :      0.16636498 Residual Norm: 0.00004037   converged
               Excitation 9   :      0.16668669 Residual Norm: 0.00004192   converged
               Excitation 10  :      0.17159803 Residual Norm: 0.00004912   converged
               Excitation 11  :      0.17383750 Residual Norm: 0.00003059   converged
               Excitation 12  :      0.17640265 Residual Norm: 0.00004878   converged
               Excitation 13  :      0.17672447 Residual Norm: 0.00004794   converged
               Excitation 14  :      0.17861654 Residual Norm: 0.00003716   converged
               Excitation 15  :      0.18185681 Residual Norm: 0.00004279   converged
               Excitation 16  :      0.18196717 Residual Norm: 0.00005217   converged
               Excitation 17  :      0.18596082 Residual Norm: 0.00005142   converged
               Excitation 18  :      0.18814778 Residual Norm: 0.00009472   converged
               Excitation 19  :      0.18872677 Residual Norm: 0.00007781   converged
               Excitation 20  :      0.19145339 Residual Norm: 0.00011689

* Info * Processing Fock builds... (batch size: 2)
* Info *   batch 1/1

* Info * 174 gerade trial vectors in reduced space
* Info * 174 ungerade trial vectors in reduced space

* Info * 348.34 MB of memory used for subspace procedure on the master node
* Info * 393.64 GB of memory available for the solver on the master node

               *** Iteration:   12 * Residuals (Max,Min): 9.46e-05 and 2.74e-05

               Excitation 1   :      0.12104706 Residual Norm: 0.00005199   converged
               Excitation 2   :      0.12182468 Residual Norm: 0.00004825   converged
               Excitation 3   :      0.14081320 Residual Norm: 0.00004076   converged
               Excitation 4   :      0.14295798 Residual Norm: 0.00002878   converged
               Excitation 5   :      0.14453728 Residual Norm: 0.00004969   converged
               Excitation 6   :      0.14747313 Residual Norm: 0.00002739   converged
               Excitation 7   :      0.16466401 Residual Norm: 0.00003413   converged
               Excitation 8   :      0.16636498 Residual Norm: 0.00004031   converged
               Excitation 9   :      0.16668669 Residual Norm: 0.00004192   converged
               Excitation 10  :      0.17159803 Residual Norm: 0.00004912   converged
               Excitation 11  :      0.17383750 Residual Norm: 0.00003058   converged
               Excitation 12  :      0.17640265 Residual Norm: 0.00004846   converged
               Excitation 13  :      0.17672447 Residual Norm: 0.00004792   converged
               Excitation 14  :      0.17861654 Residual Norm: 0.00003715   converged
               Excitation 15  :      0.18185681 Residual Norm: 0.00004239   converged
               Excitation 16  :      0.18196717 Residual Norm: 0.00005216   converged
               Excitation 17  :      0.18596082 Residual Norm: 0.00005112   converged
               Excitation 18  :      0.18814778 Residual Norm: 0.00009461   converged
               Excitation 19  :      0.18872677 Residual Norm: 0.00007415   converged
               Excitation 20  :      0.19145338 Residual Norm: 0.00005861   converged

* Info * Checkpoint written to file: ecd-benchmark.rsp.h5

               *** Linear response converged in 12 iterations. Time: 7492.90 sec


* Info * Response solution vectors written to file: ecd-benchmark.rsp.solutions.h5

               Electric Transition Dipole Moments (dipole length, a.u.)
               --------------------------------------------------------
                                                X            Y            Z
               Excited State    S1:      1.035143    -0.336998     0.044327
               Excited State    S2:      0.127529     1.683542    -0.179197
               Excited State    S3:      0.773151     0.013847     0.012873
               Excited State    S4:     -0.044020    -0.098343    -0.528998
               Excited State    S5:     -0.063487    -0.818716     0.167652
               Excited State    S6:     -1.741110    -0.066965     0.014258
               Excited State    S7:     -0.015688    -0.333758    -0.061533
               Excited State    S8:      0.406881    -0.238272     0.126888
               Excited State    S9:     -0.108239    -0.755694     0.270263
               Excited State   S10:      0.015712     0.414967    -0.551259
               Excited State   S11:      1.427443     0.022343    -0.026686
               Excited State   S12:      0.147740    -0.060704    -0.088970
               Excited State   S13:     -0.017318    -0.459320    -0.634134
               Excited State   S14:     -0.457829    -0.036271    -0.118951
               Excited State   S15:     -0.405447     0.035586     0.361811
               Excited State   S16:      0.826665     0.075703     0.165087
               Excited State   S17:      0.048622     0.630348    -0.318267
               Excited State   S18:      0.705558     0.012076     0.019932
               Excited State   S19:     -0.699622    -0.089530    -0.010895
               Excited State   S20:     -0.101558     0.011712     0.023749

               Electric Transition Dipole Moments (dipole velocity, a.u.)
               ----------------------------------------------------------
                                                X            Y            Z
               Excited State    S1:      1.025578    -0.335025     0.044634
               Excited State    S2:      0.126796     1.673673    -0.182038
               Excited State    S3:      0.750473     0.011150     0.013623
               Excited State    S4:     -0.042190    -0.128651    -0.516061
               Excited State    S5:     -0.061025    -0.824293     0.172006
               Excited State    S6:     -1.711012    -0.064370     0.013881
               Excited State    S7:     -0.017762    -0.311199    -0.062383
               Excited State    S8:      0.373165    -0.232901     0.128696
               Excited State    S9:     -0.097198    -0.732830     0.274192
               Excited State   S10:      0.014825     0.403728    -0.545118
               Excited State   S11:      1.416372     0.024550    -0.026639
               Excited State   S12:      0.164915    -0.055498    -0.087551
               Excited State   S13:     -0.024433    -0.431542    -0.609345
               Excited State   S14:     -0.429232    -0.030912    -0.116916
               Excited State   S15:     -0.395097     0.015438     0.355448
               Excited State   S16:      0.817385     0.066528     0.161981
               Excited State   S17:      0.047981     0.600552    -0.315363
               Excited State   S18:      0.694609     0.012679     0.019765
               Excited State   S19:     -0.678247    -0.087177    -0.011693
               Excited State   S20:     -0.099262     0.005479     0.019690

               Magnetic Transition Dipole Moments (a.u.)
               -----------------------------------------
                                                X            Y            Z
               Excited State    S1:     -0.164393     0.005413     0.251393
               Excited State    S2:     -0.080372     0.003622    -1.033917
               Excited State    S3:     -0.006360     0.011232     0.029025
               Excited State    S4:      0.010611    -0.054291    -0.867530
               Excited State    S5:      0.027377    -0.016722     0.358730
               Excited State    S6:      0.098316    -0.024990    -0.004231
               Excited State    S7:      0.015166    -0.070214     0.277639
               Excited State    S8:      0.019181    -0.018495     0.386395
               Excited State    S9:      0.022914    -0.053748     0.978406
               Excited State   S10:     -0.008009    -0.004069    -0.935445
               Excited State   S11:     -0.309603     0.020507     0.001693
               Excited State   S12:      0.143313     0.016584    -0.054912
               Excited State   S13:     -0.006687     0.062979    -0.677433
               Excited State   S14:      0.235668     0.002379    -0.144468
               Excited State   S15:      0.108944     0.124018     0.619367
               Excited State   S16:     -0.233276     0.059235     0.270629
               Excited State   S17:     -0.038655    -0.079484    -1.150627
               Excited State   S18:     -0.117578     0.016422     0.072388
               Excited State   S19:      0.005794    -0.035423     0.024762
               Excited State   S20:      0.037021    -0.187173     0.255529

               One-Photon Absorption
               ---------------------
               Excited State    S1:      0.12104706 a.u.      3.29386 eV    Osc.Str.    0.0958
               Excited State    S2:      0.12182468 a.u.      3.31502 eV    Osc.Str.    0.2341
               Excited State    S3:      0.14081320 a.u.      3.83172 eV    Osc.Str.    0.0561
               Excited State    S4:      0.14295798 a.u.      3.89008 eV    Osc.Str.    0.0278
               Excited State    S5:      0.14453728 a.u.      3.93306 eV    Osc.Str.    0.0677
               Excited State    S6:      0.14747313 a.u.      4.01295 eV    Osc.Str.    0.2985
               Excited State    S7:      0.16466401 a.u.      4.48074 eV    Osc.Str.    0.0127
               Excited State    S8:      0.16636498 a.u.      4.52702 eV    Osc.Str.    0.0264
               Excited State    S9:      0.16668669 a.u.      4.53578 eV    Osc.Str.    0.0729
               Excited State   S10:      0.17159803 a.u.      4.66942 eV    Osc.Str.    0.0545
               Excited State   S11:      0.17383750 a.u.      4.73036 eV    Osc.Str.    0.2363
               Excited State   S12:      0.17640265 a.u.      4.80016 eV    Osc.Str.    0.0039
               Excited State   S13:      0.17672447 a.u.      4.80892 eV    Osc.Str.    0.0723
               Excited State   S14:      0.17861654 a.u.      4.86040 eV    Osc.Str.    0.0268
               Excited State   S15:      0.18185681 a.u.      4.94858 eV    Osc.Str.    0.0360
               Excited State   S16:      0.18196717 a.u.      4.95158 eV    Osc.Str.    0.0869
               Excited State   S17:      0.18596082 a.u.      5.06025 eV    Osc.Str.    0.0621
               Excited State   S18:      0.18814778 a.u.      5.11976 eV    Osc.Str.    0.0625
               Excited State   S19:      0.18872677 a.u.      5.13552 eV    Osc.Str.    0.0626
               Excited State   S20:      0.19145338 a.u.      5.20971 eV    Osc.Str.    0.0014

               Electronic Circular Dichroism
               -----------------------------
               Excited State    S1:     Rot.Str.     -0.159190 a.u.   -75.0492 [10**(-40) cgs]
               Excited State    S2:     Rot.Str.      0.184083 a.u.    86.7846 [10**(-40) cgs]
               Excited State    S3:     Rot.Str.     -0.004252 a.u.    -2.0048 [10**(-40) cgs]
               Excited State    S4:     Rot.Str.      0.454235 a.u.   214.1463 [10**(-40) cgs]
               Excited State    S5:     Rot.Str.      0.073817 a.u.    34.8004 [10**(-40) cgs]
               Excited State    S6:     Rot.Str.     -0.166670 a.u.   -78.5756 [10**(-40) cgs]
               Excited State    S7:     Rot.Str.      0.004261 a.u.     2.0089 [10**(-40) cgs]
               Excited State    S8:     Rot.Str.      0.061193 a.u.    28.8489 [10**(-40) cgs]
               Excited State    S9:     Rot.Str.      0.305432 a.u.   143.9942 [10**(-40) cgs]
               Excited State   S10:     Rot.Str.      0.508167 a.u.   239.5720 [10**(-40) cgs]
               Excited State   S11:     Rot.Str.     -0.438055 a.u.  -206.5183 [10**(-40) cgs]
               Excited State   S12:     Rot.Str.      0.027522 a.u.    12.9749 [10**(-40) cgs]
               Excited State   S13:     Rot.Str.      0.385776 a.u.   181.8716 [10**(-40) cgs]
               Excited State   S14:     Rot.Str.     -0.084339 a.u.   -39.7612 [10**(-40) cgs]
               Excited State   S15:     Rot.Str.      0.179024 a.u.    84.3998 [10**(-40) cgs]
               Excited State   S16:     Rot.Str.     -0.142899 a.u.   -67.3687 [10**(-40) cgs]
               Excited State   S17:     Rot.Str.      0.313276 a.u.   147.6918 [10**(-40) cgs]
               Excited State   S18:     Rot.Str.     -0.080032 a.u.   -37.7305 [10**(-40) cgs]
               Excited State   S19:     Rot.Str.     -0.001131 a.u.    -0.5333 [10**(-40) cgs]
               Excited State   S20:     Rot.Str.      0.000331 a.u.     0.1561 [10**(-40) cgs]

               Character of excitations:

               Excited state 1
               ---------------
               HOMO     -> LUMO         0.9598

               Excited state 2
               ---------------
               HOMO-1   -> LUMO         0.9687

               Excited state 3
               ---------------
               HOMO-2   -> LUMO         0.8935
               HOMO-1   -> LUMO+1       0.3826

               Excited state 4
               ---------------
               HOMO-3   -> LUMO         0.8053
               HOMO     -> LUMO+1      -0.5091

               Excited state 5
               ---------------
               HOMO     -> LUMO+1      -0.7608
               HOMO-3   -> LUMO        -0.5628
               HOMO-1   -> LUMO+1      -0.2980

               Excited state 6
               ---------------
               HOMO-1   -> LUMO+1       0.8135
               HOMO-2   -> LUMO        -0.3800
               HOMO     -> LUMO+1      -0.2867

               Excited state 7
               ---------------
               HOMO-2   -> LUMO+1      -0.7513
               HOMO     -> LUMO+2       0.5590
               HOMO-1   -> LUMO+2       0.2059

               Excited state 8
               ---------------
               HOMO-3   -> LUMO+1      -0.7150
               HOMO-1   -> LUMO+2      -0.4344
               HOMO-4   -> LUMO         0.2997
               HOMO     -> LUMO+2       0.2704
               HOMO     -> LUMO+3      -0.2320

               Excited state 9
               ---------------
               HOMO-4   -> LUMO         0.8538
               HOMO-3   -> LUMO+1       0.2929
               HOMO-2   -> LUMO+1       0.2179
               HOMO-1   -> LUMO+2       0.2174
               HOMO-1   -> LUMO+3       0.2078

               Excited state 10
               ----------------
               HOMO     -> LUMO+2      -0.6463
               HOMO-2   -> LUMO+1      -0.5091
               HOMO-1   -> LUMO+2      -0.2989
               HOMO-1   -> LUMO+3       0.2589
               HOMO-1   -> LUMO+4       0.2569

               Excited state 11
               ----------------
               HOMO-1   -> LUMO+2       0.5571
               HOMO-3   -> LUMO+1      -0.4949
               HOMO     -> LUMO+3       0.3969
               HOMO-5   -> LUMO        -0.2479
               HOMO     -> LUMO+2      -0.2425

               Excited state 12
               ----------------
               HOMO     -> LUMO+3       0.7902
               HOMO-1   -> LUMO+2      -0.4957

               Excited state 13
               ----------------
               HOMO-1   -> LUMO+3      -0.8282
               HOMO-1   -> LUMO+4       0.2440
               HOMO     -> LUMO+3       0.2352
               HOMO     -> LUMO+4      -0.2214

               Excited state 14
               ----------------
               HOMO     -> LUMO+4       0.8248
               HOMO-1   -> LUMO+4       0.3562
               HOMO-1   -> LUMO+5      -0.2095

               Excited state 15
               ----------------
               HOMO-1   -> LUMO+4       0.7306
               HOMO-5   -> LUMO        -0.3521
               HOMO     -> LUMO+4      -0.3190
               HOMO     -> LUMO+2       0.2241

               Excited state 16
               ----------------
               HOMO-5   -> LUMO         0.8519
               HOMO-1   -> LUMO+4       0.3388

               Excited state 17
               ----------------
               HOMO     -> LUMO+5       0.8725
               HOMO-1   -> LUMO+5       0.3310

               Excited state 18
               ----------------
               HOMO-1   -> LUMO+5      -0.8159
               HOMO     -> LUMO+5       0.3086
               HOMO-2   -> LUMO+3       0.2908

               Excited state 19
               ----------------
               HOMO-4   -> LUMO+1      -0.6060
               HOMO-2   -> LUMO+3      -0.3998
               HOMO-3   -> LUMO+2       0.3826
               HOMO     -> LUMO+6       0.3477
               HOMO     -> LUMO+7      -0.2252
               HOMO-1   -> LUMO+6       0.2183

               Excited state 20
               ----------------
               HOMO-2   -> LUMO+2      -0.8701
               HOMO     -> LUMO+7       0.2932
               HOMO-1   -> LUMO+6       0.2374

!========================================================================================================================!
!                               VeloxChem execution completed at Wed Nov  9 22:45:53 2022.                               !
!========================================================================================================================!
!                                          Total execution time is 7991.92 sec.                                          !
!========================================================================================================================!
!                     Rinkevicius, Z.; Li, X.; Vahtras, O.; Ahmadzadeh, K.; Brand, M.; Ringholm, M.;                     !
!                              List, N. H.; Scheurer, M.; Scott, M.; Dreuw, A.; Norman, P.                               !
!                     VeloxChem: A Python-driven Density-functional Theory Program for Spectroscopy                      !
!                                Simulations in High-performance Computing Environments.                                 !
!                                       WIREs Comput Mol Sci 2020, 10 (5), e1457.                                        !
!========================================================================================================================!
```
