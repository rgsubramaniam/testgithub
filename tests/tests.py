from src.maths import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_mul():
    assert mul(5,3)==15
    assert mul(2,3)==6
