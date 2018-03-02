from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import generic
from .utils import send_confirmation, email_report_question

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
        description = "¡Gracis por formar parte de nuestra comunidad!<br>Para restablecer su contraseña"
        
        is_send = send_confirmation(host, email_to, name, activation_key,
                                    subject, description)
#	file = open('text.txt', 'w')
#	file.write(host)
#	file.close()
        return JsonResponse({'status': is_send})


class SendEmail(generic.View):
    """ Send email to user """

    def get(self, request):
        """ GET Method """
        host = request.GET['HTTP_HOST']
        email = request.GET['email']
        user = request.GET['user']
        exam = request.GET['exam']
        comentary = request.GET['comentary']
        num_question = request.GET['numQuestion']
        chosen_options = request.GET['chosenOptions'].split(',')
        str_chosen_options = ""
        subject = "PREGUNTA RECTIFICADA"
        if len(chosen_options) == 1:
            str_chosen_options = "- " + chosen_options[0] + "<br>"
            if comentary == "":
                description = "<span style='font-weight: 600; font-size: 1.4rem'>" + exam.upper() + "</span><br><span style='font-weight: 600'>PREGUNTA N° " + num_question + "</span><br><br>ERROR ENCONTRADO:<br>" + str_chosen_options + "<br><br>" + user.upper() + ", ¡GRACIAS POR REPORTAR ESTA PREGUNTA!<br>Se ha solucionado el inconveniente que tuviste. Con tu ayuda seguiremos creciendo.<br><br><hr><span style='color: #c3d100; font-weight: 600'>TEAM KIWILEX</span>"
            else:
                description = "<span style='font-weight: 600; font-size: 1.4rem'>" + exam.upper() + "</span><br><span style='font-weight: 600'>PREGUNTA N° " + num_question + "</span><br><br>ERROR ENCONTRADO:<br>" + str_chosen_options + "<br>TU COMENTARIO:<br>" + comentary + "<br><br>" + user.upper() + ", ¡GRACIAS POR REPORTAR ESTA PREGUNTA!<br>Se ha solucionado el inconveniente que tuviste. Con tu ayuda seguiremos creciendo.<br><br><hr><span style='color: #c3d100; font-weight: 600'>TEAM KIWILEX</span>"
        else:
            for option in chosen_options:
                str_chosen_options += "- " + option + "<br>"
            if comentary == "":
                description = "<span style='font-weight: 600; font-size: 1.4rem'>" + exam.upper() + "</span><br><span style='font-weight: 600'>PREGUNTA N° " + num_question + "</span><br><br>ERRORES ENCONTRADOS:<br>" + str_chosen_options + "<br><br>" + user.upper() + ", ¡GRACIAS POR REPORTAR ESTA PREGUNTA!<br>Se ha solucionado el inconveniente que tuviste. Con tu ayuda seguiremos creciendo.<br><br><hr><span style='color: #c3d100; font-weight: 600'>TEAM KIWILEX</span>"
            else:
                description = "<span style='font-weight: 600; font-size: 1.4rem'>" + exam.upper() + "</span><br><span style='font-weight: 600'>PREGUNTA N° " + num_question + "</span><br><br>ERRORES ENCONTRADOS:<br>" + str_chosen_options + "<br>TU COMENTARIO:<br>" + comentary + "<br><br>"  + user.upper() + ", ¡GRACIAS POR REPORTAR ESTA PREGUNTA!<br>Se ha solucionado el inconveniente que tuviste. Con tu ayuda seguiremos creciendo.<br><br><hr><span style='color: #c3d100; font-weight: 600'>TEAM KIWILEX</span>"
        is_send = email_report_question(host, email,  subject, description)
        return JsonResponse({'status': is_send})


class SendNewEmail(generic.View):
    """ Send any type of email to user """

    def get(self, request):
        """ GET Method """
        host = request.GET['HTTP_HOST']
        #user = request.GET['user']
        email = request.GET['email']
        subject = request.GET['subject']
        description = request.GET['description']
        is_send = email_report_question(host, email, subject, description)
        return JsonResponse({'status': is_send})

