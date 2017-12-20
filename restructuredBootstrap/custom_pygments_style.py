#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal, Text


# https://github.com/jhermann/pygments-markdown-lexer/blob/master/src/pygments_markdown_lexer/__init__.py
class StackOverflowStyle(Style):  # pragma: no cover
    #: highlight background color
    background_color = "#eff0f1"
    highlight_color = 'rgba(174, 247, 174, 0.5)'
    default_style = ""

    styles = {
        # No corresponding class for the following:
        #Text: "", # class: ''
        Whitespace: "underline #F8F8F8",  # class: 'w'
        Error: "#A40000 border:#EF2929",  # class: 'err'
        Other: "#303336",  # class 'x'
        Comment: "#858C93",  # class: 'c'
        Comment.Single: "#858C93",  # class: 'c1'
        Comment.Multiline: "#858C93",  # class: 'cm'
        Comment.Preproc: "italic #AAA",  # class: 'cp'
        Keyword: "#101094",  # class: 'k'
        Keyword.Constant: "#303336",  # class: 'kc'
        Keyword.Declaration: "#101094",  # class: 'kd'
        Keyword.Namespace: "#101094",  # class: 'kn'
        Keyword.Pseudo: "#101094",  # class: 'kp'
        Keyword.Reserved: "#101094",  # class: 'kr'
        Keyword.Type: "#7D2727",  # class: 'kt'
        Operator: "#303336",  # class: 'o'
        Operator.Word: "#1010B7",  # class: 'ow' - like keywords
        Punctuation: "#3c3d3e",  # class: 'p'
        Punctuation.Indicator: "#000",  # class: 'p-Indicator'

        # because special names such as Name.Class, Name.Function, etc.
        # are not recognized as such later in the parsing, we choose them
        # to look the same as ordinary variables.
        Name: "#303336",  # class: 'n'
        Name.Attribute: "#e64320",  # class: 'na' - to be revised
        Name.Builtin: "#303336",  # class: 'nb'
        Name.Builtin.Pseudo: "#3465A4",  # class: 'bp'
        Name.Class: "#1010B7",  # class: 'nc' - to be revised
        Name.Constant: "#303336",  # class: 'no' - to be revised
        Name.Decorator: "#888",  # class: 'nd' - to be revised
        Name.Entity: "#ce5c00",  # class: 'ni'
        Name.Exception: "#cc0000",  # class: 'ne'
        Name.Function: "#008000",  # class: 'nf'
        Name.Property: "#303336",  # class: 'py'
        Name.Label: "#f57900",  # class: 'nl'
        Name.Namespace: "#303336",  # class: 'nn' - to be revised
        Name.Other: "#303336",  # class: 'nx'
        Name.Tag: "#7d2727",  # class: 'nt' - like a keyword
        Name.Variable: "#303336",  # class: 'nv' - to be revised
        Name.Variable.Class: "#303336",  # class: 'vc' - to be revised
        Name.Variable.Global: "#303336",  # class: 'vg' - to be revised
        Name.Variable.Instance: "#303336",  # class: 'vi' - to be revised
        Number: "#7D2727",  # class: 'm'
        Literal: "#303336",  # class: 'l'
        Literal.Date: "#303336",  # class: 'ld'
        Literal.Scalar.Plain: '#090977',  # class: 'l-Scalar-Plain'
        String: "#1010B7",  # class: 's'
        String.Backtick: "#008000",  # class: 'sb'
        String.Char: "#008000",  # class: 'sc'
        String.Doc: "italic #B729D9",  # class: 'sd' - like a comment
        String.Double: "#008000",  # class: 's2'
        String.Escape: "#008000",  # class: 'se'
        String.Heredoc: "#008000",  # class: 'sh'
        String.Interpol: "#008000",  # class: 'si'
        String.Other: "#008000",  # class: 'sx'
        String.Regex: "#008000",  # class: 'sr'
        String.Single: "#7D2727",  # class: 's1'
        String.Symbol: "#008000",  # class: 'ss'
        Generic: "#000",  # class: 'g'
        Generic.Deleted: "#A40000",  # class: 'gd'
        Generic.Emph: "italic #444",  # class: 'ge'
        Generic.Error: "#EF2929",  # class: 'gr'
        Generic.Heading: "#1010b7",  # class: 'gh'
        Generic.Inserted: "#00A000",  # class: 'gi'
        Generic.Output: "#888",  # class: 'go'
        Generic.Prompt: "#745334",  # class: 'gp'
        Generic.Strong: "bold #444",  # class: 'gs'
        Generic.Subheading: "#800080",  # class: 'gu'
        Generic.Traceback: "#A40000",  # class: 'gt'
    }
