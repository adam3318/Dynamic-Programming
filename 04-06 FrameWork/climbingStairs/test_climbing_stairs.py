from climbing_stairs_redstairs import climbing_stairs
from pytest import *


def test_climbing_stairs_valid_input():
    # Test valid input
    list = [False, True, False, True, True, False, False]
	# TODO: Review values in assert statement
    assert climbing_stairs(7,3,list) == 2

def test_climbing_stairs_invalid_input():
    # Test invalid input
    try:
        climbing_stairs(7,3,None)
    except:
        print("Invalid input")

def test_climbing_stairs_specific_inputs_of_red_stairs_list():
    # Test for input with no red stairs
    list = [False, False, False, False, False, False, False]
	# TODO: Review values in assert statement
    assert climbing_stairs(7,3,list) == 44
    # Test for input with all red stairs
    list = [True, True, True, True, True, True, True]
	# TODO: Review values in assert statement
    assert climbing_stairs(7,3,list) == 0
    # Test for input with some red stairs
    list = [False, True, False, True, True, False, False]
	# TODO: Review values in assert statement
    assert climbing_stairs(7,3,list) == 2

def test_climbing_stairs_missing_input():
    # Test without input
    try:
        climbing_stairs()
    except TypeError:
        print("type error")

def test_climbing_stairs_NaN_input():
    # Test NaN input
	# TODO: Review values in assert statement
    assert climbing_stairs(None, None, None) == None

def test_climbing_stairs_null_input():
    # Test null input
	# TODO: Review values in assert statement
    assert climbing_stairs(0,0,[]) == 1
