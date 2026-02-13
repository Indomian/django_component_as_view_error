from typing import Dict, Any
from django_components import component, types
from django.template import Template
from django.template.loader import get_template


@component.register("test_component2")
class Magic2Component(component.Component):
    template: types.django_html = """
        <div class="test-component">
        This is test component with argument: <strong>{{ argument }}</strong><br />
        and it is with magic template <strong>{{ with_magic_template }}</strong>
        </div>
    """


    class Kwargs:
        argument: str
        with_magic_template: bool = False


    def get_template_data(self, args, kwargs: Kwargs, slots, context) -> Dict[str, Any]:
        return {
            "argument": kwargs.argument,
            "with_magic_template": kwargs.with_magic_template,
        }

    def on_render(self, context, template: Template) -> str:
        if self.request and self.request.GET.get("with_magic", None):
            # This line wouldn't work, but it is stated in the guide it should: https://django-components.github.io/django-components/0.148.0/concepts/advanced/hooks/#modifying-rendered-template
            return get_template("test_on_render_htmx/template.html").render(context)

        return Template(self.template).render(context)

    class View:
        def get(self, request):
            return Magic2Component.render_to_response(
                kwargs={
                    "argument": "From Get Request",
                    "with_magic_template": True
                },
                request=request,
                deps_strategy="fragment",
            )