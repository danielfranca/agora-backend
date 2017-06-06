"""
Views related to account/authentication
"""
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from api.views import BaseApiView, SerializerFactory
from accounts.models import BorrowerUser


class FacebookLogin(SocialLoginView):
    """
    Class to handle Facebook authentication
    """
    adapter_class = FacebookOAuth2Adapter


class BorrowerUserApi(BaseApiView):
    """
    Handle user api
    """
    pass
