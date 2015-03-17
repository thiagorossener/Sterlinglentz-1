import multiprocessing

bind = "unix:/srv/feral.com/var/gunicorn.sock"
workers = 1
errorlog = "/srv/feral.com/logs/gunicorn.errors.log"
accesslog = "/srv/feral.com/logs/gunicorn.access.log"
timeout = 360