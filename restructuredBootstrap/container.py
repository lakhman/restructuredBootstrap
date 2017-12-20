#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.writers.html import HTMLTranslator


class BaseContainer(Directive):
    """
    Container contextual variants
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged
    }
    node_class = None

    def run(self):
        node = nodes.container()
        node['classes'] = [self.node_class]

        if self.arguments:
            try:
                classes = directives.class_option(self.arguments[0])
                node['classes'].extend(classes)
            except ValueError:
                err = 'Invalid class attribute value for "%s" directive: "%s".'
                raise self.error(err % (self.name, self.arguments[0]))
        node['classes'] += self.options.get('class', [])

        node['html_attributes'] = {}

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        return [node]


class Jumbotron(BaseContainer):
    node_class = 'jumbotron'


class PageHeader(BaseContainer):
    node_class = 'page-header'


class Well(BaseContainer):
    node_class = 'well'


class WellSm(BaseContainer):
    node_class = 'well well-sm'


def visit_container(self, node):
    """
    Remove the default "container" class from docutils
    html_attributes come from ButtonGroups and ButtonToolbars
    """
    if 'html_attributes' in node:
        html_attrs = node['html_attributes']
    else:
        html_attrs = {}

    self.body.append(self.starttag(node, 'div', CLASS='', **html_attrs))


def depart_container(self, node):
    if not len(node.children):
        # Tested via Clearfix directive (no content)
        self.body[-1] = self.body[-1].strip()
        self.body[-1] += '</div>\n'
    else:
        if not self.body[-1].endswith("\n"):
            self.body[-1] += "\n"
        self.body.append('</div>\n')


def setup(app):
    app.add_directive('jumbotron', Jumbotron)
    app.add_directive('page-header', PageHeader)
    app.add_directive('well', Well)
    app.add_directive('well-sm', WellSm)

    HTMLTranslator.visit_container = visit_container
    HTMLTranslator.depart_container = depart_container
