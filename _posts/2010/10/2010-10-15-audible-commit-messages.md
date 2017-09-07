---
title: "Audible Commit Messages with CommitBot"
date: 2010-10-15 13:14:33 +0000
external-url: http://blog.gleitzman.com/post/1216562825
hash: 21917590b8932ea8b9d24415f1dae8dd
---

I enjoy a good commit message as much as the next coder. (For the non-nerds in the audience, a commit message is a short description of the changes you made to the source code). At Hunch we found that greping through commit logs was a bit of a pain and instead wrote CommitBot, a script for audibly broadcasting commit messages. You can see it in action here:





The code is relatively straightforward. Every couple seconds, CommitBot looks for new commits, parses hash tags from the message (#female for a female voice, #novelty for weirder voices, #silent for silent commit messages, etc.), pauses whatever music is playing in the office, and announces the message.

Intrigued? I’m happy. Feel free to grab the source here (tested on OSX).

