from pyramid.config import Configurator
from pyramid.response import Response


def index(request):
    return Response(
        'Khruang Bin - Laura Lee!\n',
        content_type='text/plain',
    )

config = Configurator()
config.add_route('laura', '/laura')
config.add_view(index, route_name='laura')
app = config.make_wsgi_app()
