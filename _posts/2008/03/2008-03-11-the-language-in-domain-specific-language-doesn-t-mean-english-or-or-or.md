---
title: "The 'Language' in Domain-Specific Language Doesn't Mean English (or French, or Japanese, or ...)"
date: 2008-03-11 08:40:00 -0500
external-url: http://pragdave.blogs.pragprog.com/pragdave/2008/03/the-language-in.html
hash: 013e5ef7a9b48c084e35d4d8156c704f
year: 2008
month: 03
scheme: http
host: pragdave.blogs.pragprog.com
path: /pragdave/2008/03/the-language-in.html

---


I'm a really big fan of Domain-Specific Languages. Andy and I plugged them back in '98 when writing The
Pragmatic Programmer. I've written my share of them over the years, and I've used even more. Which is why it is distressing to see that a whole group of developers are writing DSLs (and discussing DSLs) without seeming to get one of the fundamental principles behind good DSL design.




  Domain experts don't speak a natural language




Let's say that another way. Whenever domain experts communicate, they may seem to be speaking in English (or
French, or whatever). But they are not. They are speaking jargon, a specialized language that they've
invented as a shorthand for communicating effectively with their peers. Jargon may use English words, but these
words have been warped into having very different meanings—meanings that you only learn through experience in
the field.




Let's look at some successful domain specific languages before turning our attention on the way that some DSLs are trying just a little too hard.



Success Story 1: Dependency Management in Make


  The Make utility has been a mainstay of Unix software development for over 30 years. You can complain about
some strange syntax rules (some of which involve the invisible difference between tabs and spaces), but it would
be hard to argue that Make hasn't had a major impact in the open source world.




At its heart, Make addresses the building of systems from components in the presence of dependencies. Make lets
me express the dependencies between header files, source files, object files, libraries, and executable images.
It also lets me specify the commands to execute to resolve those dependencies when certain items are missing.
For example, I could say




my_prog.o: my_prog_.c common.h

extras.o:   extras.c common.h

my_prog:    my_prog.o extras.o
            cc -o my_prog -lc my_prog.o extras.o



  This example of the Make DSL says that my_prog.o depends on my_prog.c and
common.h, and that extras.o depends on extras.c and also depends on
common.h. The final program, my_prog, depends on the two object files. To build the
program, we have to execute the cc command on the line that follows the dependency line. No build
command is needed for the object files: in this case Make knows what to do implicitly.




People who build software from source are domain experts in the area of dependencies and build commands. They need concise ways of expressing that expertise, of saying things like "if I ask you to ensure my program is up-to-date, and the common header file has been changed, then I want you to rebuild all the dependent object files before then rebuilding the main program". Make is by no means perfect, but its longevity shows that it goes a long way as a DSL to meeting its expert's needs.



Success Story 2: Active Record Declarations


  Love it or loathe it, you have to admit that Rails has changed the game. And one reason is its extensive use of DSLs. For example, when you are writing model classes, you are claiming to be an expert on your application's domain, and in the relationships between objects in that domain. And Rails has a nifty DSL to let you express those relationships.




class Post < ActiveRecord::Base
  has_many :comments
  ...
end

class Comment < ActiveRecord::Base
  belongs_to :post
  ...
end



  The two lines containing has_many and belongs_to are part of a data modeling DSL
provided by Rails. Behind the scenes, this simple-looking code creates a whole heap of supporting
infrastructure in the application, infrastructure that allows the programmer to easily navigate and manage the
relationships between (in this case) posts and comments.




  At first blush, this might seem like an English-language DSL. But, despite appearances, has_many and belongs_to are not English phrases. They are jargon from the world of modeling. They have a specific meaning in that context, a meaning that is clear to developers using Rails (because those developers take on the role of domain modeler when they start writing the application).



Success Story 3: Groovy Builders


  The Groovy language has a wonderful way of expressing data in code. The builder concept lets you construct a set of nodes as a side effect of code execution. You can then express those nodes as (for example) XML, or JSON, or Swing user interfaces. Here's a trivial example that constructs some nodes describing a person which we can then output as XML.




  result = new StringWriter
  xml = new groovy.xml.MarkupBuilder(result)
  xml.person(category: 'employee') &#123;
    name('dave')
    likes('programming')
  &#125;
  println result



  This would generate something like




  <person category="employee">
    <name>dave</name>
    <likes>programming</likes>
  </person>



  (Jim Wierich took this idea and created the wonderful Ruby Builder library, the basis of Rails' XML-generating templates.)




Again, we have a DSL aimed squaring at someone who knows what they are doing. If you're creating XML, then you know that the elements can be nested, that they can have textual content, and that elements have optional attributes. The Builder DSL takes care of all the details for you—the angle brackets, any quoting, and so on—but you still have to know the underlying concepts. Again, the language of the DSL is the language of the domain.



Seduced by Language


  Over the years, people have looked at DSLs and wondered just how far they can be taken. Would it be possible to
create a DSL that could be used by somewhat who wasn't a domain expert? So far, the answer is “no.” The problem
is that abstractions leak—to do things in a domain, you need to know the domain. The folks who brought us
Startrek TNG pretended otherwise. Jean Luc Picard used an English language DSL to talk to his food dispenser. It
worked every time. But, in the real world, you know that the first time someone said "Earl Gray, hot" to this
magic box, they'd be surprised when a naked English peer covered in baby oil popped out. 




The reality is that languages such as English, French, and so on, are imprecise. That ambiguity makes them powerful. Because of this, whenever we try to create a DSL that looks like a natural language, we fall short. Take AppleScript as an example. On the face of it, it looks nice and expressive—we're writing something that looks very natural. Here's an example from the Apple example scripts.




  set this_file to choose file without invisibles
  try
  tell application "Image Events"
  launch
  set this_image to open this_file
  scale this_image to size 640
  save this_image with icon
  close this_image
  end tell
  on error error_message
  display dialog error_message
  end try



  Kind of makes sense, doesn't it? I thought so too. So, for years, I've been trying to get into AppleScript. I keep trying, and I keep failing. Because the language is deceptive. They try to make it English-like. But it isn't English. It's a programming language.  And it has rules and a syntax that are very unEnglish like. There's a major cognitive dissonance—I have to take ideas expressed in a natural language (the problem), then map them into an artificial language (the AppleScript programming model), but then write something that is a kind of faux natural language. (Piers Cawley calls these kinds of DSLs domain-specific pidgin, but my understanding is that pidgins are full languages, and our code hasn't got that far.)




What's the point? When you're writing logic like this, with exception handling, command sequencing, and (in more advanced examples) conditionals and loops, then what you're doing is programming. The domain is the world of code. If you're not up to programming, then you shouldn't be writing AppleScript. And if you are up to programming, then AppleScript just gets in your way.




But this isn't a discussion of AppleScript. That's just an example of the kind of trouble you get into when you forget what the domain is and try to create natural language DSLs.



Testing Times


  Here's a little code from a test written using the test/spec framework.




  specify "should be a string" do
    @result.should.be.a.kind_of String
  end
  specify "value should be 'cat'" do
    @result.should.equal "cat"
  end



  It's an elegant example of what can be done with Ruby. And, don't get me wrong. I'm not picking on Chris here. I think he's created a clever framework, and one that is likely to become quite popular.



 But let's look at it from a DSL point of view. What is the domain? I'm thinking it is the specification of
the correct behavior of programs. And who are the domain experts? That's a trickier question to answer. In an
ideal world, it would be the business users. But, the reality is that if the business users had the time,
patience, an inclination to write things at this level, they wouldn't need programmers. Don't kid
yourselves—writing these specs is programming, and the domain experts are programmers. 



  As a programmer, a couple of things leap out at me from these tests. First, there's the duplication. The
specify lines are a form of grouping, and each contains a string documenting what that group
tests. But the whole point of the DSL part of the exercise is to make that blindingly obvious anyway. Now the
BDD folks say that you write the specifications first, without any content, and then gradually add the tests in
the blocks as you add supporting application code. I'd suggest that you might want to look at ways of removing
the eventual duplication by transforming the specification into the test.




  But for me the really worrying thing is the syntax. @result.should.be.a.kind.of String. It reads like English. But it isn't. The words are separated by periods, except the last two, where we have a space. As a programmer, I know why. But as a user, I worry about it. In the first example, we write @result.should.be.a.kind_of. Why not kind.of? If I want to test that floats are roughly equal, I'd have said @result.should.be.close value. Why not close.to value? 




Trivial details, but it means that I can't just write tests using my knowledge of English—I have to look things up. ANd if I have to do that, why not just use a language/API that is closers to the domain of specifications and testing?
Chris's work is great, but it illustrates how a DSL that pretends to be English can never really get there. The domain of his language is software development--it would be perfectly OK to produce a DSL that makes sense in that domain.




RSpec is another behavior-driven testing framework. Here's part of a specification (or should it be test?).




  describe "(empty)" do

    it &#123; @stack.should be_empty &#125;

    it_should_behave_like "non-full Stack"

    it "should complain when sent #peek" do
      lambda &#123; @stack.peek &#125;.should raise_error(StackUnderflowError)
    end

    it "should complain when sent #pop" do
      lambda &#123; @stack.pop &#125;.should raise_error(StackUnderflowError)
    end

  end



  Another nice, readable piece of code, full of clever Ruby tricks. But, again, the attempt to create a natural
language feel in the DSL leads to all sorts of leaks in the abstraction. Look at the use of
should. We have should be_empty. Here, the actual assertion is (somewhat
surprisingly) "should be_". That's right—the be_ part is really part of the should, indicating that what
follows the underscore is a predicate method to be called (after adding a question mark, so we'd call
@result.empty? in this case). Then we have another way of using _should_ in the phrase
it_should_behave_like—all one word. Then there's a third way of using should when we reach should
raise_error. And, of course, all these uses of _should_ differ from the use in test/spec, even though both
strive for an English-like interface. The same kinds of dissonance occur with the use of it in the first three lines (it &#123;...&#125; vs. it_should_... vs. it "...").



It's a Domain Language


  Just to reiterate, I'm not bashing either of these testing frameworks—they are popular and I'm in favor of anything that brings folks to the practices of testing.




However, I am concerned that the popularity of these frameworks, and other similar uses of English-as-a-DSL, may lead developers astray. Martin Fowler writes about fluent interfaces. I think his work might have been misunderstood—the fluency here is programmer fluency, not English fluency. It's writing succinct, expressive code (and, in particular, using method chaining where appropriate).




  The language in a DSL should be the language of the domain, not the natural language of the developer. Resist the temptation to use cute tricks to make the DSL more like a natural, human language. By doing so you might add to its readability, but I can guarantee that you'll be taking away from its writability, and you'll be adding uncertainty and ambiguity (the strengths of natural languages). The second you find yourself writing




  def a
    self
  end


so that you can use "a" as a connector in


  
    add.a.diary.entry.for("Lunch").for(August.10.at(3.pm))



  you know you've crossed a line. This is not longer a DSL. It's broken English.


    
