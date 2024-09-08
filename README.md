# Django Components As View Component Register Issue Test

This is a test application to reproduce problem with the `django_components` as_view
feature when using `ComponentDependencyMiddleware` and setting
`RENDER_DEPENDENCIES` set to True.

## Usage

1. Create venv `python3.12 -m venv venv`
2. Start venv: `source venv/bin/activate`
3. Start django: `cd myproject`
4. `python manage.py runserver`
5. Go to 'localhost:8000' and you will see rendering of component located
   `myproject/components/test_component`
6. If you click link "Click to see error" you will see exception that component named "MagicComponent" is not found

## Expected behaviour

Rendering of component as view should persist name under which component was registered. Right now it
is not persisted and name of the class is used.
