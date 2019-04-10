# -*- coding: utf-8 -*-
# Copyright (C) 2011 by Florian Mounier, Kozea
# This file is part of brigit, licensed under a 3-clause BSD license.
import shutil

from brigit import Git


def test_basic():
    shutil.rmtree("/tmp/brigit_test", ignore_errors=True)
    git = Git("/tmp/brigit_test")
    with open("/tmp/brigit_test/file_1", "w") as f:
        f.write('1')
    git.add("/tmp/brigit_test/file_1")
    git.commit(message="Adding file_1")
    assert "Adding file_1" in git.log()
    assert len(list(git.pretty_log())) == 1
    with open("/tmp/brigit_test/file_2", "w") as f:
        f.write('2')
    git.add("/tmp/brigit_test/file_2")
    git.commit(message="Adding file_2")
    assert "Adding file_2" in git.log()
    assert len(list(git.pretty_log())) == 2
    git.reset("HEAD~1")
    assert len(list(git.pretty_log())) == 1
    assert "Untracked files:\n\tfile_2" in git.status()
    git.clean("-fdx")
    git.branch("newbranch")
    with open("/tmp/brigit_test/file_3", "w") as f:
        f.write('3')
    git.add("/tmp/brigit_test/file_3")
    git.commit(message="Adding file_3")
    assert "Adding file_3" in git.log()
    git.checkout("newbranch")
    git.cherryPick("master")
    shutil.rmtree("/tmp/brigit_test")
