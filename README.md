briGit
======

Very simple git wrapper module licensed under BSD
Copyright (C) 2011 by Florian Mounier, Kozea


Installation
------------

Use pip :

    pip install git+git://github.com/Kozea/brigit.git

And that's all.


Usage
-----

```python
from brigit import Git
new_repo = Git("~/brigit/new_repo")  # Will do a git init
git = Git("~/brigit/clone_of_brigit",
    "git://github.com/Kozea/brigit.git",
     quiet=False)  # Will do a git clone git://github.com/Kozea/brigit.git

# Then you can use all of your git command like this:
git.pull()
# Touch a new file
open(os.path.expanduser("~/brigit/clone_of_brigit/myNewFile"), "a+").close()
git.add("myNewFile")
git.commit("-a", message="Adding myNewFile")
# There's also some utils command:
git.pretty_log()
git.push() # if you have push rights
```
