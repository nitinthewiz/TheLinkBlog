---
title: "A Proof That P Is Not Equal To NP?"
date: 2010-08-10 02:03:20 +0000
external-url: http://rjlipton.wordpress.com/2010/08/08/a-proof-that-p-is-not-equal-to-np/
hash: bc18341399f902b2819fc49a14b0da4d
annum:
    year: 2010
    month: 08
url-parts:
    scheme: http
    host: rjlipton.wordpress.com
    path: /2010/08/08/a-proof-that-p-is-not-equal-to-np/

---

 
 A serious proof that claims to have resolved the P=NP question. 





Vinay Deolalikar is a Principal Research Scientist at HP Labs who has done important research in various areas of networks. He also has worked on complexity theory, including previous work on infinite versions of the P=NP question. He has just claimed that he has a proof that P is not equal to NP. That’s right: . No infinite version. The real deal. 


Today I will talk about his paper. So far I have only had a chance to glance at the paper; I will look at it more carefully in the future. I do not know what to think right now, but I am certainly hopeful. 



 The Paper  



Deolalikar’s draft paper is here—he was kind enough to give me the pointer to his paper. For now please understand that this is a “preliminary version.” See the discussion by Greg Baker, who first posted on his paper. 


At first glance it is a long, well written paper, by a serious researcher. He clearly knows a great deal of complexity theory and mathematics. His Ph.D. thesis at USC is titled:  


On splitting places of degree one in extensions of algebraic function fields, towers of function fields meeting asymptotic bounds, and basis constructions for algebraic-geometric codes.



My first thought is who knows—perhaps this is the solution we have all have been waiting for. If it is correct, the Clay list will drop down to five. I assume he would take the prize.


But first there is the small issue of correctness. Is his paper correct? 


I suggest you look at his paper to see his own summary of his approach, and of course the details of his proof. At the highest level he is using the characterization of polynomial time via finite model theory. His proof uses the beautiful result of Moshe Vardi (1982) and Neil Immerman (1986): 

Theorem:   On ordered structures, a relation is defined by a first order formula plus the Least Fixed Point (LFP) operator if and only if it is computable in polynomial time. 



Then, he attacks SAT directly. He creates an ordered structure that encodes SAT. He then argues if P=NP, then by the above theorem it must follow that SAT has certain structural properties. These properties have to do with the structure of random SAT. This connection between finite model theory and random SAT models seems new to me. 


The one thing that strikes me immediately is his use of finite model theory. This is one area of logic that has already led to at least one breakthrough before in complexity theory. I believe that Neil used insights from this area to discover his famous proof that  is closed under complement. It is interesting that the “final” proof does not directly use the machinery of finite model theory. Deolalikar’s connection between model theory and the structure of random SAT is interesting. I hope it works, or at least sheds new light on SAT.


An obvious worry about his proof, just from a quick look, is the issue of relativization. I believe that the LFP characterization, and similar first order arguments do relativize in general. However, it is possible that his use of concretely encoded structures prevents his entire argument from relativizing. We will need to check carefully that his proof strategy evades this limitation. I am on record as not being a fan of oracle results, so if this is the problem for his proof, I will have to re-think my position. Oh well.


Deolalikar does cite both Baker-Gill-Solovay for relativization and Razborov-Rudich for the “Natural Proofs” obstacle. His proof strategy ostensibly evades the latter because it exploits a uniform characterization of P that may not extend to give lower bounds against circuits. In fact the paper does not state a concrete time lower bound for SAT, as the proof is by contradiction. Since the gap in the contradiction is between “” and “,” it is possible that a time lower bound of “ for some ” is implied. More will have to wait until there is time to examine all the threads of this long and complex paper closely. However, the author certainly shows awareness of the relevant obstacles and command of literature supporting his arguments—this is a serious effort.



 Open Problems  



Is his paper correct? How does he avoid all the “barriers” that have been claimed to surround the P=NP question? Let’s hope it all checks out.


       

