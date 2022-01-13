#!/usr/bin/python3
"""Module that deploys the contents of web_static to the server"""
from fabric.api import local, hosts, put, run, env

env.hosts = ['35.237.0.179', '54.167.64.127']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    from os import path

    if not path.exists(archive_path):
        return False

    filename = archive_path.split('/')[1]
    dest_path = "/data/web_static/releases/{}/".format(filename.split('.')[0])

    try:
        print("Executing task 'do_deploy'")
        put(archive_path, "/tmp/")
        run('mkdir -p {}'.format(dest_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, dest_path))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(dest_path, dest_path))
        run('rm -rf {}web_static'.format(dest_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
