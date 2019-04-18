from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url



urlpatterns=[
   url(r'^$', views.shops, name = 'shops'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^categories/', views.display_images_categories, name = 'categories'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^myProfile/(\d+)', views.myProfile, name='myProfile'),
    url(r'^new/project$', views.new_project, name='new-project'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)