import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

meta = {}
re_meta = re.compile(r'__(\w+?)__\s*=\s*(.*)')
re_version = re.compile(r'VERSION\s*=.*?\((.*?)\)')


def strip_quotes(quoted_string):
    """Remove quote from string"""
    return quoted_string.strip("\"'")


def add_version(match):
    """return a dict from the version number"""
    return {'VERSION': match.group(1).replace(" ", "").replace(",", ".")}


def add_meta(match):
    """return a dict from the match"""
    attr_name, attr_value = match.groups()
    return {attr_name: strip_quotes(attr_value)}


patterns = {
    re_meta: add_meta,
    re_version: add_version
}


HERE = os.path.dirname(os.path.realpath(__file__))

relative_init_path = 'race_tracker_api/__init__.py'
with open(os.path.join(HERE, relative_init_path), 'r') as handle:
    for line in handle:
        for pattern, handler in patterns.items():
            m = pattern.match(line.strip())
            if m:
                meta.update(handler(m))

setup(
    name='race-tracker-api',
    version=meta['VERSION'],
    description="Backend API of the race-tracker service",
    author=meta['author'],
    author_email=meta['email'],
    url='https://github.com/race-tracker/api',
    packages=['race_tracker_api', ],
    include_package_data=True,
    install_requires=[
        'requests==2.8.1',
        'Flask==0.10.1',
        'Flask-RESTful==0.3.4',
        'Flask-RQ==0.2',
        'Flask-SQLAlchemy==2.0'
    ],
    license=meta['license'],
    zip_safe=False,
    keywords='race_tracker_api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    test_suite='tests',
    dev_require=[
        'Flask-Script==2.0.5'
    ],
)
