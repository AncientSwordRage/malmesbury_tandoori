from django.conf.urls import patterns, include, url
from django.contrib import admin
from tandoor.views import FoodCategoryListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tandoor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/$', FoodCategoryListView.as_view()),
)