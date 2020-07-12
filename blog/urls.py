from django.urls import path,include
import blog.views

urlpatterns = [
    path('<int:blog_id>',blog.views.detail,name="detail"),
    path('new',blog.views.new,name="new"),
    path('edit/<int:blog_id>',blog.views.edit,name="edit"),
    path('delete/<int:blog_id>',blog.views.delete,name="delete"),
    path('comment_new/<int:blog_id>',blog.views.comment_new,name="comment_new"),
] 
