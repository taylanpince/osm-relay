from fabric.api import *
from fabric.contrib.console import confirm


env.root_dir = "/home/taylan/sites/osm-relay"
env.project_dir = "%s/src/osm-relay" % env.root_dir
env.hosts = [
    "67.23.16.73",
]

def deploy():
    """
    Deploy the latest version
    """
    update()
    update_pip()
    restart()

def update():
    """
    Updates project source
    """
    run('cd %s; git pull' % env.project_dir)

def version():
    """
    Show last commit to repo on server
    """
    run('cd %s; git log -1' % env.project_dir)

def restart():
    """
    Restart Apache process
    """
    sudo('/etc/init.d/apache2 stop')
    sudo('/etc/init.d/apache2 start')

def update_pip():
    """
    Update pip requirements
    """
    virtualenv_run('pip install -E %s -r %s/conf/requirements.pip' % (env.root_dir, env.project_dir))

def syncdb():
    """
    Run syncdb and apply south migrations
    """
    virtualenv_run('manage.py syncdb')
    virtualenv_run('manage.py migrate')

def virtualenv_run(cmd):
    """
    Runs a command using the virtualenv environment
    """
    require('root_dir')

    return run('source %s/bin/activate; %s' % (env.root_dir, cmd))
