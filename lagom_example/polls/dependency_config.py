from lagom import Container
from lagom.experimental.integrations.django import DjangoIntegration

from .models import Question

container = Container()
deps = DjangoIntegration(container, models=[Question])

