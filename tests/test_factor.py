from nose.tools import *
from proj_eul.prime_tools import factor

_prime_decomp = factor.prime_decomposition
_prime_factors_with_mult = factor.prime_factors_with_multiplicity

def test_prime_decomp():
    assert_equals(_prime_decomp(2), {2:1})
    assert_equals(_prime_decomp(3), {3:1})
    assert_equals(_prime_decomp(4), {2:2})
    assert_equals(_prime_decomp(12), {2:2, 3:1})

def test_prime_factors_with_mult():
    assert_equals(_prime_factors_with_mult(2), [2])
    assert_equals(_prime_factors_with_mult(4), [2, 2])
    assert_equals(_prime_factors_with_mult(12), [2, 2, 3])
    assert_equals(_prime_factors_with_mult(10), [2, 5])
