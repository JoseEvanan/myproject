import hashlib
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

def send_confirmation(host, email_to, name, activation_key, subject='', description=''):
    """function send message
        parameters
        ----------
        host: String
            URL server
        user: Object
            Object user django
        password_user:String
            password of user
        activation_key: String
            Key Account Activation"""
    if not host or not activation_key:
        return False
    if subject == '':
        titulo = "Registro KIWILEX"
    else:
        titulo = subject
    if description == '':
        description = """Para confirmar su registro de Kiwilex """
    else:
        description = description
    text = """Bienvenido!
              Sr/a: {}  {} le solicitamos haga click en el siguiente enlace:
              http://{}/confirm/{}""".format(name,description, host, activation_key)
    html = """\
    <html>
      <head>
        
      </head>
      <body background: #D6D6D5;">
          <div style="background: #302f2f; padding: 2% 4% 2%">
              <img style="width: 170px; height: 70px " src="http://kiwilex.com/static/img/logo.png"/>
          </div>
          <div style="background: white; padding: 2% 4% 2%">
            <p style="font-family: 'ClanPro-Book','HelveticaNeue-Light','Helvetica Neue Light',Helvetica,Arial,sans-serif; color: #717172; font-size: 16px; line-height: 28px"> <span style="font-weight: 600">{}</span>, {}, por favor, haga 
            click en este 
            <a href='http://{}/confirm/{}'>ENLACE</a><br><p>
          </div>
          <div style="background: #F1F1F1; padding: 1% 4% 1%">
              
                <a style="margin-right: 1%" href="https://play.google.com/store/apps/details?id=com.iim.kiwilex"><img style="cursor: pointer; width: 5rem; height: 5rem" src="https://4.bp.blogspot.com/-RVKEQjOvyF8/WG0nsvErouI/AAAAAAAADtA/AUx5gTp7JTkJvfjucKKQdhYPUHv1hPPcgCLcB/s1600/google_play_logo.png"/></a>
                <a style="margin-left: 1%" href="https://www.facebook.com/kiwilex/"><img style="cursor: pointer; width: 5rem; height: 5rem" src="https://images.seeklogo.net/2016/09/facebook-icon-preview-1.png"/>
                <a style="margin-right: 1%" href="https://itunes.apple.com/pe/app/kiwilex/id1239610888"><img style="cursor: pointer; width: 4rem; height: 4rem; margin: 1% 0% 1% 1%;" src="https://meraki.cisco.com/blog/wp-content/uploads/2012/08/App-Store-Icon1.png"/></a>
          </div>
      </body>
    </html>
    """.format(name, description, host, activation_key)
    try:
        mensaje = MIMEMultipart('alternative')
        text_text = MIMEText(text, 'plain')
        text_html = MIMEText(html, 'html')
        mensaje.attach(text_text)
        mensaje.attach(text_html)
        mensaje['From'] = "noreply@kiwilex.biz"
        mensaje['To'] = email_to
        mensaje['Subject'] = titulo
        server_smtp = smtplib.SMTP('smtp.office365.com', 587)
        server_smtp.ehlo()
        server_smtp.starttls()
        server_smtp.ehlo()
        server_smtp.login("noreply@kiwilex.biz", "K1w1R0b0t_")# send the message
        server_smtp.sendmail("noreply@kiwilex.biz", email_to, mensaje.as_string())
        server_smtp.close()# closed the connection
        return True
    except Exception as error:
        return False





def email_report_question(host, user, email, subject='', description=''):
    if not host:
        return False
    if subject == '':
        titulo = "Registro KIWILEX"
    else:
        titulo = subject
    if description == '':
        description = """Para confirmar su registro de Kiwilex """
    else:
        description = description
    text = ""
    css_str01 = "{font-weight: 600; font-size: 1.4rem;}"
    css_str02 = "{font-weight: 600;}"
    css_str03 = "{color: #c3d100; font-weight: 600;}"
    html = """\
    <html>
      <head>
          <style rel="stylesheet" type="text/css">
              .outer_span {}
              .inner_span {}
              .footer_span {}
          </style>
        
      </head>
      <body background: #D6D6D5;">
          <div style="background: #302f2f; padding: 2% 4% 2%">
              <img style="width: 170px; height: 70px " src="http://kiwilex.com/static/img/logo.png"/>
          </div>
          <div style="background: white; padding: 2% 4% 2%">
            <p class="text_format" style='font-family: "ClanPro-Book","HelveticaNeue-Light","Helvetica Neue Light",Helvetica,Arial,sans-serif; color: #717172; font-size: 16px; line-height: 28px'>{}<p>
          </div>
          <div style="background: #F1F1F1; padding: 1% 4% 1%">
              
                <a style="margin-right: 1%" href="https://play.google.com/store/apps/details?id=com.iim.kiwilex"><img style="cursor: pointer; width: 5rem; height: 5rem" src="https://4.bp.blogspot.com/-RVKEQjOvyF8/WG0nsvErouI/AAAAAAAADtA/AUx5gTp7JTkJvfjucKKQdhYPUHv1hPPcgCLcB/s1600/google_play_logo.png"/></a>
                <a style="margin-left: 1%" href="https://www.facebook.com/kiwilex/"><img style="cursor: pointer; width: 5rem; height: 5rem" src="https://images.seeklogo.net/2016/09/facebook-icon-preview-1.png"/>
                <a style="margin-right: 1%" href="https://itunes.apple.com/pe/app/kiwilex/id1239610888"><img style="cursor: pointer; width: 4rem; height: 4rem; margin: 1% 0% 1% 1%;" src="https://meraki.cisco.com/blog/wp-content/uploads/2012/08/App-Store-Icon1.png"/></a>
          </div>
      </body>
    </html>
    """.format(css_str01, css_str02, css_str03, description)
    try:
        mensaje = MIMEMultipart('alternative')
        text_text = MIMEText(text, 'plain')
        text_html = MIMEText(html, 'html')
        mensaje.attach(text_text)
        mensaje.attach(text_html)
        mensaje['From'] = "noreply@kiwilex.biz"
        mensaje['To'] = email
        mensaje['Subject'] = titulo
        server_smtp = smtplib.SMTP('smtp.office365.com', 587)
        server_smtp.ehlo()
        server_smtp.starttls()
        server_smtp.ehlo()
        server_smtp.login("noreply@kiwilex.biz", "K1w1R0b0t_")# send the message
        server_smtp.sendmail("noreply@kiwilex.biz", email, mensaje.as_string())
        server_smtp.close()# closed the connection
        return True
    except Exception as error:
        return False
