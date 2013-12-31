# Std lib
import os

# 3rd party
from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory

# Local
from alakazam.models import initialize_sql

def add_routes(config):
    """
    Docstring goes here

    :param config: blah blah
    :returns: blah blah
    """
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('register', '/register')

def heroku_engine(settings):
    """
    Docstring goes here

    :param settings: blah blah
    :returns: blah blah

    """
    # Connection string info will be in environment var in heroku
    return create_engine(os.environ['DATABASE_URL'])  

def main(global_config, **settings):
    """
    This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve`` or ``pserve``.

    """
    #SQLAlchemy engine config for main DB depending on environ
    if settings.get('heroku') == 'true':
        from sqlalchemy import create_engine
        db_engine = heroku_engine(settings)
    else:
        from sqlalchemy import engine_from_config
        db_engine = engine_from_config(settings, 'sqlalchemy.')
    #Binding engine to the model
    initialize_sql(db_engine)
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    #The views/routes are added here
    config.add_static_view('static', 'static')
    # Add routes
    config.include(add_routes)
    # Scans views.py for view_config[s] 
    config.scan()
    #config.add_route("my_route",'/')
    #config.add_view('alakazam.views.home_view',
    #                route_name="home", renderer="home.jinja2")
    return config.make_wsgi_app()
