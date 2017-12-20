#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles
import re


class abbr_node(nodes.Inline, nodes.TextElement):
    pass


def visit_abbr_node(self, node):
    self.body.append(self.starttag(node, 'abbr', '', title=node['title']))


def depart_abbr_node(self, node):
    self.body.append('</abbr>')


node_map = {
    'abbr': abbr_node,
}


def generic_role(name, rawtext, text, lineno, inliner):
    try:
        regex = r"([^<>]+)((?:[ \n]+|^)<(?![ \n])(([^<>]|\x00[<>])+)(?<![ \n\x00])>)"
        text_matches = re.match(regex, text)

        if text_matches is None:
            raise ValueError(
                "Invalid abbr text. "
                "Using a role within a role? try escaping the last back tick."
            )

        word = text_matches.group(1)
        title = text_matches.group(3)
        unescaped = word.replace('\x00`', '`')
        children, msgs = inliner.parse(unescaped, lineno, inliner,
                                       inliner.parent)
        for i, child in enumerate(children):
            if isinstance(child, nodes.Text):
                child = children.pop(i)
                new_child = nodes.Text(child.astext())
                children.insert(i, new_child)

        node = node_map[name]()
        node['title'] = title
        node += children
    except ValueError as error:
        msg = inliner.reporter.error(error, line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    return [node], []


def setup(app):
    roles.register_local_role('abbr', generic_role)
    app.add_node(abbr_node, html=(visit_abbr_node, depart_abbr_node))
