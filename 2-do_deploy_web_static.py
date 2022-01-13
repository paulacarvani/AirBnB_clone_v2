#!/usr/bin/python3

"""
Files deployment
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['35.237.0.179', '54.167.64.127']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy files """
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split('/')[1]
        no_ext = archive_path.split('/')[1].split('.')[0]
        final_path = "/data/web_static/releases/"

        put('{}, /tmp/'.format(archive_path))
        run('sudo mkdir -p {}{}/'.format(final_path, no_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(
            filename, final_path, no_ext))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(
            final_path, no_ext))
        run('sudo rm -rf {}{}/web_static'.format(final_path, no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(
            final_path, no_ext))
        return True
    except Exception:
        return False
