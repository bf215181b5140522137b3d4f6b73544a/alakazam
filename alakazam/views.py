from pyramid.view import view_config
from pyramid.i18n import TranslationStringFactory
from alakazam.models import DBSession, User

_ = TranslationStringFactory('Alakazam')

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    """
    Docstring goes here

    """
    session = DBSession()
    #Use session to make queries
    #session.query()
    return {'project': 'Alakazam'}

@view_config(route_name='register', renderer='templates/register.jinja2')
def register_view(request):
    """
    Docstring goes here

    """
    return {'nothing': 'Something'}

