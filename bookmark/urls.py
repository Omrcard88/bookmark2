from django.urls import path

from .views import *
urlpatterns = [
    #path(url패턴, 뷰, url패턴의 이름),
    # 클래스형 뷰, 함수형 뷰를 path에 사용할 때 모양이 다릅니다.
    # 함수형 뷰 : 뷰 이름만 쓴다.
    # 클래스형 뷰 : 뷰이름.as_view()
    # http://127.0.0.1:8000/bookmark/
    path('', BookmarkListView.as_view() , name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    # Primary Key
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'), 
    # int, str, slug, path, 
    # 필터 - Custom 으로 만들 수 있음
    # 자료형을 뺴주면 문자열이 기본
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name ='delete'),
]