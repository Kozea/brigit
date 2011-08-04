briGit
======

Very simple git wrapper module licensed under BSD    
Copyright (C) 2011 by Florian Mounier, Kozea


Installation
------------

Use pip :

pip install git+git://github.com/paradoxxxzero/brigit.git

And that's all.


Usage
-----

```python
from brigit import Git
new_repo = Git("~/brigit/new_repo")  # Will do a git init
git = Git("~/brigit/clone_of_brigit", "git://github.com/paradoxxxzero/brigit.git", quiet=False)  # Will do a git clone git://github.com/paradoxxxzero/brigit.git

# Then you can use all of your git command like this:
git.pull())
git.add("myNewFile")
git.commit("-a", message="Adding myNewFile")
git.push() # if you have push rights
```
