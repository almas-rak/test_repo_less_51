from django.urls import path

from webapp.views.base import index_view
from webapp.views.cat_stats import view_cat_stats

from webapp.db import add_cats

urlpatterns = [
    path('', index_view),
    path('add_cat', add_cats),
    path('cat_stats', view_cat_stats)
]
