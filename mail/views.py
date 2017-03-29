from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import generic
from .utils	import send_confirmation
# Create your views here.
class ResetPassAjax(generic.View):
    """ Reset the forgotten password of the user and send it to his email """
    def get(self, request):
        """ Get function for the view """
        #http://localhost:8000/reset_pass/?HTTP_HOST=104.236.215.145&email_to=jose.evanan@gmail.com&activation_key=123&name=Jose Evanan
        host = request.GET['HTTP_HOST']
        email_to = request.GET['email_to']
        activation_key = request.GET['activation_key']
        name = request.GET['name']
        subject = "Restablecer contraseña Kiwilex"
        description = "¡Gracias por formar parte de nuestra comunidad!<br>Para restablecer su contraseña"
        
        is_send = send_confirmation(host, email_to, name, activation_key,
                                    subject, description)

        return JsonResponse({'status': is_send})