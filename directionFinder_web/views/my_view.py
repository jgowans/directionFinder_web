from pyramid.view import view_config


@view_config(route_name='home', renderer='directionFinder_web:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'directionFinder_web'}
