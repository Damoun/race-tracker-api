"""This file provide some helpers functions"""
import importlib
import inspect


def load_module_instances(module_name, package=None):
    """Return a loaded module"""
    mod = importlib.import_module(module_name, package)
    return [ext for ext in mod.__dict__.itervalues() if
            hasattr(ext, '__dict__') and not inspect.isclass(ext)]
