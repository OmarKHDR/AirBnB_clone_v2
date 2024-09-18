#!/usr/bin/python3
"""A module here to do stuff"""
from fabric.api import run, put, local
from fabric.api import env
from datetime import datetime
import os

env.hosts = ['34.224.3.252', '100.25.129.71']

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

def do_deploy(archive_path):
    """Just be moduled for me"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, f'/tmp/{file_n}')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
    """Easy function"""
    myPath = do_pack()
    if myPath is None:
        return False
    return do_deploy(myPath)
