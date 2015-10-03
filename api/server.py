"""
Run the bottle HTTP server.
"""
from .api import APP


if __name__ == "__main__":
    APP.run()
