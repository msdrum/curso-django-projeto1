from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.home),
    # O comando <int:id> indica para o Django receber apenas Ids que sejam números inteiros.
    path('recipes/<int:id>/', views.recipe),

]
