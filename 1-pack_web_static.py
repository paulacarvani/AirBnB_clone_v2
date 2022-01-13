#!/usr/bin/python3
"""Module that deploys the contents of web_static to the server"""
from fabric.api import local


def do_pack():
    """Packs contents of web_static as a .tgz and returns its filepath."""
    from os import mkdir, path
    from datetime import datetime

    now = datetime.now()
    filename = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    filepath = "versions/{}".format(filename)

    try:
        mkdir('./versions')
    except FileExistsError:
        pass

    print("Packing web_static to {}".format(filepath))
    cmd = local('tar -cvzf {} web_static'.format(filepath))
    if (cmd.return_code == 0):
        filesize = path.getsize(filepath)
        print("web_static packed: {} -> {}Bytes".format(filepath, filesize))
        return filepath
    return None
