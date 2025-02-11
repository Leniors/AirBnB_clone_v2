#!/usr/bin/python3
"""
    script that generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import local
from os.path import exists


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if exists("./versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
