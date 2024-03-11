from django.urls import path
from .views import PrototypeList, PrototypeCreate, PrototypeDetail, PrototypeUpdate, PrototypeDelete


app_name = 'prototypes'
urlpatterns = [
    path('', PrototypeList.as_view(), name='list'),
    path('prototypes/', PrototypeCreate.as_view(), name='create'),
    path('prototypes/<int:pk>/', PrototypeDetail.as_view(), name='detail'),
    path('prototypes/<int:pk>/update', PrototypeUpdate.as_view(), name='update'),
    path('prototypes/<int:pk>/delete', PrototypeDelete.as_view(), name='delete'),
]