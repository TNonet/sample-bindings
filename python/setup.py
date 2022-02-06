from skbuild import setup

setup(
    name="sample_bindings",
    version="0.0.1",
    description="a minimal example package (with pybind11)",
    author='Tim Nonet',
    license="MIT",
    install_requires=['cython'],
    packages=['sample_bindings'],
    package_dir={'': ''},
    cmake_install_dir='sample_bindings'
)