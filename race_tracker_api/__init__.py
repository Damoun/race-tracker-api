"""
This module provide the API of the race-tracker project
"""
from __future__ import absolute_import
from collections import namedtuple


VersionInfo = namedtuple('version_info', ('major', 'minor', 'patch'))

VERSION = VersionInfo(0, 0, 0)

__title__ = 'race-tracker-api'
__version__ = '{0.major}.{0.minor}.{0.patch}'.format(VERSION)
__author__ = 'Damien Plenard'
__email__ = 'damien@plenard.me'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Damien Plenard'
