#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles


class label_role_node(nodes.General, nodes.TextElement):
    pass


def visit_tag_node(self, node):
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'span', '', **atts))


def depart_tag_node(self, node):
    self.body.append('</span>')


node_map = {
    'label-default': label_role_node,
    'label-primary': label_role_node,
    'label-success': label_role_node,
    'label-info': label_role_node,
    'label-warning': label_role_node,
    'label-danger': label_role_node,
}


def label_generic_role(name, rawtext, text, lineno, inliner):
    unescaped = text.replace('\x00`', '`')
    children, msgs = inliner.parse(unescaped, lineno, inliner, inliner.parent)
    node = node_map[name]()

    if not node:  # pragma: no cover
        raise ValueError('Unknown node ' + name)

    node += children
    node['classes'] += ['label', name]

    return [node], []


def setup(app):
    app.add_node(label_role_node, html=(visit_tag_node, depart_tag_node))

    roles.register_local_role('label-default', label_generic_role)
    roles.register_local_role('label-primary', label_generic_role)
    roles.register_local_role('label-success', label_generic_role)
    roles.register_local_role('label-info', label_generic_role)
    roles.register_local_role('label-warning', label_generic_role)
    roles.register_local_role('label-danger', label_generic_role)
