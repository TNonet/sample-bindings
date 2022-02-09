# distutils: language = c++
# distutils: include_dirs = RECTANGLE_HEADERS

# Source: https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#cythonize-arguments

cdef extern from "../src2/include/Rectangle.h" namespace "shapes":

    cdef cppclass Rectangle:
        Rectangle() except +
        Rectangle(int, int, int, int) except +
        int x0, y0, x1, y1
        int getArea()
        void getSize(int* width, int* height)
        void move(int, int)
