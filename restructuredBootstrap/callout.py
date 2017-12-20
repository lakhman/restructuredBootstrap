#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util import nested_parse_with_titles
from sphinx.util.nodes import set_source_info


class callout(nodes.General, nodes.Element):
    pass


def visit_callout(self, node):
    self.body.append(self.starttag(node, 'div'))


def depart_callout(self, node):
    self.body[-1] = self.body[-1].strip()
    self.body.append('\n</div>\n')


class BaseCallout(Directive):
    """
    Custom callouts can be styled as required, used in docs like block-quotes
    Requires a small CSS chunk as shown in the codepen

    - https://cpratt.co/twitter-bootstrap-callout-css-styles/
    - https://codepen.io/chrisdpratt/pen/IAymB
    """
    required_arguments, optional_arguments = 0, 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'title': directives.unchanged,
    }

    node_class = None

    def get_title_node(self):
        title_text = self.options.get('title', '')
        textnodes, msgs = self.state.inline_text(title_text, self.lineno)
        p = nodes.paragraph(title_text, '', *textnodes)
        p.source, p.line = (self.state_machine.get_source_and_line(self.lineno))
        p['classes'] = ['h4']

        return p

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = callout(text, **self.options)
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] += ['bs-callout', self.node_class]

        if 'title' in self.options:
            title = self.get_title_node()
            node += title

        nested_parse_with_titles(self.state, self.content, node)
        self.add_name(node)

        return [node]


class CalloutDefault(BaseCallout):
    node_class = 'bs-callout-default'


class CalloutPrimary(BaseCallout):
    node_class = 'bs-callout-primary'


class CalloutSuccess(BaseCallout):
    node_class = 'bs-callout-success'


class CalloutInfo(BaseCallout):
    node_class = 'bs-callout-info'


class CalloutWarning(BaseCallout):
    node_class = 'bs-callout-warning'


class CalloutDanger(BaseCallout):
    node_class = 'bs-callout-danger'


def setup(app):
    app.add_node(callout, html=(visit_callout, depart_callout))

    app.add_directive('callout', CalloutDefault)
    app.add_directive('callout-success', CalloutSuccess)
    app.add_directive('callout-primary', CalloutPrimary)
    app.add_directive('callout-info', CalloutInfo)
    app.add_directive('callout-warning', CalloutWarning)
    app.add_directive('callout-danger', CalloutDanger)
