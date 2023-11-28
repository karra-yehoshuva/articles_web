from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.article_list,name="articlelist"),
    path('<id>/<slug>',views.Artical_Detail,name='Artical_detail'),
    path('article_create',views.article_create,name = 'article_create'),
    path('loginform',views.UserLoginView,name='loginform'),
    path('logout',views.logoutview,name='logout'),
    path('registerview',views.UserRegisterview,name='registerview'),
    path('like_article',views.Likes_View,name='like_article'),
    path('article_edit/<id>',views.ArticleEditForm,name='article_edit')
]