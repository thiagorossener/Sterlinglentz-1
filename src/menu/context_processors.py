from menu.models import MenuNode


def menu(request):
    try:
        global_menu = MenuNode.published.get(slug__exact='global_menu') \
            .get_children()
        for node in global_menu:
            if node.url == "/":
                if request.path == "/":
                    node.active = True
            elif node.url in request.path:
                node.active = True
    except MenuNode.DoesNotExist:
        global_menu = []
    return {
        "global_menu": global_menu
    }
