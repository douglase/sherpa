# -*- coding: utf-8 -*-
#
# Sherpa documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 19 16:30:00 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
# import shlex

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

import sherpa

# For now include the '+...' part of the version string
# and that I can drop the '+...' part.
#
sherpa_release = sherpa._version.get_versions()['version']
sherpa_version = sherpa_release[:sherpa_release.find('+')]

# For sherpaext
sys.path.insert(0, os.path.abspath('.'))

# For run-time code used in the documentation
#   TODO: is there a better way to do this?
sys.path.insert(0, os.path.join(os.path.abspath('.'), 'code'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',

    # currently do not look at coverage
    # 'sphinx.ext.coverage',

    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',

    'IPython.sphinxext.ipython_console_highlighting',

    # does ipython directive properly handle figure location;
    # apparently not
    # 'IPython.sphinxext.ipython_directive',
    #
    'sherpaext.ipython_directive',

    'numpydoc.numpydoc'
]

# Stop the error messages about
#   Unknown directive type "autosummary"
#
# Taken from https://github.com/phn/pytpm/issues/3#issuecomment-12133978
#
numpydoc_show_class_members = False

# It looks like something has changed, so that it is easier (for now)
# to use the default location for images (html_static_path) than
# set one.
#
# ipython_savefig_dir = ['_generated']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Sherpa'
copyright = u'2016, Chandra X-ray Center, Smithsonian Astrophysical Observatory'
author = u'Chandra X-ray Center, Smithsonian Astrophysical Observatory'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = sherpa_version
# The full version, including alpha/beta/rc tags.
release = sherpa_release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# Define standard header/footers.

rst_prolog = ""

rst_epilog = ""

renamed_rst_epilog = """

.. _AstroPy: http://www.astropy.org/
.. _ChIPS: http://cxc.harvard.edu/chips/
.. _CIAO: http://cxc.harvard.edu/ciao/
.. _crates: http://cxc.harvard.edu/ciao/ahelp/crates.html
.. _CXC: http://cxc.harvard.edu/
.. _DS9: http://ds9.si.edu/
.. _FFTW: http://www.fftw.org/
.. _FITS: http://fits.gsfc.nasa.gov/
.. _IPython: http://ipython.org/
.. _matplotlib: http://matplotlib.org/
.. _PyFITS: http://www.stsci.edu/institute/software_hardware/pyfits
.. _Sphinx: http://sphinx.pocoo.org/
.. _Xspec: https://heasarc.gsfc.nasa.gov/xanadu/xspec/

"""

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'alabaster'

# For when/if we use ReadTheDocs, based on
# http://docs.readthedocs.org/en/latest/theme.html
#
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    # html_theme_options = {}
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Sherpadoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'Sherpa.tex', u'Sherpa Documentation',
   u'Chandra X-ray Center, Smithsonian Astrophysical Observatory', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sherpa', u'Sherpa Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'Sherpa', u'Sherpa Documentation',
   author, 'Sherpa', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False
