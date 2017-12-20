#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import roles
import re


class tooltip_top_node(nodes.Inline, nodes.TextElement):
    position = 'top'


class tooltip_right_node(nodes.Inline, nodes.TextElement):
    position = 'right'


class tooltip_bottom_node(nodes.Inline, nodes.TextElement):
    position = 'bottom'


class tooltip_left_node(nodes.Inline, nodes.TextElement):
    position = 'left'


def visit_tag_node(self, node):
    attrs = {
        'class': 'tooltip-text',
        'data-toggle': 'tooltip',
        'title': node['title'],
        'data-placement': node.position,
    }
    self.body.append(self.starttag(node, 'span', '', **attrs))


def depart_tag_node(self, node):
    self.body.append('</span>')


node_map = {
    'tooltip-top': tooltip_top_node,
    'tooltip-right': tooltip_right_node,
    'tooltip-bottom': tooltip_bottom_node,
    'tooltip-left': tooltip_left_node,
}


def tooltip_role(name, rawtext, text, lineno, inliner):
    try:
        regex = r"([^<>]+)((?:[ \n]+|^)<(?![ \n])(([^<>]|\x00[<>])+)(?<![ \n\x00])>)"
        text_matches = re.match(regex, text)

        if text_matches is None:
            raise ValueError(
                "Invalid tooltip text. "
                "Using a role within a role? try escaping the last back tick."
            )

        word = text_matches.group(1)
        tooltip = text_matches.group(3)
        unescaped = word.replace('\x00`', '`')
        children, msgs = inliner.parse(unescaped, lineno, inliner,
                                       inliner.parent)
        for i, child in enumerate(children):
            if isinstance(child, nodes.Text):
                child = children.pop(i)
                new_child = nodes.Text(child.astext())
                children.insert(i, new_child)

        node = node_map[name]()
        node['title'] = tooltip
        node += children
    except ValueError as error:
        msg = inliner.reporter.error(error, line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    return [node], []


def setup(app):
    roles.register_local_role('tooltip-top', tooltip_role)
    app.add_node(tooltip_top_node, html=(visit_tag_node, depart_tag_node))

    roles.register_local_role('tooltip-right', tooltip_role)
    app.add_node(tooltip_right_node, html=(visit_tag_node, depart_tag_node))

    roles.register_local_role('tooltip-bottom', tooltip_role)
    app.add_node(tooltip_bottom_node, html=(visit_tag_node, depart_tag_node))

    roles.register_local_role('tooltip-left', tooltip_role)
    app.add_node(tooltip_left_node, html=(visit_tag_node, depart_tag_node))
