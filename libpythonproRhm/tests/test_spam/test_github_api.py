from unittest.mock import Mock

import pytest

from libpythonproRhm import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/3457114?v=4'
    resp_mock.json.return_value = {
        'login': 'renzo',
        'id': 402714,
        'node_id': 'MDQ6VXNlcjQwMjcxNA==',
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonproRhm.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('renzo')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
