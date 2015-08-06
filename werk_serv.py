from werkzeug.wrappers import Request, Response


def fibo():
    old = 0
    n = 1
    while True:
        yield n
        old, n = n, old + n


f = fibo()


@Request.application
def application(request):
    return Response(str(next(f)))