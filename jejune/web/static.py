from .. import app

from aiohttp.web import FileResponse


async def index_html(request):
    return FileResponse(path=app.config['paths']['static'] + '/index.html')


app.router.add_get('/', index_html)
app.router.add_static('/static', path=app.config['paths']['static'] + '/static', name='static')
