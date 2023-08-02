from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save,sender=CustomUser)
def post_save_custom_user_send_welcom_mail(sender,instance,created,**kwargs):
    if created:
        subject = 'Welcome to ByChat Application'
        message = f'''Hi,{instance.username},thank you for registering in Bychat Application,
        We are offering you to share ideologies and thoghts with your friends and loved ones,
        we are offering you chat/video call facility'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject,message,email_from,recipient_list)
    