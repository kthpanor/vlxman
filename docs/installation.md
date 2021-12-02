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

- Build tool providing the `make` utility
- C++ compiler fully compliant with the C++11 standard
- Linear algebra libraries implementing the BLAS and LAPACK interfaces (e.g. Intel MKL, OpenBLAS or Cray LibSci)
- MPI library (e.g. MPICH, Intel MPI or Open MPI)
- Installation of Python >=3.6 that includes the interpreter, the development header files, and the development libraries
- The [MPI4Py](https://mpi4py.readthedocs.io/en/stable/) module for Python

Optional, add-on dependencies:

- [CPPE (v0.2.1)](https://github.com/maxscheurer/cppe/releases/tag/v0.2.1)
- [XTB](https://github.com/grimme-lab/xtb)

See {ref}`external-dependencies` for instructions on how to get these add-ons.

To avoid clashes between dependencies, we recommend to always use a [virtual enviroment](https://docs.python.org/3.6/tutorial/venv.html).

(with-anaconda)=
### With Anaconda

[Anaconda](https://www.anaconda.com/products/individual) and the software packaged on the [conda-forge](https://conda-forge.org/) channel provide build isolation and greatly simplify the installation of VeloxChem.

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

- Build and install VeloxChem in the conda environment:

  ```
  $ python -m pip install .
  ```

  By default, the build process will use *all* available cores to compile the C++ sources in parallel. This behavior can be controlled via the `VLX_NUM_BUILD_JOBS` environment variable:

  ```
  $ VLX_NUM_BUILD_JOBS=N python -m pip install .
  ```

  which will install VeloxChem using *N* cores.

- The environment now contains all that is necessary to run VeloxChem. You can deactivate it by

  ```
  $ conda deactivate
  ```

### Cray platform (x86-64 or ARM processor)

- Load cray modules:

  ```
  $ module swap PrgEnv-cray PrgEnv-gnu
  $ module load cray-python
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3.6/tutorial/venv.html)

  ```
  $ python3 -m venv vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip
  ```

- Install [MPI4Py](https://mpi4py.readthedocs.io/en/stable/)

  ```
  $ CC=cc MPICC=cc python3 -m pip install --no-deps --no-binary=mpi4py mpi4py
  ```

- Use the compiler wrapper to compile VeloxChem:

  ```
  $ cd veloxchem
  $ CXX=CC python3 -m pip install .
  ```

  This will also take care of installing the additional necessary Python modules.

  If you are installing VeloxChem on a HPC cluster, please run the compilation on an interactive node:

  ```
  $ salloc -N 1 ...
  $ CXX=CC VLX_NUM_BUILD_JOBS=N srun -n 1 python3 -m pip install .
  ```

  where *N* is the number of cores on the node.

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


(external-dependencies)=
## External dependencies

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

