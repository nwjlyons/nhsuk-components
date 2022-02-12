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
        {% nhsuk:button %}
          Save and continue
        {% /nhsuk:button %}
    
        {% nhsuk:details summary="How to find your NHS number" %}
          <p>An NHS number is a 10 digit number, like 485 777 3456.</p>
          <p>You can find your NHS number by logging in to a GP online service or on any document the NHS has sent you, such as your:</p>
          <ul>
            <li>prescriptions</li>
            <li>test results</li>
            <li>hospital referral letters</li>
            <li>appointment letters</li>
          </ul>
          <p>Ask your GP surgery for help if you can't find your NHS number.</p>
        {% /nhsuk:details %}
    
        {% nhsuk:inset_text %}
          <p>You can report any suspected side effect to the <a href="https://yellowcard.mhra.gov.uk/" title="External website">UK safety scheme</a>.</p>
        {% /nhsuk:inset_text %}
    </body>
</html>
```
