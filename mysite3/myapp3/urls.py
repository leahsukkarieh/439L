from django.urls import path
from . import views

urlpatterns = [
	path('', views.contact_list, name='contact_list'),
	path('create-contact/', views.create_contact, name='create_contact'),
	path('edit-contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
	path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),	
]