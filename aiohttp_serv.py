import asyncio

import aiohttp
from aiohttp import web


def fibo():
    old = 0
    n = 1
    while True:
        yield n
        old, n = n, old + n


f = fibo()


@asyncio.coroutine
def handle(request):
    key = request.match_info.get('key', "default")
    response = yield from aiohttp.request(
        'GET',
        "http://localhost:5555/count/{}".format(key)
    )
    body = yield from response.read()
    return web.Response(body=body)


@asyncio.coroutine
def fibo(request):
    b = str(next(f))
    b = bytes(b, 'utf-8')
    return web.Response(body=b)


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/fibo', fibo)
    app.router.add_route('GET', '/{key}', handle)

    srv = yield from loop.create_server(app.make_handler(),
                                        '127.0.0.1', 8001)
    print("Server started at http://127.0.0.1:8001")
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
