from django.db import models
from datetime import datetime

class PDF(models.Model):
    pdffile = models.FileField(upload_to='PDFs/')
    created_at = models.DateTimeField(default=datetime.now, blank=True)


