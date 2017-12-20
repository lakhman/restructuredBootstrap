#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles


class text_cx_role_node(nodes.General, nodes.TextElement):
    pass


def visit_tag_node(self, node):
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'span', '', **atts))


def depart_tag_node(self, node):
    self.body.append('</span>')


node_map = {
    'text-muted': text_cx_role_node,
    'text-primary': text_cx_role_node,
    'text-success': text_cx_role_node,
    'text-info': text_cx_role_node,
    'text-warning': text_cx_role_node,
    'text-danger': text_cx_role_node,
}


def text_cx_generic_role(name, rawtext, text, lineno, inliner):
    unescaped = text.replace('\x00`', '`')
    children, msgs = inliner.parse(unescaped, lineno, inliner, inliner.parent)
    node = node_map[name]()

    if not node:  # pragma: no cover
        raise ValueError('Unknown node ' + name)

    node += children
    node['classes'] += [name]

    return [node], []


def setup(app):
    app.add_node(text_cx_role_node, html=(visit_tag_node, depart_tag_node))

    roles.register_local_role('text-muted', text_cx_generic_role)
    roles.register_local_role('text-primary', text_cx_generic_role)
    roles.register_local_role('text-success', text_cx_generic_role)
    roles.register_local_role('text-info', text_cx_generic_role)
    roles.register_local_role('text-warning', text_cx_generic_role)
    roles.register_local_role('text-danger', text_cx_generic_role)
