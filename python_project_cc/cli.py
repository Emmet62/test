# -*- coding: utf-8 -*-

"""Console script for python_project_cc."""

import click


@click.command()
def main(args=None):
    """Console script for python_project_cc."""
    click.echo("Replace this message by putting your code into "
               "python_project_cc.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
