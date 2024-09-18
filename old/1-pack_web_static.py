#!/usr/bin/python3
"""A module here to do stuff"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as Anything:
        return None
