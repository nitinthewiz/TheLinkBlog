#!/usr/bin/python

import pinboard
from datetime import datetime
from dateutil import tz
from slugify import slugify
import os
from urlparse import urlparse, parse_qsl

pb = pinboard.Pinboard(os.environ['PINBOARD_API'])

def make_post(p, timestamp):

    post_template = u"""---
title: "{}"
date: {}
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
        timestamp.strftime('%Y-%m-%d %H:%M:%S %z'),
        p.url,
        p.hash,
        timestamp.strftime('%Y'),
        timestamp.strftime('%m'),
        url_parts.scheme,
        url_parts.netloc,
        url_parts.path,
        qstring,
        p.extended.replace('{', '&#123;').replace('}', '&#125;'))


def write_file(p, timestamp):

    # Make directories
    dname = "_posts/{}".format(timestamp.strftime('%Y/%m'))
    if not os.path.exists(dname):
        print "Creating %s directory" % dname
        os.makedirs(dname)

    fname = "{}/{}-{}.md".format(
        dname,
        timestamp.strftime('%Y-%m-%d'),
        slugify(p.description, max_length=70, word_boundary=True))

    if not os.path.isfile(fname):

        print "Writing %s" % fname

        file = open(fname,"w") 
        file.write(make_post(p, timestamp).encode('utf8'))      
        file.close() 

    else:

        print "ERROR: %s exists!" % (fname)


def main():
    if 'PINBOARD_API' not in os.environ:
        print "Please set PINBOARD_API environment variable."
        exit(1)

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/Chicago')

    #pins = pb.posts.recent()['posts']
    pins = pb.posts.all()

    for p in pins:
        if p.shared and not p.toread:
            # Convert date from UTC to CDT
            utc = p.time.replace(tzinfo=from_zone)
            central = utc.astimezone(to_zone)

            write_file(p, central)


main()

