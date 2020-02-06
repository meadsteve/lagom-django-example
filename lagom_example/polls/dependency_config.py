import types

from django.views import View
from lagom import Container


class DjangoContainer(Container):

    def view(self, view):
        if isinstance(view, types.FunctionType):
            # Plain old function can be bound to the container
            return self.partial(view)
        if issubclass(view, View):
            # For django class based view each method needs to be bound
            # to the container
            self._bind_view_methods_to_container(view)
            return view.as_view()
        raise SyntaxError(f"Container doesn't know how to handle type {type(view)}")

    def _bind_view_methods_to_container(self, view):
        for method in View.http_method_names:
            if hasattr(view, method):
                setattr(view, method, self.partial(getattr(view, method)))


container = DjangoContainer()
