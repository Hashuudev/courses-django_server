

from django.urls import path
from app import views

urlpatterns = [
      path('',views.Home.as_view(),name=''),
      path('watch-video/<int:id>',views.WatchVideo.as_view(),name='watch-video'),
      path('playlist/<int:id>',views.PlaylistView.as_view(),name='playlist'),
      path('comment',views.Comment.as_view(),name='comment'),
      path('delete-comment/<str:id>',views.Comment.as_view(),name='delete-comment'),
      path('about',views.About.as_view(),name='about'),
]
        