#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import repackage

repackage.up()

# noinspection PyUnresolvedReferences
import click as click

author = ""
name = ""
desc = ""

v_major = "1"
v_min = "0"
v_patch = "0"


# noinspection SpellCheckingInspection
def _fversion():
    return f"{v_major}.{v_min}.{v_patch}"


@click.group(name, invoke_without_command=True, context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("-v", "--version", "v", is_flag=True)
@click.option("-n", "--name", "n", is_flag=True)
@click.option("-a", "--author", "a", is_flag=True)
@click.option("-d", "--debug", "d", is_flag=True)
@click.pass_context
def main(ctx, v, n, a, d):
    ctx.obj = {
        "d": d
    }

    if v:
        print(_fversion())

    if n:
        print(name)

    if a:
        print(author)


if __name__ == "__main__":
    main()
