from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import time

@shared_task
def send_otp_email(email, code):
    print("Sending...")
    send_mail(
        "Добро Пожаловать",
        f"вот ваш коТ: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    print("Done")
    return "OK"

@shared_task
def send_daily_report():
    print("Собираем данные...")
    time.sleep(10)
    print("Успешно")
    return "Ok"
