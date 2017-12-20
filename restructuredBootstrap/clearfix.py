#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class Clearfix(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged
    }

    def run(self):
        node = nodes.container()
        node['classes'] = ['clearfix']

        if self.arguments:
            classes = directives.class_option(self.arguments[0])
            node['classes'].extend(classes)
        node['classes'] += self.options.get('class', [])
        self.add_name(node)

        return [node]


def setup(app):
    app.add_directive('clearfix', Clearfix)
