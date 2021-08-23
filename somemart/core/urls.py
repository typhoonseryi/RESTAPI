from django.urls import path

from .views import AddShowItemsView, GetItemView

urlpatterns = [
    path('api/v1/goods/', AddShowItemsView.as_view()),
    path('api/v1/goods/<int:item_id>/', GetItemView.as_view()),
]