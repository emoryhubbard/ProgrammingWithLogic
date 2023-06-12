import pytest
from loan import is_approved

def test_is_approved():
    assert is_approved(8, 7, 8, 1)
    assert is_approved(5, 2, 7, 5)
    assert not is_approved(8, 2, 8, 3)
    assert is_approved(2, 4, 1, 7)
    assert not is_approved(4, 5, 5, 3)
    

pytest.main(["-v", "--tb=line", "-rN", __file__])