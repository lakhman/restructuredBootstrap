#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from .inline_badge import setup as inline_badge_setup
from .inline_heading import setup as inline_heading_setup
from .inline_text import setup as inline_text_setup
from .inline_label import setup as inline_label_setup
from .inline_abbr import setup as inline_abbr_setup
from .inline_text_alignment import setup as inline_text_alignment_setup
from .inline_text_contextual import setup as inline_text_contextual_setup
from .inline_text_transform import setup as inline_text_transform_setup
from .inline_background_contextual import setup as inline_background_contextual_setup
from .fontawesome import setup as fontawesome_setup
from .inline_tooltip import setup as inline_tooltip_setup

################################################################################
# Setup for Sphinx
################################################################################
def setup(app):
    inline_text_setup(app)
    inline_abbr_setup(app)
    inline_heading_setup(app)
    inline_label_setup(app)
    inline_text_alignment_setup(app)
    inline_text_transform_setup(app)
    inline_text_contextual_setup(app)
    inline_badge_setup(app)
    inline_background_contextual_setup(app)
    inline_tooltip_setup(app)
    fontawesome_setup(app)
