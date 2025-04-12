# Installing the program

## Installing precompiled binaries using conda

Binaries are available for the three main operating systems:

- Windows
- macOS
- Linux

[Conda](https://docs.conda.io/en/latest/) is an open-source package and environment management system that runs on Windows, macOS, and Linux. The [conda-forge](https://conda-forge.org/) channel contains a large number of open-source certified packages enabling scientific work. It is recommended that you install the minimal installer for conda named miniconda, or the community-driven installer named miniforge, that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others.

Retrieve miniconda or miniforge from the following website

> <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>

Install the version for 64-bit computers that comes with Python (>=3.9).

Start a conda terminal, or Anaconda Prompt / Miniforge Prompt as it is referred to on a Windows system. Conda supports multiple *environments* and you start in the one named `base` as is typically indicated by the prompt. To create a new and additional environment named `vlxenv` and install VeloxChem, Matplotlib, and Jupyter notebook (and package dependencies such as NumPy and SciPy) into it, you enter the following command line statement

```
$ conda create -n vlxenv veloxchem matplotlib jupyterlab -c veloxchem -c conda-forge
```

````{admonition} Considerations for NumPy performance
:class: tip

On Linux, we recommend installing `veloxchem` alongside `libopenblas` to ensure that `numpy` uses a high-performance backend for linear algebra operations.
````

You can list your conda environments

```
$ conda env list
```

The activated environment will be marked with an asterisk (the `base` environment to begin with) and you can activate your new environment with the command

```
$ conda activate vlxenv
```

as should be indicated by getting a modified prompt.

Inside this newly created environment, you should now be ready to start JupyterLab with the command

```
$ jupyter-lab
```

which should open in your default web browser. A notebook in JupyterLab allows for interactive execution of Python code written into cells. You should now be able to import the VeloxChem module in a cell:

```
import veloxchem as vlx
```

and start calculations. See the [eChem](https://kthpanor.github.io/echem) book for a multitude of examples.


## Installing from source

### Obtaining the source code

The source code can be downloaded from the [GitHub repository](https://github.com/VeloxChem/VeloxChem):

```
$ git clone https://github.com/VeloxChem/VeloxChem.git
```

### Build prerequisites

- [CMake](https://cmake.org/)
- C++ compiler fully compliant with the C++20 standard
- Linear algebra libraries implementing the BLAS and LAPACK interfaces (e.g. OpenBLAS)
- MPI library (e.g. MPICH)
- [Python](https://www.python.org/) (>=3.9) that includes the interpreter, the development header files, and the development libraries
- [MPI4Py](https://mpi4py.readthedocs.io/en/stable/)
- [Scikit-build](https://scikit-build.readthedocs.io/en/latest/)
- [Libxc](https://libxc.gitlab.io/)
- [Eigen](https://gitlab.com/libeigen/eigen)

Optional, add-on dependencies:

- [dftd4-python](https://github.com/dftd4/dftd4)

See {ref}`external-dependencies` for instructions on how to get these add-ons.

To avoid clashes between dependencies, we recommend to always use a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html).

(with-conda)=
### Installing on Unix-like systems using conda

[Conda](https://docs.conda.io/en/latest/) and the software packaged on the [conda-forge](https://conda-forge.org/) channel provide build isolation and greatly simplify the installation of VeloxChem.

- Move to the folder containing the source code:

  ```
  $ cd VeloxChem
  ```

- Create and activate the conda environment:

  ```
  $ conda env create -f <environment_file>
  $ conda activate vlxenv
  ```

  This will create and activate a conda environment named `vlxenv`. In this environment all the build dependencies will be installed from the conda-forge channel, including the C++ compiler, MPI, [NumPy](https://numpy.org), [MPI4Py](https://mpi4py.readthedocs.io/en/stable/), etc. We provide two options for the `<environment_file>` that specifies different linear algebra backend for your conda environment:

  - `mkl_env.yml` which installs the Intel Math Kernel Library,
  - `openblas_env.yml` which installs the OpenBLAS library.

  Note that the MPICH library will be installed by the .yml file. If you prefer another MPI library such as Open MPI, you can edit the .yml file and replace mpich by openmpi. Read more about the .yml file in [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually).

- Set scikit-build and cmake options:

  ```
  $ export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=<math_library> -DCMAKE_CXX_COMPILER=mpicxx"
  ```

  where ``<math_library>`` can be ``MKL`` or ``OpenBLAS``.

  If you are installing VeloxChem on macOS you may also need to set the
  `CMAKE_ARGS` environment variable. See [Known issues](known-issues-macos) for
  details.

- Build and install VeloxChem in the conda environment:

  ```
  $ python3 -m pip install --no-build-isolation -v .
  ```

  By default, the build process will use *all* available cores to compile the C++ sources in parallel. This behavior can be controlled via the `VLX_NUM_BUILD_JOBS` environment variable:

  ```
  $ VLX_NUM_BUILD_JOBS=N python3 -m pip install --no-build-isolation -v .
  ```

  which will install VeloxChem using *N* cores.

- The environment now contains all that is necessary to run VeloxChem. You can deactivate it by

  ```
  $ conda deactivate
  ```

### Installing on Cray system

- Load Cray modules:

  ```
  $ module load PrgEnv-gnu
  $ module load cpe
  $ module load cray-python
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) with `--system-site-packages`

  ```
  $ python3 -m venv --system-site-packages vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip setuptools wheel
  $ python3 -m pip install h5py pytest psutil geometric cmake pybind11-global scikit-build ninja rdkit
  ```

- Clone [Eigen](https://gitlab.com/libeigen/eigen) and set environment variable `EIGEN_INCLUDE_DIR`

  ```
  $ git clone -b 3.4.0 https://gitlab.com/libeigen/eigen.git
  $ export EIGEN_INCLUDE_DIR=/path/to/your/eigen
  ```

- Install [Libxc](https://libxc.gitlab.io/)

  ```
  $ cd libxc-7.0.0
  $ mkdir build && cd build
  $ cmake -DDISABLE_KXC=OFF -DDISABLE_LXC=OFF -DCMAKE_C_COMPILER=gcc-12 -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/libxc ..
  $ make && make test
  $ make install
  $ cd ../..
  ```

  Make sure to replace `gcc-12` with the C compiler you are using. Please also
  note that compiling Libxc with `-DDISABLE_KXC=OFF -DDISABLE_LXC=OFF` takes a
  long time. If you do not need the third- and fourth-order derivatives you can
  remove them to speed up the compilation. 

- Compile VeloxChem

  ```
  $ cd VeloxChem
  $ export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=Cray -DCMAKE_CXX_COMPILER=CC"
  $ export CMAKE_PREFIX_PATH=/path/to/your/libxc:$CMAKE_PREFIX_PATH
  $ export LD_LIBRARY_PATH=/path/to/your/libxc/lib:$LD_LIBRARY_PATH
  $ python3 -m pip install --no-build-isolation -v .
  ```

  If you are installing VeloxChem on a HPC cluster, please make sure to run the
  above compilations on an interactive node.

- CrayBLAS environment variables

  When running VeloxChem on Cray systems, we recommend setting the following environment
  variables:

  ```
  export CRAYBLAS_LEVEL1_LEGACY=1
  export CRAYBLAS_LEVEL2_LEGACY=1
  export CRAYBLAS_LEVEL3_LEGACY=1
  ```

### Installing on Ubuntu

- Install dependencies using apt

  ```
  $ sudo apt update
  $ sudo apt install build-essential wget cmake git python3 python3-pip python3-venv
  $ sudo apt install libopenblas-openmp-dev liblapacke-dev libeigen3-dev mpich
  ```

- Install [Libxc](https://libxc.gitlab.io/)

  ```
  $ cd libxc-7.0.0
  $ mkdir build && cd build
  $ cmake -DDISABLE_KXC=OFF -DDISABLE_LXC=OFF -DCMAKE_C_COMPILER=gcc-12 -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/libxc ..
  $ make && make test
  $ make install
  $ cd ../..
  ```

  Make sure to replace `gcc-12` with the C compiler you are using. Please also
  note that compiling Libxc with `-DDISABLE_KXC=OFF -DDISABLE_LXC=OFF` takes a
  long time. If you do not need the third- and fourth-order derivatives you can
  remove them to speed up the compilation. 

- Create and activate a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html)

  ```
  $ python3 -m venv vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip setuptools wheel
  $ python3 -m pip install numpy mpi4py h5py
  $ python3 -m pip install cmake pybind11-global scikit-build
  ```

- Install VeloxChem:

  ```
  $ cd VeloxChem
  $ export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=OpenBLAS -DCMAKE_CXX_COMPILER=mpicxx"
  $ export CMAKE_PREFIX_PATH=/path/to/your/libxc:$CMAKE_PREFIX_PATH
  $ export LD_LIBRARY_PATH=/path/to/your/libxc/lib:$LD_LIBRARY_PATH
  $ python3 -m pip install --no-build-isolation -v .
  ```

### Installing on PowerLinux

- See installation instructions [using conda](with-conda)

### Installing on macOS

- See installation instructions [using conda](with-conda)

(known-issues-macos)=
- Known issues

  On macOS you may encounter the following error at the end of the ``pip install`` step:

  ```
  ...
      base_version = tuple(int(x) for x in base_version.split("."))
  ValueError: invalid literal for int() with base 10: ''
  error: subprocess-exited-with-error
  ...
  ```

  One workaround is to manually add the ``CMAKE_OSX_DEPLOYMENT_TARGET`` option
  to ``CMAKE_ARGS`` and redo the ``pip install`` step:

  ```
  $ python3 -c 'import sysconfig; print(sysconfig.get_platform())'
  macosx-10.9-x86_64

  $ export CMAKE_ARGS="-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9"
  $ python3 -m pip install --no-build-isolation .
  ```

  Another issue that one may encounter on macOS is that the ``-march=native``
  flag is not supported by the compiler. The workaround is to add
  ``-DENABLE_ARCH_FLAGS=OFF`` to ``CMAKE_ARGS``. For example:

  ```
  $ export CMAKE_ARGS="-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9 -DENABLE_ARCH_FLAGS=OFF"
  $ python3 -m pip install --no-build-isolation .
  ```

(external-dependencies)=
## External dependencies

If you wish to use functionality offered through interfaces with other software packages, you will first need to install them.  Currently, interface to add-on dependency [dftd4-python](https://github.com/dftd4/dftd4) is available.

### The dftd4-python package for dispersion correction

It is recommended to install the dftd4-python package in a conda environment:

```
$ conda install dftd4-python -c conda-forge
```

Alternatively, you can compile it using ``meson``:

```
$ python3 -m pip install meson ninja cffi
$ cd dftd4-3.7.0/
$ meson setup _build -Dpython=true -Dpython_version=$(which python3)
$ meson test -C _build --print-errorlogs
$ meson configure _build --prefix=/path/to/your/dftd4
$ meson install -C _build
```

If you want to use custom math library, add `-Dlapack=custom` and
`-Dcustom_libraries=...` to the `meson setup` command.

After installation, add the dftd4 package to `PYTHONPATH` and `LD_LIBRARY_PATH`. Make sure to
replace "python3.11" with the version of Python used in your virtual
environment.

```
$ export PYTHONPATH=$PYTHONPATH:/path/to/your/dftd4/lib/python3.11/site-packages
$ export LD_LIBRARY_PATH=/path/to/your/dftd4/lib64:$LD_LIBRARY_PATH
```
