from skit_auth import __version__
from skit_auth import utils


def test_package_version():
    assert utils.get_version() == __version__
