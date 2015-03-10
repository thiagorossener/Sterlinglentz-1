from fabric.api import *

from feral.settings.private import *

env.project_name = "feral"


def staging():
    """ Send commands to staging server. """
    env.hosts = ['feral.timmyomahony.com:30000', ]
    env.user = "admin"

    env.key_filename = [STAGING_PRIVATE_KEY, ]
    env.password = STAGING_SUDO
    env.dbname = STAGING_DB_NAME
    env.dbuser = STAGING_DB_USER
    env.dbpassword = STAGING_DB_PASSWORD

    env.virtualenv = "feral.com"
    env.branch = "develop"

    env.virtualenv_path = "/srv/feral.com/"
    env.project_path = "/srv/feral.com/src/"
    env.python_path = "/srv/feral.com/src/src/"


def production():
    """ Send commands to production server. """
    pass


def virtualenv(command):
    """ Run a command in the virtualenv. """
    run('workon %(project)s && %(command)s' % {'project': env.virtualenv, 'command': command})


def supervisor(action):
    """ Run a supervisorctl command. """
    sudo('sudo supervisorctl %(action)s' % {'action': action})


def restart_nginx():
    """ Restart the webserver. """
    sudo('sudo service nginx restart')


def restart_app():
    """ Restart the supervisor app server. """
    supervisor('reread')
    supervisor('update')
    supervisor('restart {0.project_name}'.format(env))


def pull_git():
    """ Pull the latest code from Github. """
    with cd(env.project_path):
        run('git fetch origin && git checkout {0} && git pull origin {0}'.format(env.branch))


def build_staticfiles():
    """ Build and collect static files with grunt and Django. """
    with cd(env.project_path):
        run('grunt build')
    virtualenv('django-admin collectstatic --noinput')


def migrate():
    """ Migrate the DB. """
    virtualenv('django-admin syncdb && django-admin migrate')


def deploy():
    """ Pull code, built static files, migrate DBs and restart servers. """
    pull_git()
    build_staticfiles()
    migrate()
    restart_nginx()
    restart_app()
