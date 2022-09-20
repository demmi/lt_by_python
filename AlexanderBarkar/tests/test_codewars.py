import pytest
from AlexanderBarkar.codewars import counting_valleys
from AlexanderBarkar.codewars import user_friendly_size

cases = (('UFFFD', 0), ('DFFFD', 0), ('UFFFU', 0), ('DFFFU', 1), ('UFFDDFDUDFUFU', 1),
         ('UFFDDFDUDFUFUUFFDDFDUDFUFU', 2), ('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU', 3),
         ('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU', 4),
         ('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU', 6))

file_cases = ((1024, '1.00 kB'), (9999, '9.76 kB'), (9999999, '9.54 MB'), (9999999999, '9.31 GB'),
              (99999999999999, '90.95 TB'), ('9999999999', '9.31 GB'), ('/etc/services', '662.09 kB'))


@pytest.mark.parametrize('path, solution', cases)
def test_counting_valleys(path, solution):
    assert counting_valleys(path) == solution


@pytest.mark.parametrize('file_size, expected_size', file_cases)
def test_user_friendly_size(file_size, expected_size):
    assert user_friendly_size(file_size) == expected_size
