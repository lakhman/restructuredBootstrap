#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles


class heading_role_node(nodes.General, nodes.TextElement):
    pass


def visit_heading_role_node(self, node):
    """
    If wrapped in a p, we remove the outer wrapping and delete the closing tag
    If we're in a list item, add a .first class if more than 1 paragraph
    The first class can come from HTMLTranslatorOverrides:visit_list_item
    """
    heading_parent = node.parent
    parent_container = heading_parent.parent
    parent_container_is_list = isinstance(parent_container, nodes.list_item)
    is_first_in_list = parent_container.children.index(heading_parent) == 0
    add_first_class = len(parent_container.children) > 0 \
        and is_first_in_list \
        and parent_container_is_list

    if self.body[-1] in ['<p>', '<p class="first">']:
        if self.body[-1] == '<p class="first">' or add_first_class:
            node['classes'] += ['first']
        del self.body[-1]
    if len(self.context) and self.context[0] == '</p>\n':
        self.context[0] = ''
    self.body.append(
        self.starttag(node, 'p', '', CLASS=(" ".join(node['classes']))))


def depart_heading_role_node(self, node):
    self.body.append('</p>\n')


node_map = {
    'h1': heading_role_node,
    'h2': heading_role_node,
    'h3': heading_role_node,
    'h4': heading_role_node,
    'h5': heading_role_node,
    'h6': heading_role_node,
}


def heading_role(name, rawtext, text, lineno, inliner):
    """
    Inside headings, you can use font awesome roles.
    You must escape them like so:

    :h6:`:fa:`book\` Heading 6 Role`

        or

    :h6:`:fa:\`book\` Heading 6 Role`

    View fa-heading test for more info.

    Replace "\`" (Slash + backtick) with a backtick - to allow inline roles
    """
    unescaped = text.replace('\x00`', '`')
    children, msgs = inliner.parse(unescaped, lineno, inliner, inliner.parent)
    node = node_map[name]()

    if not node:  # pragma: no cover
        raise ValueError('Unknown node ' + name)

    node += children
    node['classes'] += [name]

    return [node], []


def setup(app):
    visitors = (visit_heading_role_node, depart_heading_role_node)
    app.add_node(heading_role_node, html=visitors)

    roles.register_local_role('h1', heading_role)
    roles.register_local_role('h2', heading_role)
    roles.register_local_role('h3', heading_role)
    roles.register_local_role('h4', heading_role)
    roles.register_local_role('h5', heading_role)
    roles.register_local_role('h6', heading_role)
