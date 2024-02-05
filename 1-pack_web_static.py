#!/usr/bin/python3
"""
Creating a tar file for my web_static folder using fabric module
"""

from fabric.api import *
from datetime import datetime
import os

def do_pack():
    """The function to pack my web_static to a tar file"""
    if not os.path.exists("./versions"):
        local("mkdir -p versions")

    # Create the archive name based on the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(now)

    # Create the archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    # Check if the archive was created successfully
    if result is not None:
        return archive_name
    else:
        return None
