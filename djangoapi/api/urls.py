from django.urls import path
from .views import StatusAPIView, StatusDetailAPIView
    #  StatusCreateAPIView, \
    #  StatusDeleteAPIView, StatusUpdateAPIView

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>/', StatusDetailAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()), #creation handled by StatusAPIView as createModelMixin was used for the same.
    # path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]
