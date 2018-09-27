import importlib
import inspect
import pkgutil
from mdr.messages import BaseResponse

__path__ = pkgutil.extend_path(__path__, __name__)
__imported_classes__ = []
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__ + '.'):
    m = importlib.import_module(modname)
    [__imported_classes__.append(m.__dict__[k]) for k in m.__dict__.keys() if not k.startswith('__') and inspect.isclass(m.__dict__[k]) and issubclass(m.__dict__[k], BaseResponse)]
