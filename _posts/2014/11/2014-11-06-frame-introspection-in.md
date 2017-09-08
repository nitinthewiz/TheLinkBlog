---
title: "Frame introspection in Pyston"
date: 2014-11-06 03:21:21 +0000
external-url: http://blog.pyston.org/2014/11/06/frame-introspection-in-pyston/
hash: c413b2628fbba2dbcd0b1b09bbeaab43
annum:
    year: 2014
    month: 11
hostname: blog.pyston.org
---

We recently landed a new feature for Pyston: frame introspection, the ability to inspect the local variables of stack frames (usually but not always the current one).  There are a couple ways to directly make use of this feature from your Python code, such as the locals() method and the f_locals attribute on frame objects.  There are also some Python features that aren’t explicitly about locals but require them to be available, such as eval() and exec statements.  Finally, frame introspection is important for the JIT to be able to introspect its own stack frames to be able to support features such as deoptimization.  (I should mention that none of these features work yet since they all depend on the base frame introspection mechanism, which only just got added.)
