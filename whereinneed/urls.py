from django.conf.urls import url
from django.contrib import admin


from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^charity/(\d+)/', views.charity_detail, name = 'charity_detail'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_request, name="logout"),
    url(r'^login/$', views.login_request, name='login'),
    url(r'^search/$', views.searchposts, name='searchposts'),
    url(r'^like/$', views.like, name='like'),
    url(r'^update_profile/(?P<username>\w+)/$', views.update_profile, name='update_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^delete/(?P<username>\w+)/$', views.delete_profile, name='delete_profile'),
    url(r'^user_profile/(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    url(r'^category/$',views.category_view,name='category'),
    url(r'^city/$',views.city_view,name="city"),
    url(r'^rating/$',views.rating_view,name="rating"),

]
