from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from lagom.experimental.integrations.django import DjangoModel

from .dependency_config import container
from .models import Question


class SomeDep:
    message = "Hello, world. I'm an injected dependency"


@container.bind_view
def index(request, dep: SomeDep, questions: DjangoModel[Question]):
    new_question = questions.new(question_text="What's next?", pub_date=timezone.now())
    new_question.save()
    return HttpResponse(f"plain old function: {dep.message} with {questions.objects.all().count()} questions")


@container.bind_view
class CBVexample(View):
    def get(self, request, dep: SomeDep):
        return HttpResponse(f"Class based: {dep.message}")


@container.bind_view
class CBVexampleWithPathParams(View):
    def get(self, request, favourite_number, dep: SomeDep):
        return HttpResponse(f"Class based with my favourite number: {favourite_number} but also: {dep.message}")
