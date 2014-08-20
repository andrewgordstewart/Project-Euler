from nose.tools import *
from proj_eul.prime_tools import sieve

def test_sieve():
    assert_equal(sieve.primes_to_n(20), [2, 3, 5, 7, 11, 13, 17, 19])
    assert_equal(sieve.primes_to_n(3), [2, 3], 3)

def test_naive_is_prime():
    assert_equal(sieve.naive_is_prime(2), True)
    assert_equal(sieve.naive_is_prime(3), True)
    assert_equal(sieve.naive_is_prime(5), True)
    assert_equal(sieve.naive_is_prime(4), False)
    assert_equal(sieve.naive_is_prime(12), False)

def test_is_prime():
    assert_equal(sieve.is_prime(2), {1: False, 2: True})
    assert_equal(sieve.is_prime(3), {1: False, 2: True, 3: True})
