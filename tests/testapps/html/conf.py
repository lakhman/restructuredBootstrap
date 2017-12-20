# -*- coding: utf-8 -*-
import os, sys

# Shared options for our test configuration
extensions = ['restructuredBootstrap']

# We override layout.html to a blank page for testing
templates_path = ['_templates']

# Add our custom pygments style
pygments_style = 'restructuredBootstrap.custom_pygments_style.StackOverflowStyle'

# Configuration Block option
highlight_language = 'default'

# Configuration Block option
config_block = {
    # http://pygments.org/docs/lexers/#lexers-for-python-and-related-languages
    'shell': 'Shell',
}

# For 1.4
html_use_smartypants = False
