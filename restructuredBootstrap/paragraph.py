#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.body import Container


class Lead(Container):
    required_arguments, optional_arguments = 0, 0
    has_content = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged
    }
    node_class = None

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        if len(self.content) == 1:
            node = nodes.paragraph(text, **self.options)
        else:
            node = nodes.container(text, **self.options)

        node['classes'] += ['lead']
        node['classes'] += self.options.get('class', [])

        if self.node_class:
            node['classes'] += [self.node_class]

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        return [node]


class LeadMuted(Lead):
    node_class = 'text-muted'


class LeadPrimary(Lead):
    node_class = 'text-primary'


class LeadSuccess(Lead):
    node_class = 'text-success'


class LeadInfo(Lead):
    node_class = 'text-info'


class LeadWarning(Lead):
    node_class = 'text-warning'


class LeadDanger(Lead):
    node_class = 'text-danger'


def setup(app):
    app.add_directive('lead', Lead)
    app.add_directive('lead-muted', LeadMuted)
    app.add_directive('lead-primary', LeadPrimary)
    app.add_directive('lead-success', LeadSuccess)
    app.add_directive('lead-info', LeadInfo)
    app.add_directive('lead-warning', LeadWarning)
    app.add_directive('lead-danger', LeadDanger)
