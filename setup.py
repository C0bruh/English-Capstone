from setuptools import setup

APP=['test.py']
OPTIONS = {}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)