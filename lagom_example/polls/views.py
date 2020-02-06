from django.http import HttpResponse


class SomeDep:
    message = "Hello, world. I'm an injected dependency"


def index(request, dep: SomeDep):
    return HttpResponse(dep.message)
