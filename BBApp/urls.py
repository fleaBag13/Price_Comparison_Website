from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compare', views.compare, name='compare'),
    path('feature', views.feature, name='feature'),
    path('Oneplus7', views.Oneplus7, name='Oneplus7'),
    path('Realmec35', views.Realmec35, name='Realmec35'),
    path('realmegt', views.realmegt, name='realmegt'),
    path('oneplus9rt', views.oneplus9rt, name='oneplus9rt'),
    path('oneplus8t', views.oneplus8t, name='oneplus8t'),
    path('oneplusnord', views.oneplusnord, name='oneplusnord'),
    path('pr1', views.pr1, name='pr1'),
    path('pr2', views.pr2, name='pr2'),
    path('pr3', views.pr3, name='pr3'),
    path('pr4', views.pr4, name='pr4'),
]