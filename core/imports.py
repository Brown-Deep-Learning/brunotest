import importlib.abc
import importlib.machinery
import importlib.util


def import_module_from_path(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def import_module_without_cache(module_name, module_path):
    importlib.invalidate_caches()
    return import_module_from_path(module_name, module_path)
