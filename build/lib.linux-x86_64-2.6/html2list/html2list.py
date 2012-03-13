#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: html2list
   :platform: Unix, Windows
   :synopsis: The html2list implementation.

.. moduleauthor:: Ali Anari <ali@alianari.com>

"""


import poplib, email, re, html5lib
from html5lib import treebuilders, treewalkers, serializer, sanitizer
from lxml import etree


P = {'C':"""</?\w+((\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>?""",'E':['',' ','=','"','>'],'S':['=2C','=3B',',',';','|'],'R':['&lt;[^<>]+&gt;','<meta [^<>]+>','<style>[^<>]+</style>']}


def html2list(payload):

    """This function reads a block of HTML and returns a cleaned list.
    :param payload: The HTML string to read.
    :type payload: str
    :returns: list -- The parsed output as a list of strings.
    """

    cleaned_output = []
    p = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder('lxml'),tokenizer=sanitizer.HTMLSanitizer)
    s = serializer.htmlserializer.HTMLSerializer(strip_whitespace=True,omit_optional_tags=True)
    r = treewalkers.getTreeWalker('lxml')(p.parse(payload))
    for item in r.tree.elementtree.getiterator():
        if item.getparent() is not None:
            if (item.getparent().tag.split('}')[-1] == 'html'):
                item.text = ''
        else: item.text = ''
        for k in item.attrib:
            del item.attrib[k]
        if type(item.text) is str:
            for c in P['R']:
                item.text = re.sub(c,'',item.text)
    for tag in s.serialize(r):
        if not re.match("""(?:<|&lt;)/?\w+((\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?(?:>|&gt;)?""",tag):
            tag = tag.encode('ascii', 'ignore')
            split_tag = map(lambda x: x.strip(), re.split('[|,;]|(?:=2C|=3B)',tag.replace('&amp;','&')))
            for t in split_tag:
                for e in P['E']:
                    if t == e:
                        split_tag.remove(t)
            if split_tag:
                cleaned_output += split_tag
    return cleaned_output
