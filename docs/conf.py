# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # "sphinx_autodoc_typehints",  # Must come *after* sphinx.ext.napoleon.
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
if os.getenv("SPELLCHECK"):
    extensions += ("sphinxcontrib.spelling",)
    spelling_show_suggestions = True
    spelling_lang = "en_US"

source_suffix = ".rst"
master_doc = "index"
project = "interdoc"
year = "2019"
author = "Interdoc contributors"
copyright = "{0}, {1}".format(year, author)
version = release = "0.1.0"

pygments_style = "trac"

extlinks = {
    "issue": ("https://github.com/metatooling/interdoc/issues/%s", "#"),
    "pr": ("https://github.com/metatooling/interdoc/pull/%s", "PR #"),
}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"


html_theme = "sphinx_rtd_theme"


html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {"**": ["searchbox.html", "globaltoc.html", "sourcelink.html"]}
html_short_title = "%s-%s" % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = True

autoapi_dirs = ["../src/interdoc"]
