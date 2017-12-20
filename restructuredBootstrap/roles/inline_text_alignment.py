#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles


class text_align_role_node(nodes.General, nodes.TextElement):
    pass


def visit_tag_node(self, node):
    if self.body[-1] == '<p>':
        del self.body[-1]
    if len(self.context) and self.context[0] == '</p>\n':
        self.context[0] = ''
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'p', '', **atts))


def depart_tag_node(self, node):
    self.body.append('</p>\n')


node_map = {
    'text-left': text_align_role_node,
    'text-center': text_align_role_node,
    'text-right': text_align_role_node,
    'text-justify': text_align_role_node,
    'text-nowrap': text_align_role_node,
}


def text_alignment_generic_role(name, rawtext, text, lineno, inliner):
    unescaped = text.replace('\x00`', '`')
    children, msgs = inliner.parse(unescaped, lineno, inliner, inliner.parent)
    node = node_map[name]()

    if not node:  # pragma: no cover
        raise ValueError('Unknown node ' + name)

    node += children
    node['classes'] += [name]

    return [node], []


# http://docutils.sourceforge.net/docs/howto/rst-roles.html
def setup(app):
    app.add_node(text_align_role_node, html=(visit_tag_node, depart_tag_node))

    roles.register_local_role('text-left', text_alignment_generic_role)
    roles.register_local_role('text-center', text_alignment_generic_role)
    roles.register_local_role('text-right', text_alignment_generic_role)
    roles.register_local_role('text-justify', text_alignment_generic_role)
    roles.register_local_role('text-nowrap', text_alignment_generic_role)
