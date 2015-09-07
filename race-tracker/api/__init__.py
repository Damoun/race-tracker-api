"""
Init api module.
"""
from .api import APP
from .routes import setup_routing
from .models import plugin


APP.install(plugin)
setup_routing(APP)
