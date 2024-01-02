from django.db import models

class Contact_us(models.Model):
    name = models.CharField(max_length=255)
    mail_address = models.EmailField()
    message = models.TextField()
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
