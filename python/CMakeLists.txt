cmake_minimum_required(VERSION 3.4.0)
project(sample_bindings LANGUAGES C CXX)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

include(GNUInstallDirs)

# Fetch pybind11
include(FetchContent)

FetchContent_Declare(
  pybind11
  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.6.2.tar.gz
  URL_HASH SHA256=8ff2fff22df038f5cd02cea8af56622bc67f5b64534f1b83b9f133b8366acff2
)
FetchContent_MakeAvailable(pybind11)


pybind11_add_module(pybind_module MODULE
    sample_bindings/pybind_module.cpp
    )
install(TARGETS pybind_module DESTINATION .)

add_subdirectory(sample_bindings/_Rectangle)

# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")