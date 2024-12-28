from src.maths import add,mul

def test_add(a,b):
    assert add(2,3)==5
    assert add(-1,2)==1

def test_mul(a,b):
    assert mul(4,1)==4
    assert mul(3,2)==6
