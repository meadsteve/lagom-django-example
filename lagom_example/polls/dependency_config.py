

from lagom.experimental.integrations.django import DjangoContainer

from .models import Question

container = DjangoContainer(models=[Question])
