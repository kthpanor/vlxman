(sec:nlo)=
# Multi-photon interactions

(sec:tpa)=
## Two-photon absorption

(sec:cpp_qrf)=
## General quadratic response functions

A general quadratic response function

$$
\langle\langle \hat{\Omega}; \hat{V}_1, \hat{V}_2 
\rangle \rangle_{\omega_1, \omega_2}^\gamma
$$

can be requested, referring to the linear response of the molecular property associated with $\hat{\Omega}$ due to the perturbation associated with $\hat{V}_1$ and $\hat{V}_2$ oscillating with the angular frequencies $\omega_1$ and $\omega_2$, respectively. The damping term $\gamma$ is associated with the inverse lifetime of excited states.

**Python script**

```
import veloxchem as vlx

molecule = vlx.Molecule.read_xyz_string("""4
Hydrogen peroxide
O  -0.65564532 -0.06106286 -0.03621403
O   0.65564532  0.06106286 -0.03621403
H  -0.97628735  0.65082652  0.57474201
H   0.97628735 -0.65082652  0.57474201
""")

basis = vlx.MolecularBasis.read(molecule, "def2-svpd", ostream=None)

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

crf_drv = vlx.QuadraticResponseDriver()

crf_drv.a_operator = "electric dipole"
crf_drv.b_operator = "magnetic dipole"
crf_drv.c_operator = "electric dipole"

# available operators
#qrf.b_operator = "electric dipole"
#qrf.b_operator = "magnetic dipole"
#qrf.b_operator = "linear momentum"
#qrf.b_operator = "angular momentum"

crf_drv.a_component = "z"
crf_drv.b_component = "x"
crf_drv.c_component = "x"

crf_drv.b_frequencies = [0.0656, 0.1312]
crf_drv.c_frequencies = [0.0656, 0.1312]

crf_drv.damping = 0.004556  # 1000 cm-1

crf_results = crf_drv.compute(molecule, basis, scf_results)
```

(sec:cpp_crf)=
## General cubic response functions

A general cubic response function

$$
\langle\langle \hat{\Omega}; \hat{V}_1, \hat{V}_2, \hat{V}_3 
\rangle \rangle_{\omega_1, \omega_2, \omega_3}^\gamma
$$

can be requested, referring to the linear response of the molecular property associated with $\hat{\Omega}$ due to the perturbation associated with $\hat{V}_1$, $\hat{V}_2$, and $\hat{V}_3$ oscillating with the angular frequencies $\omega_1$, $\omega_2$, and $\omega_3$, respectively. The damping term $\gamma$ is associated with the inverse lifetime of excited states.

**Python script**

```
import veloxchem as vlx

molecule = vlx.Molecule.read_xyz_string("""4
Hydrogen peroxide
O  -0.65564532 -0.06106286 -0.03621403
O   0.65564532  0.06106286 -0.03621403
H  -0.97628735  0.65082652  0.57474201
H   0.97628735 -0.65082652  0.57474201
""")

basis = vlx.MolecularBasis.read(molecule, "def2-svpd", ostream=None)

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

crf_drv = vlx.CubicResponseDriver()

crf_drv.a_operator = "electric dipole"
crf_drv.b_operator = "magnetic dipole"
crf_drv.c_operator = "electric dipole"
crf_drv.d_operator = "electric dipole"

# available operators
#crf.b_operator = "electric dipole"
#crf.b_operator = "magnetic dipole"
#crf.b_operator = "linear momentum"
#crf.b_operator = "angular momentum"

crf_drv.a_component = "z"
crf_drv.b_component = "x"
crf_drv.c_component = "x"
crf_drv.d_component = "z"

crf_drv.b_frequencies = [0.0656, 0.1312]
crf_drv.c_frequencies = [0.0656, 0.1312]
crf_drv.d_frequencies = [0.0656, 0.1312]

crf_drv.damping = 0.004556  # 1000 cm-1

crf_results = crf_drv.compute(molecule, basis, scf_results)
```
