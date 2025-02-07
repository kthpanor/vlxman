# Installing the program

## Installing binaries using conda

Binaries are available for the three main operating systems:

- Windows
- macOS
- Linux

[Conda](https://docs.conda.io/en/latest/) is an open-source package and environment management system that runs on Windows, macOS, and Linux. The conda repository contains a large number of open-source certified packages enabling scientific work. It is recommended that you install the minimal installer for conda named miniconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others.

Retrieve miniconda from the following website

> <https://docs.conda.io/en/latest/miniconda.html>

Install the version for 64 bit computers that comes with Python (>=3.8).

````{admonition} Faster conda solver
:class: tip

The new `conda-libmamba-solver` run much faster than the default, as discussed in [this blog post](https://www.anaconda.com/blog/conda-is-fast-now). We recommend that you use this solver, which is done by updating conda, installing the new solver to your base environment, and configuring your solver selection:

```
conda update -n base conda
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```
````

Start a conda terminal, or Anaconda Powershell as it is referred to on a Windows system. Conda supports multiple *environments* and you start in the one named `base` as is typically indicated by the prompt. To create a new and additional environment named `vlxenv` and install VeloxChem, Matplotlib, and Jupyter notebook (and package dependencies such as NumPy and SciPy) into it, you enter the following command line statement

```
$ conda create -n vlxenv veloxchem matplotlib jupyterlab -c veloxchem -c conda-forge
```

You can list your conda environments

```
$ conda env list
```

The activated environment will be marked with an asterisk (the `base` environment to begin with) and you can activate your new environment with the command

```
$ conda activate vlxenv
```

as should be indicated by getting a modified prompt.

Inside this newly created environment, you should now be ready to start a Jupyter notebook with the command

```
$ jupyter-notebook
```

which should open in your default web browser. A notebook allows for interactive execution of Python code written into cells. You should now be able to import the VeloxChem module in a cell:

```
import veloxchem as vlx
```

and start calculations. See the [eChem](https://kthpanor.github.io/echem) book for a multitude of examples.


## Installing from source

### Obtaining the source code

The source code can be downloaded from the [GitLab repository](https://gitlab.com/veloxchem/veloxchem):

```
$ git clone https://gitlab.com/veloxchem/veloxchem
```

### Build prerequisites

- [CMake](https://cmake.org/)
- C++ compiler fully compliant with the C++17 standard
- Linear algebra libraries implementing the BLAS and LAPACK interfaces (e.g. Intel MKL, OpenBLAS or Cray LibSci)
- MPI library (e.g. MPICH, Intel MPI or Open MPI)
- [Python](https://www.python.org/) (>=3.8) that includes the interpreter, the development header files, and the development libraries
- [MPI4Py](https://mpi4py.readthedocs.io/en/stable/)
- [Scikit-build](https://scikit-build.readthedocs.io/en/latest/)
- [Libxc](https://libxc.gitlab.io/)

Optional, add-on dependencies:

- [CPPE](https://github.com/maxscheurer/cppe)
- [XTB](https://github.com/grimme-lab/xtb)

See {ref}`external-dependencies` for instructions on how to get these add-ons.

To avoid clashes between dependencies, we recommend to always use a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html).

(with-conda)=
### Installing using conda

[Conda](https://docs.conda.io/en/latest/) and the software packaged on the [conda-forge](https://conda-forge.org/) channel provide build isolation and greatly simplify the installation of VeloxChem.

- Move to the folder containing the source code:

  ```
  $ cd veloxchem
  ```

- Create and activate the conda environment:

  ```
  $ conda env create -f <environment_file>
  $ conda activate vlxenv
  ```

  This will create and activate a conda environment named `vlxenv`. In this environment all the build dependencies will be installed from the `conda-forge` channel, including the C++ compiler, MPI, [NumPy](https://numpy.org), [MPI4Py](https://mpi4py.readthedocs.io/en/stable/), etc. We provide two options for the `<environment_file>` that specifies different linear algebra backend for your conda environment:

  - `mkl_env.yml` which installs the Intel Math Kernel Library,
  - `openblas_env.yml` which installs the OpenBLAS library.

  Note that the MPICH library will be installed by the `yml` file. If you prefer another MPI library such as Open MPI, you can edit the `yml` file and replace `mpich` by `openmpi`. Read more about the `yml` file in [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually).

- Set scikit-build configure options:

  ```
  $ export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=<math_library> -DCMAKE_CXX_COMPILER=mpicxx"
  ```

  where ``<math_library>`` can be ``MKL`` or ``OpenBLAS``.

- Set XTBHOME if you would like to enable xTB:

  ```
  $ export XTBHOME=/path/to/your/vlxenv
  ```

- Build and install VeloxChem in the conda environment:

  ```
  $ python3 -m pip install .
  ```

  By default, the build process will use *all* available cores to compile the C++ sources in parallel. This behavior can be controlled via the `VLX_NUM_BUILD_JOBS` environment variable:

  ```
  $ VLX_NUM_BUILD_JOBS=N python3 -m pip install .
  ```

  which will install VeloxChem using *N* cores.

- The environment now contains all that is necessary to run VeloxChem. You can deactivate it by

  ```
  $ conda deactivate
  ```

### Installing on Cray platform (x86-64 or ARM processor)

- Load Cray modules:

  ```
  $ module swap PrgEnv-cray PrgEnv-gnu
  $ module load cray-python
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html)

  ```
  $ python3 -m venv vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip setuptools wheel
  $ python3 -m pip install cmake pybind11-global scikit-build
  ```

- Install [MPI4Py](https://mpi4py.readthedocs.io/en/stable/)

  ```
  $ CC=cc MPICC=cc python3 -m pip install --no-deps --no-binary=mpi4py mpi4py
  ```

- Install [Libxc](https://tddft.org/programs/libxc/)

  ```
  $ cd libxc-6.0.0
  $ mkdir build && cd build
  $ cmake -DDISABLE_KXC=OFF -DDISABLE_LXC=OFF -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/libxc ..
  $ make && make test
  $ make install
  $ cd ../..
  ```

- Use the compiler wrapper to compile VeloxChem:

  ```
  $ cd veloxchem
  $ export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=Cray -DCMAKE_CXX_COMPILER=CC"
  $ export CMAKE_PREFIX_PATH=/path/to/your/libxc/:$CMAKE_PREFIX_PATH
  $ python3 -m pip install .
  ```

  This will also take care of installing the additional necessary Python modules.

  If you are installing VeloxChem on a HPC cluster, please run the compilation on an interactive node:

  ```
  $ salloc -N 1 ...
  $ VLX_NUM_BUILD_JOBS=N srun -n 1 python3 -m pip install .
  ```

  where *N* is the number of cores on the node.

### Installing on Debian-based Linux

- Install Intel Math Kernel Library from 
  [this page](https://software.intel.com/en-us/articles/installing-intel-free-libs-and-python-apt-repo).
  Note that this requires superuser privileges:

  ```
  $ wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
  $ sudo apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
  $ sudo sh -c 'echo deb https://apt.repos.intel.com/mkl all main > /etc/apt/sources.list.d/intel-mkl.list'
  $ sudo apt-get update
  $ sudo apt-get install intel-mkl-64bit-2019.1-053
  ```

- Install MPI and Python:

  ```
  $ sudo apt-get install git mpich python3 python3-dev python3-pip python3-venv
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html)

  ```
  $ python3 -m venv vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip setuptools wheel
  $ python3 -m pip install numpy mpi4py h5py
  $ python3 -m pip install cmake pybind11-global scikit-build
  ```

- Install [Libxc](https://tddft.org/programs/libxc/)

  ```
  $ cd libxc-6.0.0
  $ mkdir build && cd build
  $ cmake -DDISABLE_KXC=OFF -DDISABLE_LXC=OFF -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/libxc ..
  $ make && make test
  $ make install
  $ cd ../..
  ```

- Install VeloxChem:

  ```
  $ source /opt/intel/mkl/bin/mklvars.sh intel64
  $ export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=MKL -DCMAKE_CXX_COMPILER=mpicxx"
  $ export CMAKE_PREFIX_PATH=/path/to/your/libxc/:$CMAKE_PREFIX_PATH
  $ python3 -m pip install git+https://gitlab.com/veloxchem/veloxchem
  ```

### Installing on RPM-based Linux

- Install Math Kernel Library from
  [this page](https://software.intel.com/en-us/articles/installing-intel-free-libs-and-python-yum-repo).
  Note that this requires superuser privileges:

  ```
  $ sudo yum install yum-utils
  $ sudo yum-config-manager --add-repo https://yum.repos.intel.com/mkl/setup/intel-mkl.repo
  $ sudo rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
  $ sudo yum install intel-mkl-64bit
  ```

- Install MPI and Python:

  ```
  $ sudo yum install gcc gcc-g++ mpich mpich-devel python3 python3-devel python3-pip
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html)

  ```
  $ python3 -m venv vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip setuptools wheel
  $ python3 -m pip install numpy mpi4py h5py
  $ python3 -m pip install cmake pybind11-global scikit-build
  ```

- Install [Libxc](https://tddft.org/programs/libxc/)

  ```
  $ cd libxc-6.0.0
  $ mkdir build && cd build
  $ cmake -DDISABLE_KXC=OFF -DDISABLE_LXC=OFF -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/libxc ..
  $ make && make test
  $ make install
  $ cd ../..
  ```

- Install VeloxChem (you may need to open a new terminal to run the ``module`` command):

  ```
  $ module load mpi/mpich-x86_64
  $ source /opt/intel/mkl/bin/mklvars.sh intel64
  $ export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=MKL -DCMAKE_CXX_COMPILER=mpicxx"
  $ export CMAKE_PREFIX_PATH=/path/to/your/libxc/:$CMAKE_PREFIX_PATH
  $ python3 -m pip install git+https://gitlab.com/veloxchem/veloxchem
  ```

### Installing on PowerLinux

- See installation instructions [using conda](with-conda)

### Installing on macOS

- See installation instructions [using conda](with-conda)

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
  $ python3 -m pip install .
  ```

  Another issue that one may encounter on macOS is that the ``-march=native``
  flag is not supported by the compiler. The workaround is to add
  ``-DENABLE_ARCH_FLAGS=OFF`` to ``CMAKE_ARGS``. For example:

  ```
  $ export CMAKE_ARGS="-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9 -DENABLE_ARCH_FLAGS=OFF"
  $ python3 -m pip install .
  ```

### Installing on Windows

- Soon to come!


(external-dependencies)=
## External dependencies

If you wish to use functionality offered through interfaces with other software packages, you will first need to install them.  Currently, interfaces to add-on dependencies [XTB](https://github.com/grimme-lab/xtb) and [CPPE](https://github.com/maxscheurer/cppe) are available.

### The CPPE library for polarizable embedding

There are few ways to install the CPPE library for polarizable embedding. Note that you will need a C++ compiler compliant with the C++14 standard and CMake.

You can install it via `pip` in your virtual environment:

```
$ python3 -m pip install cppe
```

or as an extra during compilation of VeloxChem:

```
$ python3 -m pip install .[qmmm]
```

Alternatively, you can compile it without using `pip`:

```
# Build CPPE
$ git clone https://github.com/maxscheurer/cppe
$ cd cppe; mkdir build; cd build
$ cmake -DENABLE_PYTHON_INTERFACE=ON ..
$ make

# Set up python path
$ export PYTHONPATH=/path/to/your/cppe/build/stage/lib:$PYTHONPATH
```

### The XTB package for semiempirical methods

It is recommended to install the XTB package in a conda environment:

```
$ conda install xtb -c conda-forge
```

Alternatively, you can compile it using ``cmake``:

```
# Build XTB
$ git clone https://github.com/grimme-lab/xtb
$ cd xtb; mkdir build; cd build
$ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/xtb ..
$ make
$ make install

# Set XTBHOME prior to installing VeloxChem
$ export XTBHOME=/path/to/your/xtb
```
## Release versions

- 1.0-rc3 (2022-11-09) Third release candidate

- 1.0-rc2 (2021-04-23) Second release candidate

- 1.0-rc (2020-02-28) First release candidate
