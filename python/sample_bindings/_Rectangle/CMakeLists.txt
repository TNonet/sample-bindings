# set(INCLUDE_DIR ../sample_bindings/src/include)
# set(HEADER_FILES ${INCLUDE_DIR}/Rectangle.h)
# file(GLOB rectangle_sources ${INCLUDE_DIR}/*.h)
# include_directories(INCLUDE_DIR)
# add_executable( ${PROJECT_NAME} ${HEADER_FILES} )
# target_include_directories(${PROJECT_NAME} PRIVATE INCLUDE_DIR)


include_directories(".")
add_cython_target(_Rectangle CXX )
add_library(_Rectangle MODULE ${_Rectangle})
python_extension_module(_Rectangle)

install(FILES _Rectangle.pxd DESTINATION ${site_packages})

install(TARGETS _Rectangle LIBRARY DESTINATION _Rectangle)