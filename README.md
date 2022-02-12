# NHS UK Component Library

Proof of concept built using https://pypi.org/project/django-slots/

## Install

```shell
poetry add git+https://github.com/nwjlyons/nhsuk_components.git
```

```python
INSTALLED_APPS = [
    # ...
    
    'nhsuk_components',
]
```

```html+django
{% load static %}
{% load nhsuk_components %}

<html>
    <head>
        <link rel="stylesheet" href="{% static 'nhsuk_components/css/nhsuk.css' %}">
    </head>
    <body>
        {% nhsuk:button/ value="Save" %}
    </body>
</html>
```
