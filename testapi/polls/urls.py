from django.urls import path

from .views import PollListView, PollView, GetUserAnswersView

urlpatterns = [
    path('poll', PollListView.as_view(), name='list'),
    path('poll/<int:pk>', PollView.as_view(), name='detail'),
    path('answer/<int:pk>', GetUserAnswersView.as_view(), name='answers'),
]