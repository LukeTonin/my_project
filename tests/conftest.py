"""This file is automatically discovered and used by pytest.
It contains fixtures (i.e setup functions that can be used anywhere in the test directory.)
There is no need to import the fixtures in the test modules. Add them as input to the
test function and the data will be available.

e.g :
    def test_my_function(short_input_data_stream):
        assert condition
"""
import pytest

test_data_dir = join('tests', 'test_data')

@pytest.fixture(scope='session')
def fixture_example():
    return 20


# Reminder. Could be useful.
@pytest.yield_fixture(autouse=True, scope='session')
def test_suite_cleanup_thing():
    # setup
    yield
    # teardown - put your command here
