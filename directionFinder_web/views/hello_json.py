from pyramid.view import view_config
import logging

@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    logger = logging.getLogger(__name__)
    logger.info("Got JSON from name: {n}".format(n = __name__))
    request.session['counter'] = request.session.get('counter', 0) + 1
    return {
        'a': [1,2,request.session['counter']],
        'b': ['x', 'y'],
    }
