#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from .alert import setup as alert_setup
from .buttons import setup as buttons_setup
from .callout import setup as callout_setup
from .clearfix import setup as clearfix_setup
from .container import setup as container_setup
from .grid import setup as grid_setup
from .media import setup as media_setup
from .modal import setup as modal_setup
from .list_group import setup as list_group_setup
from .panel import setup as panel_setup
from .paragraph import setup as paragraph_setup
from .progress_bar import setup as progress_bar_setup
from .tabs import setup as tabs_setup
from .hr import setup as hr_setup
from .roles import setup as roles_setup
from .html_translator import BootstrapHTMLTranslator


# App setup for Sphinx
def setup(app):
    alert_setup(app)
    buttons_setup(app)
    callout_setup(app)
    clearfix_setup(app)
    container_setup(app)
    grid_setup(app)
    media_setup(app)
    modal_setup(app)
    list_group_setup(app)
    panel_setup(app)
    paragraph_setup(app)
    progress_bar_setup(app)
    tabs_setup(app)
    hr_setup(app)
    roles_setup(app)

    app.set_translator('html', BootstrapHTMLTranslator)
    app.set_translator('dirhtml', BootstrapHTMLTranslator)

    return {
        'version': '0.1',
        'parallel_read_safe': False,
        'parallel_write_safe': True
    }
