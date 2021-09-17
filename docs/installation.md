# Installing the program

## Installing binaries

Binaries are available for the three main operating systems:

- Windows
- MacOS
- Linux

### With Conda

Conda is an open-source package and environment management system that runs on Windows, MacOS, and Linux. The conda repository contains a large number of open-source certified packages enabling scientific work. It is recommended that you install the minimal installer for conda named miniconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others.

Retrieve miniconda from the following website

> <https://docs.conda.io/en/latest/miniconda.html>

Install the version for 64 bit computers that comes with Python (>=3.6).

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

- C++ compiler fully compliant with the C++11 standard
- Installation of Python >=3.6 that includes the interpreter, the development header files, and the development libraries
- Build tool providing the `make` utility
- The [pybind11](https://pybind11.readthedocs.io>) (>=2.6) header-only library
- MPI library
- Linear algebra libraries implementing the BLAS and LAPACK interfaces
- The following Python modules:
  - [h5py](https://www.h5py.org/)
  - [psutil](https://psutil.readthedocs.io/en/latest/)
  - [MPI4Py](https://mpi4py.readthedocs.io/)
  - [NumPy](https://numpy.org)
  - [geomeTRIC](https://github.com/leeping/geomeTRIC)

Optional, add-on dependencies:

- [CPPE (v0.2.1)](https://github.com/maxscheurer/cppe/releases/tag/v0.2.1)
- [XTB](https://github.com/grimme-lab/xtb)

See external-dependencies for instructions on how to get these add-ons.

To avoid clashes between dependencies, we recommend to always use a [virtual enviroment](https://docs.python.org/3.6/tutorial/venv.html).

(with-anaconda)=
### With Anaconda

[Anaconda](https://www.anaconda.com/products/individual) and the software packaged on the [conda-forge](https://conda-forge.org/) channel provide build isolation and greatly simplify the installation of VeloxChem.

- Move to the folder containing the source code:

  ```
  $ cd veloxchem
  ```

- Create and activate the Conda environment:

  ```
  $ conda create --name <name> python=3.x
  $ conda activate <name>
  ```

  ```{note}
  VeloxChem requires at least Python 3.6
  ```

- Install standard build dependencies:

  ```
  $ conda env update --file <environment> --prune
  ```

  This will install, among other, the C++ compiler and NumPy. The `environment.yml` file specifies the packages needed.  They will be installed from the `conda-forge` channel. VeloxChem can use different linear algebra backends and we provide two environment files you can use to set up your conda environment:

    - `mkl_env.yml` which installs the Intel Math Kernel Library,
    - `openblas_env.yml` which installs the OpenBLAS library.

- Install MPI and [Mpi4Py](https://mpi4py.readthedocs.io/)

  - To use [OpenMPI](https://www.open-mpi.org/)

    ```
    $ conda install openmpi mpi4py -c conda-forge
    ```

  - To use [MPICH](https://www.mpich.org/)

    ```
     $ conda install mpich mpi4py -c conda-forge
     ```

- Build and install VeloxChem in the Conda environment:

  ```
  $ python -m pip install .
  ```

  By default, the build process will use *all* available cores to compile the C++ sources in parallel. This behavior can be controlled via the `VLX_NUM_BUILD_JOBS` environment variable:

  ```
  $ env VLX_NUM_BUILD_JOBS=N python -m pip install .
  ```

  will install VeloxChem using *N* parallel processes.

- The environment now contains all that is necessary to run VeloxChem. You can deactivate it by issuing:

   ```
   $ conda deactivate
   ```

### Cray platform (x86-64 or ARM processor)

- Load cray modules:

  ```
  $ module swap PrgEnv-cray PrgEnv-gnu
  $ module load cray-hdf5
  $ module load cray-python/3.6.5.7
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3.6/tutorial/venv.html)

  ```
  $ python3 -m venv vlx
  $ source vlx/bin/activate
  $ python -m pip install -U pip
  ```

  Once the virtual environment is activated, you can just use `python` to invoke the interpreter.

- Install [Mpi4Py](https://mpi4py.readthedocs.io/):

  1. Download a recent version of the source distribution::

      ```
      $ curl -LO https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-X.Y.Z.tar.gz
      ```

  2. Unzip the archive:

     ```
     $ tar xf mpi4py-X.Y.Z.tar.gz
     $ cd mpi4py-X.Y.Z
     ```

  3. Append the following lines to `mpi.cfg`:

     ```
     [cray]
     mpicc         = cc
     mpicxx        = CC
     extra_compile_args   = -shared
     extra_link_args      = -Wl,-rpath,/opt/cray/pe/mpt/7.7.9/gni/mpich-gnu/8.2/lib
     ```

  4. Build and install Mpi4Py:
     ```
     $ python setup.py build --mpi=cray
     $ python setup.py install
     ```

- Use the compiler wrapper to compile VeloxChem:

  ```
  $ export CXX=CC
  $ cd veloxchem
  $ python -m pip install .
  ```

  This will also take care of installing the additional necessary Python modules.

### Debian-based Linux

- Install Intel Math Kernel Library from `https://software.intel.com/en-us/articles/installing-intel-free-libs-and-python-apt-repo`

  Note that this requires superuser privileges:

  ```
  $ wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
  $ apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
  $ sudo sh -c 'echo deb https://apt.repos.intel.com/mkl all main > /etc/apt/sources.list.d/intel-mkl.list'
  $ sudo apt-get update
  $ sudo apt-get install intel-mkl-64bit
  ```

- Install MPI and Python:

  ```
   $ sudo apt-get install mpich python3 python3-dev python3-pip
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3.6/tutorial/venv.html)

  ```
  $ python3 -m venv vlx
  $ source vlx/bin/activate
  $ python -m pip install -U pip
  ```

- Install VeloxChem:

  ```
  $ cd veloxchem
  $ python -m pip install .
  ```

### RPM-based Linux

- Install Math Kernel Library from `https://software.intel.com/en-us/articles/installing-intel-free-libs-and-python-yum-repo`

  Note that this requires superuser privileges:

  ```
  $ sudo yum-config-manager --add-repo https://yum.repos.intel.com/mkl/setup/intel-mkl.repo
  $ sudo rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
  $ sudo yum install intel-mkl-64bit
  ```

- Install MPI and Python:

  ```
  $ sudo yum install mpich-3.2-devel python3-devel
  $ sudo ln -s /usr/lib64/mpich-3.2/bin/mpirun /usr/bin/mpirun
  $ sudo ln -s /usr/lib64/mpich-3.2/bin/mpicxx /usr/bin/mpicxx
  $ sudo ln -s /usr/lib64/mpich-3.2/bin/mpicc /usr/bin/mpicc
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3.6/tutorial/venv.html)

  ```
  $ python3 -m venv vlx
  $ source vlx/bin/activate
  $ python -m pip install -U pip
  ```

- Install VeloxChem:

  ```
  $ cd veloxchem
  $ python -m pip install .
  ```

### PowerLinux

- See installation instructions [With Anaconda](with-anaconda)

### MacOS

- See installation instructions [With Anaconda](with-anaconda)

### Windows

- Soon to come!


## Dependencies

If you wish to use functionality offered through interfaces with other software packages, you will first need to install them.  Currently, interfaces to add-on dependencies [XTB](https://github.com/grimme-lab/xtb) and [CPPE (v0.2.1)](https://github.com/maxscheurer/cppe/releases/tag/v0.2.1) are available.

### The CPPE library for polarizable embedding

There are few ways to install the CPPE library for polarizable embedding. Note that you will need a C++ compiler compliant with the C++14 standard and CMake.

You can install it via `pip` in your virtual environment:

```
$ python -m pip install cppe==0.2.1
```

or as an extra during compilation of VeloxChem:

```
$ python -m pip install .[qmmm]
```

Alternatively, you can compile it without using `pip`:

```
# Build CPPE
$ git clone -b v0.2.1 https://github.com/maxscheurer/cppe
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
$ git clone -b v6.3.3 https://github.com/grimme-lab/xtb
$ cd xtb; mkdir build; cd build
$ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/xtb ..
$ make
$ make install

# Set XTBHOME prior to installing VeloxChem
$ export XTBHOME=/path/to/your/xtb
```
## Release versions

- 1.0-rc2 (2021-04-23) Second release candidate

- 1.0-rc (2020-02-28) First release candidate

