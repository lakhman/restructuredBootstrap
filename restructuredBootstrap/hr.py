#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class hr(nodes.General, nodes.Element):
    pass


def visit_hr(self, node):
    if len(node['classes']):
        classes = " ".join(node['classes'])
        self.body.append('<%s class="%s"/>\n' % (node['tag'], classes))
    else:
        self.body.append('<%s />\n' % node['tag'])

    raise nodes.SkipNode


class BaseRule(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        'class': directives.class_option,
    }

    node_class = None
    tag = None

    def run(self):
        node = hr("", **self.options)
        node['classes'] += self.options.get('class', [])
        node['tag'] = self.tag

        if self.arguments:
            node['classes'] += directives.class_option(self.arguments[0])

        return [node]


class Hr(BaseRule):
    tag = 'hr'


class Br(BaseRule):
    tag = 'br'


def setup(app):
    app.add_node(hr, html=(visit_hr, None))
    app.add_directive('hr', Hr)
    app.add_directive('br', Br)
