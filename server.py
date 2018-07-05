"""
Usage: server.py --port=<port>
"""
from aiohttp import web
from docopt import docopt


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])


if __name__ == '__main__':
    arguments = docopt(__doc__)
    port = arguments.get('--port', 9000)
    web.run_app(app, port=port)
