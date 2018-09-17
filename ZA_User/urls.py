from django.urls import path,include
from . import views


urlpatterns = [
    path('register/',views.Register),
    path('login/', views.Login),
    path('RegHandle/',views.Register_handle),
    path('register_ajax/', views.register_ajax),
    path('login_handle/', views.Login_Handler),
    path('logout/',views.login_out),
    path('info/', views.info),
    # path('site/', views.site),
    #此处设置为首页，以前写法是'^$',新版本不再使用^、$，只需要‘’就可以
    # path('index/', include('ZA_Index.urls')),
]
