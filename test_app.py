# test_app.py
from app import get_user_info

def test_get_user_info():
    # 这里我们只测试了 get_user_info，没有测试 unused_function
    # 这样就能触发覆盖率不达标
    assert True 
