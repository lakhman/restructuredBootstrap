#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from .roles import inline_heading


class list_group(nodes.General, nodes.Element):
    pass


class list_group_item(nodes.General, nodes.Element):
    pass


def visit_list_group(self, node):
    tag = 'div'
    self.body.append(self.starttag(node, tag, CLASS=" ".join(node['classes'])))


def depart_list_group(self, node):
    tag = 'div'
    self.body.append('</%s>\n' % tag)


def visit_list_item(self, node):
    tag = 'a'
    html_attr = {'CLASS': " ".join(node['classes'])}

    if 'href' in node and node['href'] is not None:
        html_attr['href'] = node['href']

    if 'target' in node:
        html_attr['target'] = node['target']

    if node['href'] is None:
        tag = 'div'

    if 'button' in node:
        tag = 'button'
        html_attr['type'] = 'button'
        if 'href' in html_attr:
            del html_attr['href']
        if 'target' in html_attr:
            del html_attr['target']

    self.body.append(self.starttag(node, tag, **html_attr))


def depart_list_item(self, node):
    # Required to add a new line after unwrapped text (test_button, test_href)
    if not self.body[-1].endswith("\n"):
        self.body[-1] += "\n"

    tag = 'a'
    if node['href'] is None:
        tag = 'div'

    if 'button' in node:
        tag = 'button'

    self.body.append('</%s>\n' % tag)


class ListGroup(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()

        node = list_group()
        node['classes'] = ['list-group']
        node['classes'] += self.options.get('class', [])

        if self.arguments:
            node['classes'] += directives.class_option(self.arguments[0])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class BaseListGroupItem(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'href': directives.uri,
        'target': directives.unchanged,
        'button': directives.flag,
    }
    node_classes = None
    class_map = {
        'success',
        'info',
        'warning',
        'danger',
    }

    def run(self):
        self.assert_has_content()

        node = list_group_item()
        node['classes'] = ['list-group-item']
        node['classes'] += self.options.get('class', [])
        if self.node_classes is not None:
            node['classes'] += self.node_classes

        node['href'] = self.options.get('href', None)

        if 'target' in self.options:
            node['target'] = self.options.get('target')

        if 'button' in self.options:
            node['button'] = self.options.get('button')

        if self.arguments:
            node['classes'] += directives.class_option(self.arguments[0])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        # Unwrap heading nodes and add classes
        headings = node.traverse(inline_heading.heading_role_node)
        for i, heading in enumerate(headings):
            heading['classes'] += ['list-group-item-heading']
            if isinstance(heading.parent, nodes.paragraph):
                heading.parent.replace_self(heading)

        if len(node.children) > 1:
            paragraphs = node.traverse(nodes.paragraph)
            for i, p in enumerate(paragraphs):
                p['classes'] += ['list-group-item-text']

        return [node]


class ListGroupItemSuccess(BaseListGroupItem):
    node_classes = ['list-group-item-success']


class ListGroupItemInfo(BaseListGroupItem):
    node_classes = ['list-group-item-info']


class ListGroupItemWarning(BaseListGroupItem):
    node_classes = ['list-group-item-warning']


class ListGroupItemDanger(BaseListGroupItem):
    node_classes = ['list-group-item-danger']


def setup(app):
    app.add_node(list_group, html=(visit_list_group, depart_list_group))
    app.add_node(list_group_item, html=(visit_list_item, depart_list_item))

    app.add_directive('list-group', ListGroup)
    app.add_directive('list-group-item', BaseListGroupItem)
    app.add_directive('list-group-item-success', ListGroupItemSuccess)
    app.add_directive('list-group-item-info', ListGroupItemInfo)
    app.add_directive('list-group-item-warning', ListGroupItemWarning)
    app.add_directive('list-group-item-danger', ListGroupItemDanger)
