from django.urls import path
from . import views
urlpatterns = [
    path('',views.blogListingView,name='blogs'),
    path('<int:id>',views.blogView,name='blog'),
    path('like',views.blogLike,name='blog_like'),
    path('comment',views.blogComment,name='comment'),
    path('reply',views.blogCommentReply,name='reply'),
    #path('addBlog',views.addBlogView,name='addevent')
]