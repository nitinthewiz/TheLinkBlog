---
title: "Clang Successfully Self-Hosts"
slug: clang-successfully-self-hosts
date: 2010-02-06 00:16:00 -0600
category: 
external-url: http://blog.llvm.org/2010/02/clang-successfully-self-hosts.html
hash: 6db784d07460c99900f63c5692232fee
year: 2010
month: 02
scheme: http
host: blog.llvm.org
path: /2010/02/clang-successfully-self-hosts.html

---

Doug Gregor of the LLVM project:



  We built all of LLVM and Clang with Clang (over 550k lines of C++
  code). The resulting binaries passed all of Clang and LLVM’s
  regression test suites, and the Clang-built Clang could then build
  all of LLVM and Clang again. The third-stage Clang was also
  fully-functional, completing the bootstrap.



Is there any other type of project that offers the same potential for recursive satisfaction as a compiler that can compile itself? It’s a singular milestone for LLVM.



 ★ 

