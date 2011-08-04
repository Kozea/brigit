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
from datetime import datetime


class NullHandler(logging.Handler):
    def emit(self, record):
        """Do nothing"""


class RawGit(object):
    """Git command wrapper"""

    def __init__(self, git_path, encoding="utf-8"):
        """Init a Git wrapper with an instance"""
        self.path = git_path
        self.encoding = encoding

    def __call__(self, command, *args, **kwargs):
        """Run a command with args as arguments."""
        full_command = (('git', command) +
                        args +
                        tuple((u"--%s=%s" % (key, value)
                               if len(key) > 1
                               else u"-%s %s" % (
                                   key, value))
                              for key, value in kwargs.items()))
        self.logger.info(u"Running %s" % u' '.join(full_command))
        process = Popen(full_command, stdout=PIPE, stderr=PIPE, cwd=self.path)
        out, err = process.communicate()
        out = out.decode(self.encoding)
        err = err.decode(self.encoding)
        self.logger.debug("Command stdout: %s" % out)
        retcode = process.poll()
        if retcode:
            if err:
                self.logger.error("Command stderr: %s" % err)
            raise CalledProcessError(retcode, full_command, out)
        return out

    def __getattr__(self, name):
        """Any method not implemented will be executed as is."""
        return lambda *args, **kwargs: self(name, *args, **kwargs)


class Git(RawGit):
    """Utility class overloading most used functions"""

    def __init__(self, git_path, remote=None, quiet=True):
        """Init the repo or clone the remote if remote is not None."""
        if "~" in git_path:
            git_path = os.path.expanduser(git_path)

        super(Git, self).__init__(git_path)

        dirpath = os.path.dirname(self.path)
        basename = os.path.basename(self.path)
        self.logger = getLogger("brigit")
        if not quiet:
            self.logger.addHandler(get_default_handler())
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.addHandler(NullHandler())

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

    def pretty_log(self, *args, **kwargs):
        """Return the log as a list of dict"""
        kwargs["pretty"] = "format:%H;;%an;;%ae;;%at;;%s"
        for line in self.log(*args, **kwargs).split("\n"):
            fields = line.split(";;")
            yield {
                'hash': fields[0],
                'author': {
                    'name': fields[1],
                    'email': fields[2]},
                'datetime': datetime.fromtimestamp(float(fields[3])),
                'message': fields[4]
            }
