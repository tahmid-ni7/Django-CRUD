from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('edit/<int:member_id>', views.edit, name='edit'),
    path('update/<int:member_id>', views.update, name='update'),
    path('delete/<int:member_id>', views.delete, name='delete')
]