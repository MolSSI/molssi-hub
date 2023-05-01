# -*- coding: utf-8 -*-

"""
chemhub
Container hub for computational molecular science
"""

import textwrap

wrap_text = textwrap.TextWrapper(width=120)
wrap_stdout = textwrap.TextWrapper(width=120)

# Handle versioneer
from ._version import get_versions  # noqa: E402

__author__ = """Mohammad Mostafanejad"""
__email__ = "smostafanejad@vt.edu"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
