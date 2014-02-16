# Std lib
import transaction

# 3rd Party
from pyramid.view import view_config
from pyramid.i18n import TranslationStringFactory
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from velruse import login_url

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

@view_config(route_name='profile', renderer='templates/profile.jinja2')
def profile_view(request):
    """
    Docstring goes here

    """
    user = User.by_id(request.matchdict['id_'])
    return {'User': user }

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
            user = User(name, email, password, location, field)
            DBSession.add(user)
            DBSession.flush()
            return HTTPFound(location=request.route_url('profile', 
                                                        id_=user.id_))
    # Return 
    return {'url': request.application_url + '/register',
            'came_from': came_from,
            'name': name,
            'email': email,
            'location': location,
            'field': 'FIXME: Field Goes Here!!!!!!',
            'login_url': login_url}
