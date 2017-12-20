#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class progress_stack(nodes.container):
    pass


class progress_bar(nodes.General, nodes.Element):
    pass


def visit_progress_stack(self, node):
    self.body.append(self.starttag(node, 'div', '\n'))


def depart_progress_stack(self, node):
    self.body.append('</div>')


def visit_progress_bar(self, node):
    pb_base_string = 'progress-bar-%s'
    label = node['label']
    attributes = []

    for i, nodeclass in enumerate(node['classes']):
        if nodeclass == 'striped':
            node['classes'][i] = (pb_base_string % nodeclass)

    attributes.append('role="progressbar"')
    attributes.append('aria-valuenow="%d"' % int(node['value']))
    attributes.append('aria-valuemin="%d"' % int(node['value_min']))
    attributes.append('aria-valuemax="%d"' % int(node['value_max']))
    attributes.append('style="width: %d%%;"' % int(node['value']))

    # may or may not be in a progress-stack, if stacked, don't append parent div
    if not isinstance(node.parent, progress_stack):
        self.body.append('<div class="progress">\n')

    html_attrs = (" ".join(node['classes']), " ".join(attributes), label)
    self.body.append('<div class="%s" %s>%s</div>\n' % html_attrs)

    if not isinstance(node.parent, progress_stack):
        self.body.append('</div>')

    raise nodes.SkipNode


class BaseProgressBar(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'label': directives.unchanged,
        'value': directives.unchanged_required,
        'min': directives.unchanged_required,
        'max': directives.unchanged_required
    }
    node_class = None

    def run(self):
        node = progress_bar()
        node['classes'].append('progress-bar')

        if self.node_class is not None:
            node['classes'].append(self.node_class)

        node['classes'] += self.options.get('class', '')
        node['value_min'] = self.options.get('min_value', '0')
        node['value_max'] = self.options.get('max_value', '100')
        node['value'] = self.options.get('value', '50')
        node['label'] = self.options.get('label', '')

        if self.arguments:
            node['value'] = self.arguments[0].rstrip(' %')

        self.add_name(node)

        return [node]


class ProgressStack(Directive):
    """
    Used to stack progress bars
    """
    required_arguments, optional_arguments = 0, 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()
        node = progress_stack(self.content)
        node['classes'] += ['progress']
        node['classes'] += self.options.get('class', [])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class ProgressBarPrimary(BaseProgressBar):
    node_class = None


class ProgressBarSuccess(BaseProgressBar):
    node_class = 'progress-bar-success'


class ProgressBarInfo(BaseProgressBar):
    node_class = 'progress-bar-info'


class ProgressBarWarning(BaseProgressBar):
    node_class = 'progress-bar-warning'


class ProgressBarDanger(BaseProgressBar):
    node_class = 'progress-bar-danger'


def setup(app):
    app.add_directive('progress-stack', ProgressStack)
    app.add_directive('progress-bar', ProgressBarPrimary)
    app.add_directive('progress-bar-success', ProgressBarSuccess)
    app.add_directive('progress-bar-info', ProgressBarInfo)
    app.add_directive('progress-bar-warning', ProgressBarWarning)
    app.add_directive('progress-bar-danger', ProgressBarDanger)
    app.add_node(progress_bar, html=(visit_progress_bar, None))
    app.add_node(
        progress_stack, html=(visit_progress_stack, depart_progress_stack))
