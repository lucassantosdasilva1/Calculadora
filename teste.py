import pytest
from calc import soma
from calc import subs
from calc import divs
from calc import mult

def test_soma ():
	assert soma (1,1)==2
	assert soma (-1,2)==1

def test_subs ():
	assert subs (2,1)==1
	assert subs (3,2)==1
	assert subs (5,2.5)==2.5
	assert subs (10,5.2)==4.8

def test_div ():
	assert divs (10,5)==2
	assert divs (25,5)==5
	assert divs (100,50)==2

def test_mult ():
	assert mult (50,10)==500
	assert mult (1000,1)==1000
	assert mult (50,2)==100
