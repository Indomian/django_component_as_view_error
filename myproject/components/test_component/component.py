from django_components import component, types


@component.register("test_component")
class MagicComponent(component.Component):
    def get_context_data(self, argument):
        return {
            "argument": argument,
            "name": self.registered_name
        }

    def get(self, request):
        return self.render_to_response(
            kwargs={
                "argument": "From Get Request"
            }
        )

    template: types.django_html = """
        <div class="test-component">
        This is test component with argument: <strong>{{ argument }}</strong><br />
        and my name is <strong>{{ name }}</strong>
        </div>
    """

    css: types.css = """
        .test-component { width: 200px; background: pink; }
    """
