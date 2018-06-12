"""Helper functions.
"""

import logging
import optparse 
import database
from sqlalchemy import pool

# Some basic configuration
LOGGING_FORMAT  = '%(levelname)s: %(asctime)-15s: %(message)s'

# Uniform interface for parsing options, with some common built-in options.
options = None
largs   = None

parser = optparse.OptionParser(add_help_option=False)
parser.add_option("--tidb-host", help="tidb hostname", default="192.168.255.141")
parser.add_option("--tidb-port", help="tidb port", type="int", default=4000)
parser.add_option("--tidb-user", help="tidb user", default="root")
parser.add_option("--tidb-pass", help="tidb pass", default="")
parser.add_option("--tidb-db", help="tidb database", default="test")
parser.add_option("-w", "--workers", help="default number of workers", type="int", default=50)
parser.add_option("-p", "--server-port", type="int", default=9000, help="server port")

parser.add_option("", "--help", action="help")

def _parse_options():
    global options
    global largs
    if not (options and largs):
        options, largs = parser.parse_args()

def get_options():
    """Return the parsed (named) options."""
    global options
    _parse_options()
    return options

def get_largs():
    """Return the parsed (free) options."""
    global largs
    _parse_options()
    return largs

# Wraps SQLAlchemy's DB Pool into our own connection pool.
db_pool = pool.manage(database)
def get_db_conn(host=None, port=None, user=None, password=None, database=None):
    """Returns a database connection from the connection pool."""
    global db_pool
    assert options

    if host is None:
        host = options.tidb_host
    if port is None:
        port = options.tidb_port
    if user is None:
        user = options.tidb_user
    if password is None:
        password = options.tidb_password
    if database is None:
        database = options.tidb_db

    return db_pool.connect(
            host='%s:%d' % (host, port), 
            user=user, password=password, database=database)

# Sets up the global logger.
logger = logging.basicConfig(level=logging.ERROR, format=LOGGING_FORMAT)
logger = logging
