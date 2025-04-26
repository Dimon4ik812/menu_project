from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_url = request.path  # Текущий URL

    # Получаем все пункты меню за один запрос
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related("parent")

    # Построение дерева
    tree = {}
    for item in menu_items:
        item.active = False
        tree[item.id] = {"item": item, "children": []}

    root_items = []
    for item in menu_items:
        if item.parent_id is None:
            root_items.append(tree[item.id])
        else:
            tree[item.parent_id]["children"].append(tree[item.id])

    # Определяем активный пункт и его родителей
    active_item = None
    for item in menu_items:
        if item.url == current_url or (
            item.url.startswith("/") and reverse(item.url[1:]) == current_url
        ):
            active_item = item
            break

    if active_item:
        # Активируем цепочку родителей
        while active_item:
            tree[active_item.id]["item"].active = True
            active_item = active_item.parent

    # Рендеринг HTML
    def render_menu(items, level=0):
        html = "<ul>"
        for node in items:
            item = node["item"]
            classes = "active" if item.active else ""
            html += f'<li class="{classes}"><a href="{item.url}">{item.name}</a>'
            if node["children"]:
                html += render_menu(node["children"], level + 1)
            html += "</li>"
        html += "</ul>"
        return html

    return mark_safe(render_menu(root_items))
