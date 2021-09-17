# Electronic densities

## Cube files

### Molecular orbitals

```
@jobs
task: visualization
@end

@method settings
basis: def2-svp
@end

@visualization
cubes: density(alpha), mo(homo)
files: density.cube, homo.cube
@end

@molecule
charge: 0
multiplicity: 1
units: au
xyz:  
O   0.0   0.0   0.0
H   0.0   1.4   1.1
H   0.0  -1.4   1.1
@end 
```

### Natural transition orbitals and attachment/detachment densities

Cube files for natural transition orbitals (NTOs) and detachment/attachment densities can be generated in response calculations with the following response section statements:

```
@response
property: absorption
nstates: 3
nto: yes
nto_pairs: 2
detach_attach: yes
@end
```

### Visualize cube files

The cube files can be visualized in a Jupyter notebook with use of the [py3Dmol](https://pypi.org/project/py3Dmol/) module:

```
import py3Dmol as p3d

# generate view
v = p3d.view(width=400, height=400)

v.addModel(pyridine_xyz, "xyz")
v.setStyle({'stick':{}})

with open("cube_1.cube", "r") as f:
    cube = f.read()

# negative lobe    
v.addVolumetricData(cube, "cube", {"isoval": -0.02, "color": "blue", "opacity": 0.75})
# positive lobe
v.addVolumetricData(cube, "cube", {"isoval": 0.02, "color": "red", "opacity": 0.75})

v.show()
```
