# Std lib
import transaction

# 3rd Party
from pyramid.view import view_config
from pyramid.i18n import TranslationStringFactory

# Local
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
    referrer = request.url if \
               request.url != request.route_url('register') else '/'
    came_from = request.params.get('came_from', referrer)
    # Fields to maintain if registration problem occurs
    name = email = location = field = '' 
    if 'commit' in request.params:
        # TODO: Add actual logging here
        print 'Holy shit I got here'
        # FIXME: Reference in list
        name = request.params['name']
        email = request.params['email']
        password = request.params['password']
        location = request.params['location']
        #field = request.params['field']
        # Create the new User
        with transaction.manager:
            DBSession.add(User(name, email, password, location, field))
    # Return 
    return {'url': request.application_url + '/register',
            'came_from': came_from,
            'name': name,
            'email': email,
            'location': location,
            'field': 'FIXME: Field Goes Here!!!!!!'}

