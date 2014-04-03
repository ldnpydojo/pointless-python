import imp
import requests


def get_file(url):
    r = requests.get(url)
    _file = r.text
    return _file


def string_to_module(name, module_string):
    module = imp.new_module(name)
    exec(module_string, module.__dict__)
    return module


def load_module(url):
    module_string = get_file(url)
    module = string_to_module("test", module_string)
    return module


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/markeganfuller/test-dojo/master/test-dojo.py"
    module = load_module(url)
    module.hello()
