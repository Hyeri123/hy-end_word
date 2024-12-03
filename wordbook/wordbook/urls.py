"""
URL configuration for wordbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.http import JsonResponse
from words.views import WordListView, WordDetailView, RandomWordView
from django.views.generic import TemplateView
# 기본 경로에 메시지 반환
def root_view(request):
    return JsonResponse({"message": "Welcome to the WordBook API! Visit /api/words/ for API endpoints."})

urlpatterns = [
    path('', root_view, name='root'),  # 기본 경로 처리
    path('api/words/', WordListView.as_view(), name='word_list'),
    path('api/words/<int:word_id>/', WordDetailView.as_view(), name='word_detail'),
    path('api/words/random/', RandomWordView.as_view(), name='random_words'),
    path('api/', root_view, name='api_root'),  # API 루트 경로
    
    # React 빌드 파일 제공
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html"), name='react_app'),
]