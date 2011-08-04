#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 by Florian Mounier, Kozea
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with brigit.  If not, see <http://www.gnu.org/licenses/>.

"""
briGit - Very simple git wrapper module

"""

import os
from subprocess import check_output


class Git(object):
    """Git command wrapper"""
    def __init__(self, git_path, remote=None):
        """Init the repo or clone the remote if remote is not None."""
        self.path = git_path
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.remote = remote

    def __call__(self, command, *args):
        """Run a command with args as arguments."""
        return check_output(("git", command) + args,
                         cwd=self.path)

    def __getattr__(self, name):
        """Any method not implemented will be executed as is."""
        return lambda *args: self(name, *args)
