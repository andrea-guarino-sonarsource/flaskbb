from flaskbb.cli.main import fibonacci

def test_fibonacci():
    assert fibonacci(10) == 55
