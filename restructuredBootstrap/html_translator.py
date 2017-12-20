#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from sphinx.writers.html import HTMLTranslator


class BootstrapHTMLTranslator(HTMLTranslator):
    def visit_bullet_list(self, node):
        # Sphinx
        if len(node) == 1 and node[0].tagname == 'toctree':  # pragma: no cover
            raise nodes.SkipNode

        atts = {}
        if node.hasattr('html_attributes'):
            atts = node['html_attributes']

        # If this is a list inside a button group, add a .dropdown-menu class
        if 'btn-group' in node.parent['classes'] \
                or 'btn-group-vertical' in node.parent['classes']:
            if 'dropdown-menu' not in node['classes']:
                node['classes'].append('dropdown-menu')
        elif 'panel' in node.parent['classes']:
            node['classes'].append('list-group')

        atts['CLASS'] = " ".join(node['classes'])

        self.body.append(self.starttag(node, 'ul', **atts))

    def depart_bullet_list(self, node):
        self.body.append('</ul>\n')

    def visit_list_item(self, node):
        if len(node) and hasattr(node[0], 'attributes'):
            node[0]['classes'] += ['first']

        if node.parent and 'list-group' in node.parent['classes']:
            node['classes'].append('list-group-item')

        atts = {}
        if node.hasattr('html_attributes'):
            atts = node['html_attributes']

        self.body.append(self.starttag(node, 'li', '', **atts))

    def depart_list_item(self, node):
        self.body.append('</li>\n')

    def bs_visit_enumerated_list(self, node):
        # Tests dont work with rst-class.
        # Removes our arabic class from unstyled list
        if 'list-unstyled' in node['classes']:  # pragma: no cover
            node.attributes.pop('enumtype', None)

        # then, Pass to parent
        HTMLTranslator.visit_enumerated_list_original(self,
                                                      node)  # pragma: no cover

    # overwritten: remove border=1, replace docutils/table class
    def visit_table(self, node):
        # Sphinx: overwritten to add even/odd classes
        self._table_row_index = 0

        # Bootstrap table classes
        shortcut_classes = ['bordered', 'striped', 'hover', 'condensed']
        for i, cls in enumerate(node['classes']):
            if cls in shortcut_classes:
                node['classes'][i] = 'table-%s' % cls

        # Docutils
        self.context.append(self.compact_p)
        self.compact_p = True
        node.attributes['classes'].insert(0, 'table')
        classes = ' '.join([self.settings.table_style]).strip()
        self.body.append(self.starttag(node, 'table', CLASS=classes))

    def depart_table(self, node):
        self.compact_p = self.context.pop()
        self.body.append('</table>\n')

    # overwritten to add literal-block class only
    def visit_literal_block(self, node):  # pragma: no cover
        # type: (nodes.Node) -> None
        if node.rawsource != node.astext():
            # most probably a parsed-literal block -- don't highlight
            return HTMLTranslator.visit_literal_block(self, node)
        lang = self.highlightlang
        linenos = node.rawsource.count('\n') >= \
            self.highlightlinenothreshold - 1
        highlight_args = node.get('highlight_args', {})
        if 'language' in node:
            # code-block directives
            lang = node['language']
            highlight_args['force'] = True
        if 'linenos' in node:
            linenos = node['linenos']
        if lang is self.highlightlang_base:
            # only pass highlighter options for original language
            opts = self.highlightopts
        else:
            opts = {}

        highlighted = self.highlighter.highlight_block(
            node.rawsource,
            lang,
            opts=opts,
            linenos=linenos,
            location=(self.builder.current_docname, node.line),
            **highlight_args)
        node['classes'] += [('highlight-%s' % lang), 'literal-block']
        joined_clss = " ".join(node['classes'])
        starttag = self.starttag(node, 'div', suffix='', CLASS=joined_clss)
        self.body.append(starttag + highlighted + '</div>\n')
        raise nodes.SkipNode

    # This is a copy of sphinx/writers/html.py:193
    def visit_reference(self, node):
        atts = {'class': 'reference'}

        # Required for Modals - allows modals to be toggled via inline refs
        if 'refuri' in node and node['refuri'].startswith('#modal-'):
            atts['data-toggle'] = 'modal'
            atts['data-target'] = node['refuri']
            node['internal'] = True
            atts['class'] += ' ref-modal'

        # Add nofollow if uri starts with a !
        if 'refuri' in node and node['refuri'].startswith('!'):
            node['refuri'] = node['refuri'][1:]
            atts['rel'] = 'nofollow'

        # Required for Bootstrap Tabs
        if 'html_attributes' in node:
            atts.update(node['html_attributes'])

        if node.get('internal') or 'refuri' not in node:  # pragma: no cover
            atts['class'] += ' internal'
        else:
            atts['class'] += ' external'

        # Everything below is by sphinx, we don't collect coverage on it
        if 'refuri' in node:  # pragma: no cover
            atts['href'] = node['refuri'] or '#'
            if self.settings.cloak_email_addresses and \
                    atts['href'].startswith('mailto:'):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = 1
        else:  # pragma: no cover
            assert 'refid' in node, \
                'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']
        if not isinstance(node.parent, nodes.TextElement):  # pragma: no cover
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts['class'] += ' image-reference'
        if 'reftitle' in node:  # pragma: no cover
            atts['title'] = node['reftitle']
        self.body.append(self.starttag(node, 'a', '', **atts))

        if node.get('secnumber'):  # pragma: no cover
            self.body.append(('%s' + self.secnumber_suffix) %
                             '.'.join(map(str, node['secnumber'])))

    def visit_transition(self, node):
        self.body.append(self.emptytag(node, 'hr', CLASS=''))
        raise nodes.SkipNode
