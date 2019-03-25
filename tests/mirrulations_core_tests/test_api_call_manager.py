import pytest
import requests_mock
from mock import *
from mirrulations_core.api_call_manager import APICallManager
import mirrulations_core.config as config

man = APICallManager(config.read_value('CLIENT', 'API_KEY'))


@pytest.fixture
def mock_req():
    with requests_mock.Mocker() as m:
        yield m


def set_time():
    mock_time = Mock()
    mock_time.return_value = None
    return mock_time


def test_success(mock_req):
    mock_req.get('http://docurl', status_code=200, text='{}')
    assert man.make_call('http://docurl').text == '{}'


@patch('time.sleep', set_time())
def test_user_out_of_api_calls_sleeps(mock_req):
    mock_req.register_uri('GET',
                          'http://docurl',
                          [{'text': 'resp1', 'status_code': 429}, {'text': '{}', 'status_code': 200}])
    assert man.make_call('http://docurl').text == '{}'
