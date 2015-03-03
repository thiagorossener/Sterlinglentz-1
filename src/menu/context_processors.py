from menu.models import MenuNode


def menu(request):
    try:
        global_menu = MenuNode.objects.get(slug__exact='global_menu')
    except MenuNode.DoesNotExist:
        global_menu = []
    return {
        "global_menu": global_menu.get_children()
    }
