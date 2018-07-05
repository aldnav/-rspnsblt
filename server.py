"""
Usage: server.py --port=<port>
"""
import asyncio
import aiohttp_cors
from aiohttp import web
from docopt import docopt


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    res = {'data': text}
    return web.json_response(res)


app = web.Application()


# app.add_routes([web.get('/', handle),
#                 web.get('/{name}', handle)])
app.router.add_route('GET', '/{name}', handle)

# Configure default CORS settings.
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})
# Configure CORS on all routes.
for route in list(app.router.routes()):
    cors.add(route)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    port = arguments.get('--port', 9000)
    web.run_app(app, port=port)
