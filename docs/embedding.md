# Environment

## Localized properties

### ESP charges

Since there is no unique definition for partial charges and no corresponding physical observable, they can be assigned in several ways, such as being derived from the quantum mechanical electrostatic potential

\begin{equation*}
V(\boldsymbol{r}) = 
\sum_{I}
\frac{Z_I e}{4\pi\varepsilon_0 |\boldsymbol{r}-\mathrm{\textbf{R}}_I|} - e
\sum_{\mu,\nu}
D_{\mu\nu}
\int 
\frac{
\phi_\mu^*(\boldsymbol{r}')\phi_\nu(\boldsymbol{r}')
}{
4\pi\varepsilon_0
|\boldsymbol{r}-\boldsymbol{r}'|
}
d^3\boldsymbol{r}'
\end{equation*}

that can be replaced with a potential caused by the partial charges:

\begin{equation*}
\widetilde{V}(\boldsymbol{r}) = 
\sum_{I}
\frac{
q_I
}{
4\pi\varepsilon_0
|\boldsymbol{r}-\textbf{R}_I|
}
\end{equation*}

The Merz–Kollman scheme minimizes the squared norm difference between these two quantities evaluated on a set of grid points in the solvent-accessible region of the molecule with respect to variations in the partial charges and a constraint of a conservation of the total molecular charge – the grid points are distributed on successive layers of scaled van der Waals surfaces. This measure is referred to as the figure-of-merit

\begin{equation*}
\chi_{\mathrm{esp}}^2 = \sum_a \bigl(V(\boldsymbol{r}_a) - \widetilde{V}(\boldsymbol{r}_a)\bigl)^2
\end{equation*}

The resulting electrostatic potential (ESP) charges are obtained by solving the equation

\begin{equation*}
\mathrm{\textbf{A}} \, \mathrm{\textbf{q}} = \mathrm{\textbf{b}}
\end{equation*}

where

\begin{equation*}
A_{JI} =
\frac{1}{4\pi\varepsilon_0}
\sum_{a} \frac{1}{r_{aI}r_{aJ}}
\end{equation*}

and

\begin{equation*}
b_J = \sum_{a} \frac{V_a}{r_{aJ}}
\end{equation*}

The ESP charges are detemined with VeloxChem with use of an input file as below

```
@jobs
task: esp charges
@end

@method settings
basis: 6-31g
@end

@esp charges
number layers: 5
density: 10.0
@end

@molecule
charge: 0
multiplicity: 1
units: au
xyz:  
...
@end
```

or in a Jupyter notebook according to

```
import veloxchem as vlx

mol_str = """
...
"""

molecule = vlx.Molecule.read_str(mol_str, units='au')
basis = vlx.MolecularBasis.read(molecule, '6-31g')

esp_drv = vlx.RespChargesDriver()
esp_drv.update_settings({
    'number_layers': 5,
    'density': 10.0,
})
esp_charges = esp_drv.compute(molecule, basis, 'esp')
```

In both cases, the user needs to specify the number of layers of the molecular surface as well as the surface grid point density in these layers (in units of Å$^{-2}$).

### RESP charges

The restrained electrostatic potential (RESP) charge model is an improvement to the Merz–Kollman scheme as the figure-of-merit is rather insensitive to variations in charges of atoms buried inside the molecule.

```{figure} ../images/chi_square.png
---
name: chi_square
width: 600px
align: center
---
Dependence of figure-of-merit, $\chi^2_\mathrm{esp}$, with respect to variations in atomic charges. Four separate atoms are here considered.
```

To avoid unphysically high magnitudes of the charges of interior atoms, a hyperbolic penalty function is added

\begin{equation*}
\chi_{\mathrm{rstr}}^2 = \alpha \sum_I \bigl((q_I^2+\beta^2)^{1/2}-\beta\bigl)
\end{equation*}

so that the diagonal matrix elements become equal to

\begin{equation*}
A_{JJ} = 
\frac{1}{4\pi\varepsilon_0}
\sum_{a} \frac{1}{r_{aJ}^2} + \alpha \, (q_J^2+\beta^2)^{-1/2}
\end{equation*}

with a dependency on the partial charge. Consequently, RESP charges are obtained by solving the matrix equation iteratively until the charges and Lagrange multipliers become self-consistent. In addition to that, the RESP charge model allows for the introduction of constraints on charges of equivalent atoms due to symmetry operations or bond rotations.

The RESP cahrges are detemined with VeloxChem with use of an input file as below

```
@jobs
task: resp charges
@end

@method settings
basis: 6-31g_d_
@end

@resp charges
equal charges: 2 = 3    # with reference to the atom ordering below
@end

@molecule
charge: 0
multiplicity: 1
units: au
xyz:  
...
@end 
```

or in a Jupyter notebook according to

```
import veloxchem as vlx

mol_str = """
...
"""

molecule = vlx.Molecule.read_str(mol_str, units='au')
basis = vlx.MolecularBasis.read(molecule, '6-31g_d_')

resp_drv = vlx.RespChargesDriver()
resp_drv.update_settings({
    'equal_charges': '2 = 3'
})
resp_charges = resp_drv.compute(molecule, basis, 'resp')
```

### LoProp charges and polarizabilities

The LoProp approach {cite}`Gagliardi2004` is implemented for the determination of localized (atomic) charges and polarizabilities that enter into polarizable embedding calculations of optical spectra.

````
@jobs
task: loprop
@end

@method settings
xcfun: b3lyp
basis: ANO-S-VDZP # An ANO type of basis set should be used
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
````

## Polarizable embedding

An SCF calculation with a polarizable environment is performed in VeloxChem with an input file of the form

```
@jobs
task: scf
@end

@method settings
basis: aug-cc-pvdz
potfile: pe.pot
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

together with a potential file `pe.pot` of the form

```
@COORDINATES
6
AA
O   -0.9957202   0.0160415   1.2422556
H   -1.4542703  -0.5669741   1.8472817
H   -0.9377950  -0.4817912   0.4267562
O   -0.2432343  -1.0198566  -1.1953808
H    0.4367536  -0.3759433  -0.9973297
H   -0.5031835  -0.8251492  -2.0957959
@MULTIPOLES
ORDER 0
6
1      -0.67444408
2       0.33722206
3       0.33722206
4      -0.67444408
5       0.33722206
6       0.33722206
@POLARIZABILITIES
ORDER 1 1
6
1       5.73935090    0.00000000    0.00000000    5.73935090    0.00000000    5.73935090
2       2.30839051    0.00000000    0.00000000    2.30839051    0.00000000    2.30839051
3       2.30839051    0.00000000    0.00000000    2.30839051    0.00000000    2.30839051
4       5.73935090    0.00000000    0.00000000    5.73935090    0.00000000    5.73935090
5       2.30839051    0.00000000    0.00000000    2.30839051    0.00000000    2.30839051
6       2.30839051    0.00000000    0.00000000    2.30839051    0.00000000    2.30839051
EXCLISTS
6     3
1     2     3   
2     1     3   
3     1     2   
4     5     6   
5     4     6   
6     4     5   
```
