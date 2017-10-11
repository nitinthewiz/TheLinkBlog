#!/usr/bin/python

import pinboard
import datetime
from slugify import slugify
import os
from urlparse import urlparse, parse_qsl

def make_post(p):
    post_template = u"""---
title: "{}"
date: {} +0000
external-url: {}
hash: {}
year: {}
month: {}
scheme: {}
host: {}
path: {}
{}
---

{}
"""
    
    url_parts = urlparse(p.url)
    if url_parts.query:
        qsl = parse_qsl(url_parts.query)
        qstring = 'query:'
        for q in qsl:
            qstring = qstring + '\n    {}: "{}"'.format(q[0], q[1])
    else:
        qstring = ''

    return post_template.format(
        p.description.replace('"', '\\"'),
        p.time,
        p.url,
        p.hash,
        p.time.strftime('%Y'),
        p.time.strftime('%m'),
        url_parts.scheme,
        url_parts.netloc,
        url_parts.path,
        qstring,
        p.extended.replace('{', '&#123;').replace('}', '&#125;'))


def write_file(p):

    # Make directories
    dname = "_posts/{}".format(p.time.strftime('%Y/%m'))
    if not os.path.exists(dname):
        print "Creating %s directory..." % dname
        os.makedirs(dname)

    fname = "{}/{}-{}.md".format(
        dname,
        p.time.strftime('%Y-%m-%d'),
        slugify(p.description, max_length=25, word_boundary=True))

    if not os.path.isfile(fname):

        print "Writing %s..." % fname

        file = open(fname,"w") 
        file.write(make_post(p).encode('utf8'))      
        file.close() 

    else:

        print "ERROR: File %s exists! %s" % (fname, p.description)


def main():
    if 'PINBOARD_API' not in os.environ:
        print "Please set PINBOARD_API environment variable..."
        exit(1)

    pb = pinboard.Pinboard(os.environ['PINBOARD_API'])

    #pins = pb.posts.recent()['posts']
    pins = pb.posts.all()

    for p in pins:
        if p.shared and not p.toread:
            write_file(p)


main()

