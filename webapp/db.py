from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.cat import Cat

cats = []


def add_cats(request: WSGIRequest):
    cat = Cat(request.POST.get('cat_name'), age=1, level_happy=10, level_satiety=40, state_name='not_sleep')
    cats.clear()
    cats.append(cat)
    cat_stats = {
        'cat_name': cat.cat_name,
        'cat_age': cat.cat_age,
        'level_happy': cat.level_happy,
        'level_satiety': cat.level_satiety}
    return render(request, 'cat_stats.html', context=cat_stats)
