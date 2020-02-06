from django.http import HttpResponse
from django.views import View


class SomeDep:
    message = "Hello, world. I'm an injected dependency"


def index(request, dep: SomeDep):
    return HttpResponse(f"plain old function: {dep.message}")


class CBVexample(View):
    def get(self, request, dep: SomeDep):
        return HttpResponse(f"Class based: {dep.message}")


class CBVexampleWithPathParams(View):
    def get(self, request, favourite_number, dep: SomeDep):
        return HttpResponse(f"Class based with my favourite number: {favourite_number} but also: {dep.message}")
