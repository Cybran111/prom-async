import asyncio
from collections import defaultdict
from aiohttp import web

counts = defaultdict(lambda: 0)

@asyncio.coroutine
def handle(request):
    asyncio.sleep(0.5)
    key = request.match_info.get('key', "default")
    counts[key] += 1
    return web.Response(body=str(counts[key]).encode())


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/count/{key}', handle)

    srv = yield from loop.create_server(app.make_handler(),
                                        '127.0.0.1', 8000)
    print("Server started at http://127.0.0.1:8000")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
