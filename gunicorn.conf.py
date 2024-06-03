# gunicorn.conf

# Number of worker processes
workers = 4

# Bind address and port
bind = '0.0.0.0:9001'

# Logging
errorlog = '/var/log/gunicorn/project2_error.log'
accesslog = '/var/log/gunicorn/project2_access.log'
loglevel = 'info'

# Timeout
timeout = 60
