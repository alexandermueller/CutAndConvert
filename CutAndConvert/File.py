#!/usr/bin/env python

from os import walk, path

def fetchItemsFromDir(directory, const = False):
    files   = list()
    folders = list()

    for (root, dirnames, filenames) in walk(directory):
        files   = list(filenames)
        folders = list(dirnames)
        break

    return {'files' : files, 'folders' : folders}
