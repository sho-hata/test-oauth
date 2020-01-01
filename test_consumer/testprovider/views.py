from django.conf import settings
from .provider import TestProvider
from allauth.socialaccount.providers import registry
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)
import requests


server_url_prefix = getattr(
    settings, 'TEST_PROVIDER_URL_PREFIX',
    'http://127.0.0.1:8000')


class TestOAuth2Adapter(OAuth2Adapter):
    provider_id = TestProvider.id
    access_token_url = server_url_prefix + '/oauth/token/'
    authorize_url = server_url_prefix + '/oauth/authorize/'
    profile_url = server_url_prefix + '/api/profile/'

    def complete_login(self, request, app, token, **kwargs):
        provider = registry.by_id(app.provider)
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token})

        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(
            request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(TestOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(TestOAuth2Adapter)
