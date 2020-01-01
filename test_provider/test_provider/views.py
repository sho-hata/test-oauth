from django.http import JsonResponse
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


def top_view(request):
    return HttpResponse("It works!")

class ProfileView(ProtectedResourceView):
    def get(self, request, **kwargs):
        user = request.resource_owner

        return JsonResponse({
            'user_id': user.id,
            'email': user.email,
            'date_joined': user.date_joined,
            'secret_message': 'This is a hidden message',
        })


profile_view = ProfileView.as_view()
