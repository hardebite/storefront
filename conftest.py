
# def pytest_configure(config):
#     import src.core # NB this causes `src/core/__init__.py` to run
#     # set up any "aliases" (optional...)
#     import sys
#     sys.modules['core'] = sys.modules['src.core']

import sys
sys.path[0] = '/usr/exampleUser/Documents/foo'