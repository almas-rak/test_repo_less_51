from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.db import cats


def view_cat_stats(request: WSGIRequest):
    attention = ''
    cat = cats[0]
    action = request.POST.get('action', 'play_cat')
    match action:
        case 'play_cat':
            cat.play_with_the_cat()
        case 'feed_cat':
            cat.feed_cat()
        case 'power_off':
            cat.put_the_cat_to_sleep()
    if 30 > cat.level_satiety > 0:
        attention = 'Кот скоро умрёт от голода'
    elif cat.level_satiety <= 0:
        cat.description = 'Кот умер от голода'
        cat.change_state('dead')
        cat.level_satiety = 0

    if cat.level_happy <= 0:
        cat.level_happy = 0
    context = {'cat_name': cat.cat_name,
               'cat_age': cat.cat_age,
               'level_happy': cat.level_happy,
               'level_satiety': cat.level_satiety,
               'description': cat.description,
               'action': action,
               'attention': attention
               }
    return render(request, 'cat_stats.html', context=context)
