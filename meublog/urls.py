from django.urls import path
from . import views

app_name = 'meublog'
urlpatterns = [
    path('', views.ListarPostView.as_view(), name='listar_posts'),
    path('<slug:slug>/', views.DetalharPostView.as_view(), name='detalhe'),
    path('sharepost/<int:pk>', views.FormContatoView.as_view(), name='share_post'),
    path('comentar/<int:pk>', views.ComentarioView.as_view(), name='comentar_post'),
    path('cadastrousuario', views.CadUsuarioView.as_view(), name='cadastrouser'),
    path('login', views.LoginUsuarioView.as_view(), name='loginuser'),
    path('logout', views.LogoutUsuarioView.as_view(), name='logoutuser'),
]
