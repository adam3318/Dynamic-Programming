from pytest import *
from counting_sum1 import *

def test_nSum_valid_input():
    # Test valid input
	# TODO: Review values in assert statement
    assert nSum(5) == 15

def test_nSum_invalid_input():
    # Test invalid input
	# TODO: Review values in assert statement
    assert nSum(-1) == None

def test_nSum_specific_cases():
    # Test the case where n = 1
	# TODO: Review values in assert statement
    assert nSum(1) == 1

    # Test the case where n = 5
	# TODO: Review values in assert statement
    assert nSum(5) == 15

def test_nSum_specific_inputs():
    # Test for input with n = 5
	# TODO: Review values in assert statement
    assert nSum(5) == 15
    # Test for input with n = 10
	# TODO: Review values in assert statement
    assert nSum(10) == 55

def test_nSum_missing_input():
    # Test without input
    try:
        nSum()
    except TypeError:
        print("TypeError raised as expected")

def test_nSum_NaN_input():
    # Test NaN input
	# TODO: Review values in assert statement
    assert nSum(None) == None

def test_nSum_null_input():
    # Test null input
	# TODO: Review values in assert statement
    assert nSum(0) == 0

def test_nSum_extended():
    
	# TODO: Review values in assert statement
    assert nSum(1) == 1
	# TODO: Review values in assert statement
    assert nSum(2) == 3
	# TODO: Review values in assert statement
    assert nSum(3) == 6
	# TODO: Review values in assert statement
    assert nSum(4) == 10
	# TODO: Review values in assert statement
    assert nSum(5) == 15
	# TODO: Review values in assert statement
    assert nSum(6) == 21
	# TODO: Review values in assert statement
    assert nSum(7) == 28
	# TODO: Review values in assert statement
    assert nSum(8) == 36
	# TODO: Review values in assert statement
    assert nSum(9) == 45
	# TODO: Review values in assert statement
    assert nSum(10) == 55