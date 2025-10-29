from django.db import models

class funtime_disco_ticket (models.Model):
    email=models.EmailField()
    ticket_details=models.TextField('This is your e-ticket for Funtime Disco. Please do not show this to any real bouncer. Enjoy!')
    