"""
Init api module.
"""
from .api import APP
from .routes import setup_routing


setup_routing(APP)
