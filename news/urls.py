from django.urls import path

from .views import NewListView, NewDetailView, NewCreateView, NewUpdateView, NewDeleteView


app_name = 'news'

urlpatterns = [
    path('', NewListView.as_view()),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail'),
    path('create/', NewCreateView.as_view(), name='new_create'),
    path('<int:pk>/update/', NewUpdateView.as_view(), name='new_update'),
    path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),

]
