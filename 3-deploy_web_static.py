#!/usr/bin/python3
""" generates file and deploys arch to web servers """
from fabric.api import *
from os.path import exists
from datetime import datetime
env.hosts = ['52.200.125.49', '35.196.108.12']


def do_pack():
    """ packs the webstatic """
    mktime = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    fname = "versions/web_static_{}.tgz".format(mktime)
    try:
        local('sudo tar -czvf {} web_static'.format(fname))
        return(fname)
    except BaseException:
        return None


def do_deploy(archive_path):
    """ deploys web static to web servers """
    if exists(archive_path) is False:
        return False
    f = archive_path.split('/')[-1]
    n = f.split(".")[0]
    d = "/data/web_static/releases/"
    try:
        put(archive_path, "/tmp/")
        run("sudo rm -rf {}{}".format(d, n))
        run("sudo mkdir -p {}{}/".format(d, n))
        run("sudo tar -xzf /tmp/{} -C {}{}/".format(f, d, n))
        run("sudo rm /tmp/{}".format(f))
        run("sudo mv {}{}/web_static/* "
            "{}{}/".format(d, n, d, n))
        run("sudo rm -rf {}{}/web_static".format(d, n))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(d, n))
        return True
    except:
        return False


def deploy():
    """ packs and deploys """
    ret = do_pack()
    if ret is None:
        return False
    return do_deploy(ret)
