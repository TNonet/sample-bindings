import glob
import os
import pathlib
import re
import subprocess
from typing import Union

from Cython.Distutils import build_ext as cython_build_ext
from setuptools import Extension

try:
    from Cython.Build import cythonize
except ImportError:
    cythonize = None

import sys

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension
from pybind11.setup_helpers import build_ext as pybind_build_ext
from setuptools import setup

from setuptools.command.build_ext import build_ext as setuptools_build_ext

__version__ = "0.0.1"

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


def no_cythonize(extensions, **_ignore):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in (".pyx", ".py"):
                if extension.language == "c++":
                    ext = ".cpp"
                else:
                    ext = ".c"
                sfile = path + ext
            sources.append(sfile)
        extension.sources[:] = sources
    return extensions


compiler_directives = {"language_level": 3, "embedsignature": True}


cython_extensions = [
    Extension(name='sample_bindings.rectangle',
              sources=['sample_bindings/cy_rect/rectangle.pyx',
                       'sample_bindings/src2/Rectangle.cpp'],
              include_dirs=['.', 'sample_bindings/src2/include'],
              language="c++",
              extra_compile_args=["-std=c++11"],  # Optional,
              extra_link_args=["-std=c++11"],  # Optional
              )
]

# for dirname, dirnames, filenames in os.walk('.'):
#     # print path to all subdirectories first.
#     for subdirname in dirnames:
#         print(os.path.join(dirname, subdirname))
#
#     # print path to all filenames.
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
#
#     # Advanced usage:
#     # editing the 'dirnames' list will stop os.walk() from recursing into there.
#     if '.git' in dirnames:
#         # don't go into any .git directories.
#         dirnames.remove('.git')
#
# HEADER_FILES = glob.glob("**/*.h", recursive=True)
# print(f"LIST(HEADER_FILES) = {list(HEADER_FILES)}")
# HEADER_FOLDERS = list(set(pathlib.Path(f).parents[0] for f in HEADER_FILES))
# print(f"RECTANGLE_HEADERS = {HEADER_FOLDERS}")


extensions = [
    *cythonize(cython_extensions,
               compiler_directives=compiler_directives),
    Pybind11Extension("sample_bindings.pybind_module",
                      sources=["sample_bindings/pybind_module.cpp"],
                      # Example: passing in the version to the compiled code
                      define_macros=[('VERSION_INFO', __version__)],
                      ),
]

print(extensions)

setup(
    name='sample_bindings',
    cmdclass={'build_ext': pybind_build_ext},  # Source:
    # https://stackoverflow.com/questions/66678268/mix-cython-and-cmake-extensions-in-python-setuptools
    install_requires=['cython'],
    zip_safe=False,
    extras_require={"test": [
        "pytest",
        ]},

    ext_modules=extensions,
)
