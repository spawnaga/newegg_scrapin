#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:30:27 2021

@author: alex
"""

from lxml import html


def get_tree(html_content):
    return html.fromstring(html_content)


def get_text(tree, xpath_selector):
    elements = tree.xpath(xpath_selector)
    return list(map(lambda element: element.text_content(), elements))


def get_attributes(tree, xpath_selector, attribute):
    elements = tree.xpath(xpath_selector)
    return list(map(lambda element: element.get(attribute), elements))