
def test_import():
    from sample_bindings import pybind_module


def test_import2():
    from sample_bindings import add, subtract

def test_pybind_module():
    from sample_bindings import add, subtract
    assert add(1, 1) == 2
    assert subtract(2, 1) == 1