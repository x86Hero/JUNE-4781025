from appcode import app_module

def test_count():
    assert app_module.count("a","a") == 1
    assert app_module.count("1",1) == None