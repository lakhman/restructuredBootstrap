#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles


class bg_role_node(nodes.General, nodes.TextElement):
    pass


def visit_tag_node(self, node):
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'span', '', **atts))


def depart_tag_node(self, node):
    self.body.append('</span>')


node_map = {
    'bg-primary': bg_role_node,
    'bg-success': bg_role_node,
    'bg-info': bg_role_node,
    'bg-warning': bg_role_node,
    'bg-danger': bg_role_node,
}


def bg_generic_role(name, rawtext, text, lineno, inliner):
    unescaped = text.replace('\x00`', '`')
    children, msgs = inliner.parse(unescaped, lineno, inliner, inliner.parent)
    node = node_map[name]()

    if not node:  # pragma: no cover
        raise ValueError('Unknown node ' + name)

    node += children
    node['classes'] += [name]

    return [node], []


def setup(app):
    app.add_node(bg_role_node, html=(visit_tag_node, depart_tag_node))

    roles.register_local_role('bg-primary', bg_generic_role)
    roles.register_local_role('bg-success', bg_generic_role)
    roles.register_local_role('bg-info', bg_generic_role)
    roles.register_local_role('bg-warning', bg_generic_role)
    roles.register_local_role('bg-danger', bg_generic_role)
