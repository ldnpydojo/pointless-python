#!python3
import os, sys
import importlib
import importlib.abc

import urlloader

class GithubLoader():
    def __init__(self):
        root = "https://raw.githubusercontent.com/markeganfuller/test-dojo/master"

    def load_module(self, name):
        return urlloader.load_module(root + name.replace("_", "-") + ".py")

class GithubImporter(object):

    def find_module(self, fullname, path=None):
        if fullname:
            print(path, fullname)
            loaded_module =  GithubLoader().load_module(fullname)
            return loaded_module
        return None


sys.meta_path = [GithubImporter()]
#~ sys.path_hooks = [Import]
#~ print(sys.path_hooks)

import test_dojo
test_dojo.hello()
