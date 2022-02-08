import itertools
import os
import pathlib
import typing
from glob import glob

# def follow_sym_link(path: os.PathLike, patterns) -> typing.Generator[os.PathLike, None, None]:
#     if not os.path.islink(path):
#         raise ValueError(f"expected `path`, {path}, to be a symlink, but is not")
from glob import glob
import shutil

CXX_SYMLINK = pathlib.Path('sample_bindings/src')
CXX_DEST = pathlib.Path('sample_bindings/src2')
# CXX_HEADERS = glob("**/*.h", root_dir=CXX_SYMLINK, recursive=True)
# CXX_SOURCES = glob("**/*.cpp", root_dir=CXX_SYMLINK, recursive=True)
#
# os.mkdir()
# for file in itertools.chain(CXX_HEADERS, CXX_SOURCES):
#     shutil.copy(CXX_SYMLINK / file, CXX_DEST / file)

shutil.copytree(CXX_SYMLINK, CXX_DEST)