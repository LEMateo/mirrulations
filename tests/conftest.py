import mock
import pytest
import random
import string


@pytest.fixture(scope='session', autouse=True)
def mock_config():
    fake_config_dictionary = {
        'ip': '80.80.80.80',
        'port': '8080',
        'key': ''.join(random.choices(string.ascii_letters + string.digits, k=40)),
        'client_id': ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    }

    with mock.patch('mirrulations_core.config.read_value', side_effect=lambda v: fake_config_dictionary[v]) as f:
        yield f
