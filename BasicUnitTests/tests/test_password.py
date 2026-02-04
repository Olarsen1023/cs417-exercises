import pytest
from src.password import validate_password

def test_validate_password_valid():
     assert validate_password('Password123!') == True
     print("test_validate_password_valid passed")
def test_validate_password_boundary():
     assert validate_password('Pass1234') == True
     assert validate_password('Pass123') == False
     print("test_validate_password_boundary passed")
def test_validate_password_non_string():
     with pytest.raises(TypeError):
         validate_password(12345678)
         print("test_validate_password_non_string passed")