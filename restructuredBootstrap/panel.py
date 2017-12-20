#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import set_source_info, nested_parse_with_titles


class panel_node(nodes.General, nodes.Element):
    pass


class panel_footer_node(nodes.General, nodes.Element):
    pass


class panel_header_node(nodes.General, nodes.Element):
    pass


def visit_panel(self, node):
    self.body.append(self.starttag(node, 'div', CLASS=' '))


def depart_panel(self, node):
    self.body.append('</div>\n')


def visit_header(self, node):
    node['classes'] += ['panel-heading']
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'div', '', **atts))


def depart_header(self, node):
    # Keep the source clean, p tags output a new line, strip it
    if self.body[-1].endswith("\n"):
        self.body[-1] = self.body[-1].rstrip('\n')
    self.body.append('</div>\n')


def visit_footer(self, node):
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'div', **atts))


def depart_footer(self, node):
    if not self.body[-1].endswith("\n"):
        self.body[-1] += "\n"
    self.body.append('</div>\n')


class BasePanel(Directive):
    """
    A bootstrap panel
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'panel-title': directives.flag,
    }
    node_class = None

    def run(self):
        self.assert_has_content()

        panel = panel_node()
        panel.document = self.state.document
        set_source_info(self, panel)

        panel['classes'] = ['panel']
        panel['classes'].append(self.node_class)
        panel['classes'] += self.options.get('class', [])
        self.add_name(panel)

        panel_heading = None
        if self.arguments:
            heading = self.arguments[0]
            children, msg = self.state.inliner.parse(
                heading, 0, self.state_machine, self.state.parent)
            panel_heading = panel_header_node(heading)

            if 'panel-title' in self.options:
                title_p = nodes.paragraph()
                title_p += children
                title_p['classes'] += ['panel-title']
                panel_heading += title_p
            else:
                panel_heading += children

        nested_parse_with_titles(self.state, self.content, panel)

        # If we have a footer within our panel, remove it for now.
        pfooter = None
        panel_traverse = panel.traverse(panel_footer_node)
        if len(panel_traverse):
            pfooter = panel_traverse[0]
            panel.children.remove(pfooter)

        # pending elements can be a first node, we need the next index
        first_node_pending = isinstance(panel.children[0], nodes.pending)
        fn_index = 1 if first_node_pending else 0

        # If first or last node is not a table or list-group
        # wrap it in a panel-body
        table_is_first_node = isinstance(panel.children[fn_index], nodes.table)
        table_is_last_node = isinstance(panel.children[-1], nodes.table)

        list_is_first_node = isinstance(panel.children[fn_index], nodes.Sequential)
        list_is_last_node = isinstance(panel.children[-1], nodes.Sequential)

        if table_is_first_node or table_is_last_node:
            self.create_panel_body(panel, table_is_first_node,
                                   table_is_last_node)
        elif list_is_first_node or list_is_last_node:
            self.create_panel_body(panel, list_is_first_node,
                                   list_is_last_node)
        else:
            # By default contain everything inside a panel-body
            panel_body = nodes.container()
            panel_body['classes'] = ['panel-body']
            panel_body.children = panel.children
            panel.children = [panel_body]

        if panel_heading:
            panel.children.insert(0, panel_heading)

        # Add back our footer last
        if pfooter:
            panel.children.append(pfooter)

        return [panel]

    def create_panel_body(self, node, is_first_node, is_last_node):
        if len(node.children) > 1:
            # Add back pending elements to the panel
            pending = None

            # We have multiple items e.g: [table, p, p] or [p, p, table]
            # Pop the first or last item off (it's a table)
            # If we have a pending element first or before last, add it back
            table_node = None
            if is_first_node:
                if isinstance(node.children[0], nodes.pending):
                    pending = node.children.pop(0)
                table_node = node.children.pop(0)
            elif is_last_node:
                if isinstance(node.children[-2], nodes.pending):
                    pending = node.children.pop(-2)
                table_node = node.children.pop()

            # Wrap everything else in a body from the main node
            panel_body = None
            if len(node.children):
                panel_body = nodes.container()
                panel_body['classes'] = ['panel-body']
                panel_body.children = node.children
                node.children = []

            # Add it back in the correct order
            if is_first_node:
                if pending is not None:
                    node.children += [pending]
                node.children += [table_node]
                if panel_body is not None:
                    node.children += [panel_body]
            elif is_last_node:
                if panel_body is not None:
                    node.children += [panel_body]
                if pending is not None:
                    node.children += [pending]
                node.children += [table_node]
        else:
            # If it's 1 item, just add the table raw (no wrapping required)
            # We don't have to worry about .panel-body for any other items
            pass


class PanelFooter(Directive):
    """
    A bootstrap panel footer
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        node = panel_footer_node()
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] = ['panel-footer']
        node['classes'] += self.options.get('class', [])

        if self.arguments:
            text = self.arguments[0]
            node.append(nodes.paragraph(text, text))

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class PanelDefault(BasePanel):
    node_class = 'panel-default'


class PanelPrimary(BasePanel):
    node_class = 'panel-primary'


class PanelSuccess(BasePanel):
    node_class = 'panel-success'


class PanelInfo(BasePanel):
    node_class = 'panel-info'


class PanelWarning(BasePanel):
    node_class = 'panel-warning'


class PanelDanger(BasePanel):
    node_class = 'panel-danger'


def setup(app):
    app.add_directive('panel', PanelDefault)
    app.add_directive('panel-primary', PanelPrimary)
    app.add_directive('panel-success', PanelSuccess)
    app.add_directive('panel-info', PanelInfo)
    app.add_directive('panel-warning', PanelWarning)
    app.add_directive('panel-danger', PanelDanger)
    app.add_directive('panel-footer', PanelFooter)
    app.add_node(panel_node, html=(visit_panel, depart_panel))
    app.add_node(panel_header_node, html=(visit_header, depart_header))
    app.add_node(panel_footer_node, html=(visit_footer, depart_footer))
