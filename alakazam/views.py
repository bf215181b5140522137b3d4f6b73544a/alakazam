from pyramid.i18n import TranslationStringFactory
from alakazam.models import DBSession


_ = TranslationStringFactory('Alakazam')

def my_view(request):
    session = DBSession()
    #Use session to make queries
    #session.query()
    return {'project':'Alakazam'}
