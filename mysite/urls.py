"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from home import views
from order import views as orderviews
from user import views as userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('',include('home.urls')),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('search_auto/',views.search_auto,name='search_auto'),
    path('product/',include('product.urls')),
    path('order/',include('order.urls')),
    path('user/',include('order.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/',views.category_product,name='category_product'),
    path('product/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('shopcart/',orderviews.shopcart,name='shopcart'),
    path('login/',userviews.loginform,name='loginform'),
    path('logout/',userviews.logout_func,name='logout_func'),
    path('signup/',userviews.signupform,name='signupform'),
    path('user/update/',userviews.user_update,name='user_update'),
    path('user/password/',userviews.user_password,name='user_password'),
    path('user/orders/',userviews.user_orders,name='user_orders'),
    path('user/orderdetail/<int:id>/',userviews.user_orderdetail,name='user_orderdetail'),
    path('user/userorderproduct/',userviews.user_orderproduct,name='user_orderproduct'),
    path('user/user_comments/',userviews.user_comments,name='user_comments'),
    path('user/deletecomment/<int:id>/',userviews.deletecomments,name='deletecomments'),
    path('ajaxcolor/',views.ajaxcolor,name='ajaxcolor'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#          urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
