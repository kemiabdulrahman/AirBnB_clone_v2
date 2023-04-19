#!/usr/bin/python3
"""
A tgz archive from the contents of the web_static to be generated

"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        File_Name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(File_Name))
        return File_Name
    except:
        return None
