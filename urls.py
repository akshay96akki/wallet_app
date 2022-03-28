from django.urls import path
from .views import Walletlist, CreateEntry, EntryUpdate, DeleteEntry, CustomLoginView, RegisterPage, balance
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('balance/', views.balance, name='check-balance'),

    path('', Walletlist.as_view(), name='walletlist'),
    path('create-entry/', CreateEntry.as_view(), name='create_entry'),
    path('edit-entry/<int:pk>/', EntryUpdate.as_view(), name='edit-entry'),
    path('delete-entry/<int:pk>/', DeleteEntry.as_view(), name='delete-entry')
]