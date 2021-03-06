from django.contrib import admin
from .models import Event
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from accounts.models import Mailing
# Register your models her

class EventAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print('test admin')
        emails = Mailing.objects.all()
        for email in emails:
            print(obj.image.url)
            print('test admin:'+email.email)
            subject, from_email, to = 'New Event:' + obj.caption , 'sppscooters@gmail.com', email.email
            html_content = "<div style='width:100%; text-align:left'> <h2>Sparkling <span style='COLOR:pink'> Pink </span> Pandas</h2><div style='text-align:left'><h3>"+ obj.caption +"</h3><p>"+ obj.description +"</h3><h2> Date<br>"+ str(obj.date) +"</h2></div></div>"
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        super().save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)
