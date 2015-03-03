from menu.models import MenuNode


def menu(request):
    try:
        global_menu = MenuNode.published.get(slug__exact='global_menu') \
            .get_children()
    except MenuNode.DoesNotExist:
        global_menu = []
    return {
        "global_menu": global_menu
    }
