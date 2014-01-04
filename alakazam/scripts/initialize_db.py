# Std lib
import os
import sys
import transaction

# 3rd party
from pyramid.paster import get_appsettings, setup_logging

# Local
from alakazam.models import DBSession, Base, User

def usage(argv):
    """
    Docstring goes here

    """
    cmd = os.path.basename(argv[0])
    sys.exit(1)

def main(argv=sys.argv):
    """
    Docstring goes here

    """
    if len(argv) != 2:
        usage(argv)
    config = argv[1]
    setup_logging(config)
    settings = get_appsettings(config)
    if settings.get('heroku') == 'true':
        from sqlalchemy import create_engine
        engine = create_engine(os.environ['DATABASE_URL'])
    else:
        from sqlalchemy import engine_from_config
        engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    # NOTE: Used for Testing Model (Remove Me)
    #with transaction.manager:
    #    user_model = User('brendanwjw@msn.com', 'password123')
    #    DBSession.add(user_model)
