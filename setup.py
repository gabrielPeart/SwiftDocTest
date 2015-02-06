from setuptools import setup

setup(
    name="SwiftDoc",
    version="0.1a1",
    py_modules=["swiftdoc"],
    install_requires=[
        "Click",
        "jinja2"
    ],
    entry_points="""
        [console_scripts]
        swiftdoc=swiftdoc:cli
    """,
)