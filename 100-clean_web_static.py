#!/usr/bin/python3
"""
Fabric script (based on 3-deploy_web_static.py) that deletes out-of-date archives
"""

from fabric.api import env, run, local
from datetime import datetime
from os.path import exists

env.hosts = ["34.239.255.31", "100.25.155.253"]


def do_clean(number=0):
    """
    Deletes unnecessary archives in versions and releases folders on web servers
    """
    number = int(number)
    if number < 1:
        number = 1
    try:
        local_archives = local("ls -1t versions", capture=True).split("\n")
        server_archives = run("ls -1t /data/web_static/releases").split("\n")

        for arch in local_archives[number:]:
            local("rm versions/{}".format(arch))

        for arch in server_archives[number:]:
            run("rm -rf /data/web_static/releases/{}".format(arch))

    except Exception as e:
        print(e)

