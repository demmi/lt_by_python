import pytest
from alex.normalizer import normalize

test_cases = (('https://example.com:8080/a/b/c', 'https://example.com:8080/a/b/c'),
              ('example.com', 'http://example.com:80/'),
              (' ', 'http://localhost:80/'),
              ('//habr.com', 'http://habr.com:80/'),
              ('192.168.0.1', 'http://192.168.0.1:80/'),
              ('//localhost:22', 'http://localhost:22/'))


@pytest.mark.parametrize("uri, norm_uri", test_cases)
def test_normalizer(uri, norm_uri):
    assert normalize(uri) == norm_uri
