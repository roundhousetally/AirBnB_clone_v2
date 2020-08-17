#!/usr/bin/python3
""" this script generates a compressed archive file """
from fabric.api import *
from datetime import datetime


def do_pack():
    """ packs the webstatic """
    mktime = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    try:
        archfile = local('sudo tar -czvf versions/web_static_{}.tgz web_static'
                         .format(mktime))
        return(archfile)
    except BaseException:
        return None
