#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles


class kbd_node(nodes.Inline, nodes.TextElement):
    tagname = 'kbd'


class small_node(nodes.Inline, nodes.TextElement):
    tagname = 'small'


class ins_node(nodes.Inline, nodes.TextElement):
    tagname = 'ins'


class mark_node(nodes.Inline, nodes.TextElement):
    tagname = 'mark'


class strike_node(nodes.Inline, nodes.TextElement):
    tagname = 's'


class del_node(nodes.Inline, nodes.TextElement):
    tagname = 'del'


class underline_node(nodes.Inline, nodes.TextElement):
    tagname = 'u'


class var_node(nodes.Inline, nodes.TextElement):
    tagname = 'var'


class samp_node(nodes.Inline, nodes.TextElement):
    tagname = 'samp'


class sup_node(nodes.Inline, nodes.TextElement):
    tagname = 'sup'


class sub_node(nodes.Inline, nodes.TextElement):
    tagname = 'sub'


def visit_tag_node(self, node):
    self.body.append(self.starttag(node, node.tagname, ''))


def depart_tag_node(self, node):
    self.body.append('</%s>' % node.tagname)


node_map = {
    'small': small_node,
    'kbd': kbd_node,
    'ins': ins_node,
    'mark': mark_node,
    'strike': strike_node,
    'del': del_node,
    'underline': underline_node,
    'var': var_node,
    'samp': samp_node,
    'sup': sup_node,
    'sub': sub_node,
}


def generic_role(name, rawtext, text, lineno, inliner):
    unescaped = text.replace('\x00`', '`')
    children, msgs = inliner.parse(unescaped, lineno, inliner, inliner.parent)
    node = node_map[name]()

    if not node:  # pragma: no cover
        raise ValueError('Unknown node ' + name)

    node += children

    return [node], []


def setup(app):
    # small
    roles.register_local_role('small', generic_role)
    app.add_node(small_node, html=(visit_tag_node, depart_tag_node))

    # kbd
    roles.register_local_role('kbd', generic_role)
    app.add_node(kbd_node, html=(visit_tag_node, depart_tag_node))

    # ins
    roles.register_local_role('ins', generic_role)
    app.add_node(ins_node, html=(visit_tag_node, depart_tag_node))

    # mark
    roles.register_local_role('mark', generic_role)
    app.add_node(mark_node, html=(visit_tag_node, depart_tag_node))

    # strike
    roles.register_local_role('strike', generic_role)
    app.add_node(strike_node, html=(visit_tag_node, depart_tag_node))

    # del
    roles.register_local_role('del', generic_role)
    app.add_node(del_node, html=(visit_tag_node, depart_tag_node))

    # underline
    roles.register_local_role('underline', generic_role)
    app.add_node(underline_node, html=(visit_tag_node, depart_tag_node))

    # var
    roles.register_local_role('var', generic_role)
    app.add_node(var_node, html=(visit_tag_node, depart_tag_node))

    # samp
    roles.register_local_role('samp', generic_role)
    app.add_node(samp_node, html=(visit_tag_node, depart_tag_node))

    # sup
    roles.register_local_role('sup', generic_role)
    app.add_node(sup_node, html=(visit_tag_node, depart_tag_node))

    # sub
    roles.register_local_role('sub', generic_role)
    app.add_node(sub_node, html=(visit_tag_node, depart_tag_node))
