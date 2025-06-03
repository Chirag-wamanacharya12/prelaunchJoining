from django.db import models

class PreRegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15, unique=True)
    
    # Auto-managed fields
    timestamp = models.DateTimeField(auto_now_add=True)
    eligibility = models.CharField(max_length=10)    # If the email/phone is verified

    def __str__(self):
        return f"{self.name} ({self.email})"
