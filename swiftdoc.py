__author__ = 'schwa'

import os
import fnmatch
from pathlib import Path
import re
from jinja2 import Environment, FileSystemLoader
import hashlib
import click
import sys
import pkg_resources

class PathlibPath(click.Path):
    def convert(self, value, param, ctx):
        result = super(PathlibPath, self).convert(value, param, ctx)
        result = Path(result) if result else result
        return result

class Test(object):
    def __init__(self):
        self.name = None
        self.test = None
        self.result = None
        self.location = None

class SwiftDoc(object):
    def __init__(self):
        self.templates_path = Path(pkg_resources.resource_filename(__name__, "templates"))
        assert self.templates_path.exists()
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_path)),
            trim_blocks = True,
            lstrip_blocks = True,
            extensions=["jinja2.ext.with_"],
            )

    def main(self, input_dir, output_dir, imports):

        if not output_dir.exists():
            output_dir.mkdir(parents=True)

        swift_files = []
        for dir, dirs, files in os.walk(str(input_dir)):
            dir = Path(dir)
            files = [dir / name for name in files if fnmatch.fnmatch(name, "*.swift")]
            swift_files += files

        for path in swift_files:
            lines = path.open().readlines()

            name = "{}SwiftDocTests".format(path.stem)
            output_path = (output_dir / name).with_suffix(".swift")

            tests = []

            for index, line in enumerate(lines):
                match = re.match(r"\s*:test:\s*(.+)", line)
                if not match:
                    continue

                test = Test()

                test_lines = [line.strip()]
                test.test = match.groups()[0]
                line = lines[index + 1]
                test_lines.append(line.strip())

                match = re.match(r"\s*:result:\s*(.+)", line)
                if not match:
                    continue

                test.result = match.groups()[0]

                test.source = '\n\t\t'.join(test_lines)
                test.name = hashlib.sha1(test.source).hexdigest()

                tests.append(test)

            if not tests:
                continue


            template = self.env.get_template("TestFile.jinja2")

            d = dict(
                imports = imports,
                name = name,
                tests = tests,
                author = "SOMEONE", # TODO
                created = "SOMEWHEN", # TODO
                project_name = "SOMETHING",
                copyright = "SOME STUFF",
                filename = output_path.name,
                )
            s = template.render(**d)


            output_path.open("w").write(s)

            sys.stderr.write("# Wrote \"{}\"\n".format(output_path.name))

@click.command()
@click.argument("input", type=PathlibPath(exists=True, file_okay=False, dir_okay=True, readable=True), default=".", metavar="INPUT_DIR")
@click.option("--output", type=PathlibPath(file_okay=False, dir_okay=True, writable=True), default="SwiftDocTests", metavar="OUTPUT_DIR", help="Output directory for unit test files.")
@click.option("--imports", type=str, multiple=True, metavar="IMPORT", help="Imports to include in every Unit Test file.")
def cli(input, output, imports):
    """Produce unit test source files from correctly formatted Swift doc comments
    """
    # print input
    # print output
    # print imports
    tool = SwiftDoc()
    tool.main(input, output, imports)

if __name__ == '__main__':
    cli()