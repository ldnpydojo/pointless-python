#!python3
import os, sys
import importlib
import importlib.abc

class GithubLoader():
    def load_module(self, name):
        raise ImportError("I'm loading %s from github" % name)

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



import ldnpydojo