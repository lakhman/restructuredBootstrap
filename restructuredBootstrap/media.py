#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import set_source_info


class media(nodes.General, nodes.Element):
    pass


def visit_generic_media(self, node):
    tag = 'div'
    if isinstance(node.parent, nodes.bullet_list):
        tag = 'li'
    self.body.append(self.starttag(node, tag, CLASS=" ".join(node['classes'])))


def depart_generic_media(self, node):
    tag = 'div'

    if isinstance(node.parent, nodes.bullet_list):
        tag = 'li'

    if not self.body[-1].endswith("\n"):
        self.body[-1] += "\n"

    self.body.append('</%s>\n' % tag)


class Media(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()

        node = media()
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] = ['media']
        node['classes'] += self.options.get('class', [])

        if self.arguments:
            node['classes'] += directives.class_option(self.arguments[0])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        if isinstance(node.children[0], media) and \
                'media-right' in node.children[0]['classes']:
            # Move media-right to after media-body
            node.children.append(node.children.pop(0))

        return [node]


class MediaList(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()

        node = nodes.bullet_list()
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] = ['media-list']
        node['classes'] += self.options.get('class', [])

        if self.arguments:
            node['classes'] += directives.class_option(self.arguments[0])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class MediaLeftRight(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()

        node = media()
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] = [self.name]
        node['classes'] += self.options.get('class', [])

        try:
            if self.arguments:
                node['classes'] += directives.class_option(self.arguments[0])
        except ValueError:
            err = 'Invalid class attribute value for "%s" directive: "%s".'
            raise self.error(err % (self.name, self.arguments[0]))

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        # Add media-object class to child images
        if isinstance(node.children[0], nodes.reference):
            child_is_image = isinstance(node.children[0].children[0],
                                        nodes.image)
            if len(node.children[0].children) and child_is_image:
                node.children[0].children[0]['classes'] += ['media-object']
        elif isinstance(node.children[0], nodes.image):
            node.children[0]['classes'] += ['media-object']

        return [node]


class MediaBody(Directive):
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'heading-target': directives.uri,
        'page-header': directives.flag,
    }

    def run(self):
        self.assert_has_content()

        node = media()
        node.document = self.state.document
        set_source_info(self, node)

        node['classes'] = [self.name]
        node['classes'] += self.options.get('class', [])

        if self.arguments:
            p = nodes.paragraph()
            if 'heading-target' in self.options:
                uri = self.options['heading-target']
                ref_options = {
                    'internal': False,
                    'refuri': uri,
                    'classes': ['h4', 'media-heading']
                }
                heading = nodes.reference(self.arguments[0], self.arguments[0],
                                          **ref_options)
                p.append(heading)
            else:
                heading = self.arguments[0]
                children, msg = self.state.inliner.parse(
                    heading, 0, self.state_machine, self.state.parent)
                p = nodes.paragraph()
                p['classes'] += ['h4', 'media-heading']
                p += children

            if 'page-header' in self.options:
                page_header = nodes.container()
                page_header['classes'] += ['page-header']
                page_header += p
                node.insert(0, page_header)
            else:
                node.insert(0, p)

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def setup(app):
    app.add_node(media, html=(visit_generic_media, depart_generic_media))

    app.add_directive('media', Media)
    app.add_directive('media-list', MediaList)
    app.add_directive('media-left', MediaLeftRight)
    app.add_directive('media-right', MediaLeftRight)
    app.add_directive('media-body', MediaBody)
