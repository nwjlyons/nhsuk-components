from django_slots import Library, Component

register = Library()


class NHSUKComponent(Component):
    namespace = 'nhsuk'


@register.component
class Button(NHSUKComponent):
    pass


@register.block_component
class Details(NHSUKComponent):
    pass


@register.block_component
class InsetText(NHSUKComponent):
    pass
