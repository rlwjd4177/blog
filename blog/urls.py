from django.urls import path,include
import blog.views

urlpatterns = [
    path('<int:blog_id>',blog.views.detail,name="detail"),
    path('new',blog.views.new,name="new"),
    path('edit/<int:blog_id>',blog.views.edit,name="edit"),
    path('update/<int:blog_id>',blog.views.update,name="update"),
    path('delete/<int:blog_id>',blog.views.delete,name="delete"),
] 
