#!/usr/bin/env python

from core import ROOT_PATH, Chimas

import core

Chimas = core.Chimas

from werkzeug.wsgi import DispatcherMiddleware

import os,sys

import click

@click.group()
def chimascli():
    pass

@chimascli.command()
@click.argument('directory')
def init(directory):

    if os.path.exists(directory):
        print("The name '{}' exists. Please choose a non-existent directory.".format(directory))
        return 1

    print("Creating directory {}".format(directory))
    os.makedirs(directory) # FIXME: insert modes

@chimascli.command()
@click.argument('directory')
def start(directory='.'):

    if os.path.exists(directory):
        print("The name '{}' exists. Please choose a non-existent directory.".format(directory))
        return 1

    print("Creating directory {}".format(directory))
    os.makedirs(directory) # FIXME: insert modes

@chimascli.command()
#@click.argument('directory')
def debug():
    print("__file__: " + __file__)
    print("sys.path: " + ", ".join(sys.path))
    print("sys.path[0]: " + sys.path[0])
    print("ROOT_PATH: " + ROOT_PATH)

def run_chimas():
    from werkzeug.serving import run_simple

    print("__file__: " + __file__)

    print("sys.path: " + ", ".join(sys.path))
    print("sys.path[0]: " + sys.path[0])
    print("ROOT_PATH: " + ROOT_PATH)

    #if os.path(ROOT_PATH)
    app1 = Chimas(instance='bbs1')
    app2 = Chimas(instance='bbs2')

    #app.run()
    bbs_dispatcher =\
        DispatcherMiddleware(
            None,
            {
                '/um' : app1,
                '/two' : app2
            })

    run_simple('127.0.0.1', 41345, bbs_dispatcher)


# run by script
if __name__ == "__main__":
    run_chimas()
