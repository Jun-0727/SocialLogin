from django.urls import path
from . import views

urlpatterns = [
    path('kakao/login/', views.KakaoSignInView.as_view(), name='kakao_login'),
    path('kakao/callback/', views.KakaoSignInCallBackView.as_view(), name='kakao_callback'),
]
