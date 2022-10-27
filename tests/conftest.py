import pytest


def pytest_addoption(parser):
    parser.addoption("--baseurl", action="store", default="http://localhost:8080/api/v1",
                     help="Type the base URL: http://someurl.com. Default is http://localhost:8080/api/v1")


@pytest.fixture()
def get_base_url(request):
    obtained_base_url = request.config.getoption("--baseurl")
    return obtained_base_url
