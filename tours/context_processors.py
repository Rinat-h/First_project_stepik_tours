from tours import data


def menu_link(request):
    dep_for_menu = {"depart": data.departures, "main_tile": data.title}
    return dep_for_menu
