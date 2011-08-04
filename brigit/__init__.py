#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 by Florian Mounier, Kozea
# This file is part of brigit, licensed under a 3-clause BSD license.

"""
briGit - Very simple git wrapper module

"""

import logging
from logging import getLogger
import os
from subprocess import Popen, CalledProcessError, PIPE
from brigit.log import get_default_handler


class RawGit(object):
    """Git command wrapper"""

    def __init__(self, git_path):
        """Init a Git wrapper with an instance"""
        self.path = git_path

    def __call__(self, command, *args):
        """Run a command with args as arguments."""
        full_command = ('git', command) + args
        self.logger.info("Running git %s" % ' '.join(full_command))
        process = Popen(full_command, stdout=PIPE, stderr=PIPE, cwd=self.path)
        out, err = process.communicate()
        self.logger.debug("Command stdout: %s" % out)
        if err:
            self.logger.error("Commad stderr: %s" % err)
        retcode = process.poll()
        if retcode:
            raise CalledProcessError(retcode, full_command, out)
        return out

    def __getattr__(self, name):
        """Any method not implemented will be executed as is."""
        return lambda *args: self(name, *args)


class Git(RawGit):
    """Utility class overloading most used functions"""

    def __init__(self, git_path, remote=None, quiet=False):
        """Init the repo or clone the remote if remote is not None."""
        super(Git, self).__init__(git_path)

        dirpath = os.path.dirname(self.path)
        basename = os.path.basename(self.path)
        self.logger = getLogger("brigit")
        if not quiet:
            self.logger.addHandler(get_default_handler())
            self.logger.setLevel(logging.DEBUG)

        if not os.path.exists(self.path):
            # Non existing repository
            if remote:
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)
                self.path = dirpath
                self.clone(remote, basename)
                self.path = git_path
            else:
                os.makedirs(self.path)
                self.init()
        self.remote = remote
