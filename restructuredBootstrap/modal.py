#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import nested_parse_with_titles, set_source_info


class modal(nodes.General, nodes.Element):
    pass


class modal_header(nodes.General, nodes.Element):
    pass


class modal_body(nodes.General, nodes.Element):
    pass


class modal_footer(nodes.General, nodes.Element):
    pass


def visit_modal_container(self, node):
    html_attrs = {
        "tabindex": "-1",
        "role": "dialog",
        "class": " ".join(node['classes'])
    }
    self.body.append(self.starttag(node, 'div', **html_attrs))

    dialog_classes = ["modal-dialog"]
    if 'lg' in node:
        dialog_classes += ["modal-lg"]
    self.body.append(
        self.starttag(
            nodes.container(),
            'div',
            CLASS=" ".join(dialog_classes),
            role='document'))

    self.body.append(
        self.starttag(nodes.container(), 'div', CLASS="modal-content"))


def depart_modal_container(self, node):
    if not self.body[-1].endswith("\n"):
        self.body[-1] += "\n"
    self.body.append('</div>\n')
    self.body.append('</div>\n')
    self.body.append('</div>\n')


def visit_modal_header(self, node):
    close_btn = '<button type="button" class="close" data-dismiss="modal" aria-label="Close">' \
                '<span aria-hidden="true">&times;</span>' \
                '</button>\n'

    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'div', **atts))
    self.body.append(close_btn)


def depart_modal_header(self, node):
    self.body.append('</div>\n')


def visit_modal_body(self, node):
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'div', **atts))


def depart_modal_body(self, node):
    self.body.append('</div>\n')


def visit_modal_footer(self, node):
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'div', **atts))


def depart_modal_footer(self, node):
    close_class = " ".join(
        node['close-class']) if 'close-class' in node else 'default'
    close_text = node['close-text'] if 'close-text' in node else 'Close'
    self.body.append(
        '<button type="button" class="btn btn-%s" '
        'data-dismiss="modal">%s</button>\n'
        % (close_class, close_text))
    self.body.append('</div>\n')


class ModalContainer(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'lg': directives.flag,
    }

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = modal(text, **self.options)
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] += ['modal', 'fade']
        node['classes'] += self.options.get('class', [])

        if self.arguments:
            node['classes'] += directives.class_option(self.arguments[0])

        if 'name' not in self.options:
            raise self.warning('A modal must have a "name" '
                               '(to be referenced by).')

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        return [node]


class ModalHeader(Directive):
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = modal_header(text, **self.options)
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] += ['modal-header']
        node['classes'] += self.options.get('class', [])

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        if len(node.children) == 1:
            node.children[0]['classes'] += ['h4', 'modal-title']

        return [node]


class ModalBody(Directive):
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = modal_body(text, **self.options)
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] += ['modal-body']
        node['classes'] += self.options.get('class', [])

        nested_parse_with_titles(self.state, self.content, node)

        self.add_name(node)

        return [node]


class ModalFooter(Directive):
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'close-class': directives.class_option,
        'close-text': directives.unchanged,
    }

    def run(self):
        text = '\n'.join(self.content)

        node = modal_footer(text, **self.options)
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] += ['modal-footer']
        node['classes'] += self.options.get('class', [])

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        return [node]


def setup(app):
    app.add_node(modal, html=(visit_modal_container, depart_modal_container))
    app.add_node(modal_header, html=(visit_modal_header, depart_modal_header))
    app.add_node(modal_body, html=(visit_modal_body, depart_modal_body))
    app.add_node(modal_footer, html=(visit_modal_footer, depart_modal_footer))

    app.add_directive('modal', ModalContainer)
    app.add_directive('modal-header', ModalHeader)
    app.add_directive('modal-body', ModalBody)
    app.add_directive('modal-footer', ModalFooter)
