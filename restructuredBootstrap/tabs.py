#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.body import Container
from sphinx import addnodes
from sphinx.util.nodes import set_source_info, nested_parse_with_titles


class tab(nodes.container):
    pass


class tabs(nodes.container):
    pass


def visit_tabs(self, node):
    atts = {'CLASS': " ".join(node['classes'])}
    self.body.append(self.starttag(node, 'div', **atts))


def depart_tabs(self, node):
    self.body.append('</div>\n')


def visit_tab(self, node):
    attr = node['html_attributes'] if 'html_attributes' in node else {}
    attr['CLASS'] = " ".join(node['classes'])
    self.body.append(self.starttag(node, 'div', **attr))


def depart_tab(self, node):
    if not self.body[-1].endswith("\n"):
        self.body[-1] += "\n"
    self.body.append('</div>\n')


class Tabs(Container):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged
    }

    def run(self):
        self.assert_has_content()

        node = tabs()
        node.document = self.state.document
        set_source_info(self, node)

        try:
            if self.arguments:
                node['classes'] += directives.class_option(self.arguments[0])
        except ValueError:  # pragma: no cover
            val_error = 'Invalid class attribute value for "%s" directive: "%s".'
            raise self.error(val_error % (self.name, self.arguments[0]))

        node['classes'] += self.options.get('class', [])

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        wrapper = nodes.container()
        wrapper['classes'] += ['tab-content']
        wrapper += node.children

        nav_list = nodes.bullet_list()
        nav_list['classes'] += ['nav', 'nav-tabs']
        nav_list['html_attributes'] = {'role': 'tablist'}

        has_active_class = False

        for child_tab in wrapper.children:
            if not isinstance(child_tab, tab):
                raise self.error('.. tabs can only have .. tab children.')

            if 'active' in child_tab['classes']:
                has_active_class = True
            item = nodes.list_item()
            item['html_attributes'] = {'role': 'presentation'}

            html_attributes = {'role': 'tab', 'data-toggle': 'tab'}
            ref_opts = {
                'internal': True,
                'refid': child_tab['tab_id'],
                'html_attributes': html_attributes,
            }
            reference = nodes.reference('', '', **ref_opts)
            reference += child_tab['tab_title']
            para = addnodes.compact_paragraph('', '', reference)

            item += [para]
            nav_list += item

        if not has_active_class:
            wrapper.children[0]['classes'] += ['active']
            nav_list.children[0]['classes'] += ['active']

        node.clear()
        node.insert(0, nav_list)
        node.insert(1, wrapper)

        return [node]


class Tab(Container):
    """
    A single .. tab:: <Tab-Title> to be nested in .. tabs::

    https://getbootstrap.com/docs/3.3/javascript/#tabs
    """
    required_arguments, optional_arguments = 1, 0
    has_content = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
    }

    def run(self):
        self.assert_has_content()

        node = tab()
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] += ['tab-pane']
        node['classes'] += self.options.get('class', [])
        node['html_attributes'] = {'role': 'tabpanel'}

        try:
            if self.arguments:
                tab_title = self.arguments[0]
                children, msg = self.state.inliner.parse(
                    tab_title, 0, self.state_machine, self.state.parent)
                node['tab_title'] = children
                gen_id = 'tab-pane-'
                if 'name' not in self.options:
                    for child in node['tab_title']:
                        if isinstance(child, nodes.Text):
                            gen_id += child.strip().lower().replace(' ', '-')
                node['tab_id'] = self.options.get('name',
                                                  nodes.make_id(gen_id))
                self.options['name'] = node['tab_id']
        except ValueError:  # pragma: no cover
            err = 'Invalid argument attribute value for "%s" directive: "%s".'
            raise self.error(err % (self.name, self.arguments[0]))

        nested_parse_with_titles(self.state, self.content, node)
        self.add_name(node)

        return [node]


def setup(app):
    app.add_directive('tabs', Tabs)
    app.add_directive('tab', Tab)
    app.add_node(tabs, html=(visit_tabs, depart_tabs))
    app.add_node(tab, html=(visit_tab, depart_tab))
