from django.urls import path

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'), # view에 작성한 내용 없으니까 연결할 템플릿 경로를 적어준다
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]