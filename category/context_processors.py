#it is a function .it will take request as a argument. it will return dictionary as a context.
from .models import Category


def menu_links(request):
    links=Category.objects.all() #fetching all categories from database.links like global variable
    return dict(links=links)      # WE HAVE HAVE ADD THIS MENU_LINKS CONTEXT_PRECESSORS IN SETTING.PY TEMPLATES
