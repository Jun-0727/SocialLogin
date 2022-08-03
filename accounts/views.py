from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import requests
# CLIENT_ID: REST_API KEY, REDIRECT_URI: CALLBACK_URI
from my_setting import CLIENT_ID, REDIRECT_URI

class KakaoSignInView(View):
    def get(self, request):
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
        
        return redirect(
            f'{kakao_auth_api}&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
        )


class KakaoSignInCallBackView(View):
    def get(self, request):
        # --- 인가코드 받아오기 --- #
        code = request.GET.get('code')

        # --- 토큰 받아오기 --- #
        token_request = requests.post(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&code={code}"
        )
        token_json = token_request.json()
        access_token = token_json.get("access_token")

        # --- 사용자 정보 받아오기 --- #
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}
        )
        profile_json = profile_request.json()

        return JsonResponse({"token" : token_json})
        # return JsonResponse({"profile" : profile_json})