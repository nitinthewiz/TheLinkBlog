---
title: "Parse shell one-liners with pyparsing | nvbn blog"
date: 2017-10-22 20:49:36 -0500
external-url: https://nvbn.github.io/2016/07/05/shell-ast/
hash: a4c95366fb395473b4878065395d23b9
year: 2017
month: 10
scheme: https
host: nvbn.github.io
path: /2016/07/05/shell-ast/

---

The specific example in this blog post of using [Pyparsing](http://pyparsing.wikispaces.com) to write an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) isn't the reason I’m highlighting it. I've read about PyParsing before and even attempted to write a parser for the [Planet Kubb notation system](http://wiki.planetkubb.com/wiki/Notation). This is a library developers should know about. Too often people use regex in bad ways to solve these problems when a parser with a proper [BNF](https://en.wikipedia.org/wiki/Backus–Naur_form) is the right approach.
