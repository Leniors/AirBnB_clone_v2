#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists


env.hosts = ['34.204.61.140', '100.26.56.132']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, no_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('sudo rm /tmp/{}'.format(file_n))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('sudo rm -rf {}{}/web_static'.format(path, no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        if run('test -e /data/web_static/current').failed:
            return False
        return True
    except:
        return False
