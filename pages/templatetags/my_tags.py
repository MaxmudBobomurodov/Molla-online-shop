from django import template

register = template.Library()


@register.simple_tag
def get_full_path(request, lang):
    path = request.path.split('/')
    path[1] = lang
    return "/".join(path)
