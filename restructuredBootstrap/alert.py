#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class alert(nodes.General, nodes.Element):
    pass


def visit_alert(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='alert', role='alert'))

    if node.dismissible:
        x = u'<button type="button" class="close" data-dismiss="alert" ' \
            u'aria-hidden="true" aria-label="Close">' \
            u'<span aria-hidden="true">&times;</span></button>\n'
        self.body.append(x)


def depart_alert(self, node):
    if not self.body[-1].endswith("\n"):
        self.body[-1] += "\n"
    self.body.append('</div>\n')


class BaseAlert(Directive):
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'dismissible': directives.flag,
    }

    node_class = None

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = alert(text, **self.options)
        node['classes'] += ['alert']
        node['classes'] += [self.node_class]
        node['classes'] += self.options.get('class', [])

        node.dismissible = False
        if 'dismissible' in self.options:
            node['classes'] += ['alert-dismissible']
            node.dismissible = True

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        if len(node.children):
            node.children[0]['classes'] += ['first']

        refs = node.traverse(nodes.reference)
        for ref in refs:
            ref['classes'] += ['alert-link']

        return [node]


class AlertSuccess(BaseAlert):
    node_class = 'alert-success'


class AlertInfo(BaseAlert):
    node_class = 'alert-info'


class AlertWarning(BaseAlert):
    node_class = 'alert-warning'


class AlertDanger(BaseAlert):
    node_class = 'alert-danger'


def setup(app):
    app.add_node(alert, html=(visit_alert, depart_alert))

    app.add_directive('alert-success', AlertSuccess)
    app.add_directive('alert-info', AlertInfo)
    app.add_directive('alert-warning', AlertWarning)
    app.add_directive('alert-danger', AlertDanger)
