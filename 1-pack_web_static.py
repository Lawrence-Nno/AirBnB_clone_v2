#!/usr/bin/python3
# This fabric script generates a .tgz archive of contents of my web_static folder
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    t = datetime.utcnow()
    content = "versions/web_static_{}{}{}{}{}{}.tgz".format(t.year,
                                                         t.month,
                                                         t.day,
                                                         t.hour,
                                                         t.minute,
                                                         t.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(content)).failed is True:
        return None
    return content
