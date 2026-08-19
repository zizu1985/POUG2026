"""
Pytest configuration module.
"""

# Edit this list to add new, parametrized, cli options to pytest. You can then
# use them as fixtures in any of your test functions.
_cli_args = ['pathdir','db_name','level_support','stage','db_size', 'os_version','db_host']
_cli_args_optional = ['db_port']

import pytest
import oracledb
from strip_ansi import strip_ansi


def pytest_addoption(parser):
    for arg in _cli_args:
        if arg in ['db_name','db_size','os_version']:
            parser.addoption('--' + arg, type=str, required=False)
        else:
            parser.addoption('--' + arg, type=str, required=True)
    for arg in _cli_args_optional:
        parser.addoption('--' + arg, type=str, required=False)


def pytest_generate_tests(metafunc):
    for arg in _cli_args:
        if arg in metafunc.fixturenames:
            value = getattr(metafunc.config.option, arg)
            metafunc.parametrize(arg, [value])

@pytest.fixture
def db_port(request):
    return request.config.getoption("--db_port") or ""


@pytest.fixture(scope="session")
def oracle_conn(request):
    o = request.config.getoption
    if o("--db_name") and o("--db_host") and o("--db_port"):
        db_name = strip_ansi(o("--db_name"))
        host = strip_ansi(o("--db_host"))
        domain = host.split(".", 1)[1]
        port = strip_ansi(o("--db_port"))
        db_service = db_name + '.' + domain

        dsn = f"{host}:{port}/{db_service}"
        conn = None
        try: 
            conn = oracledb.connect(user="LOGICMONITOR", password=f"L0g1cM0n1t0r$", dsn=dsn)
            yield conn
        finally:
            if conn is not None:
                conn.close()
    else:
        pytest.skip("No enough parameters to build database connection.")


@pytest.fixture
def stage(pytestconfig):
    return pytestconfig.getoption("stage")
    
@pytest.fixture(autouse=True)
def fun_test_prepare(stage, request):
    if request.node.get_closest_marker('test_prepare'):
        if request.node.get_closest_marker('test_prepare').args[0] == stage:
            return
    if request.node.get_closest_marker('test_installsw'):
        if request.node.get_closest_marker('test_installsw').args[0] == stage:
            return
    if request.node.get_closest_marker('test_createdb'):
        if request.node.get_closest_marker('test_createdb').args[0] == stage:
            return
    pytest.skip('Skipped')

def pytest_configure(config):
  config.addinivalue_line(
        "markers", "test_prepare(stage): run test if executed in proper stage",
  )
  config.addinivalue_line(
        "markers", "test_installsw(stage): run test if executed in proper stage",
  )
  config.addinivalue_line(
        "markers", "test_createdb(stage): run test if executed in proper stage",
  )