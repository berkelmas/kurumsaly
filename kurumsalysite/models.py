from django.db import models

# Create your models here.
class Contact(models.Model):
    iletisim_adsoyad = models.CharField(('Gönderenin Ad-Soyadı'), max_length=100)
    iletisim_ulasim = models.CharField(('Ulaşım Bilgileri'), max_length= 100)
    iletisim_mesaj = models.TextField(('Mesaj'))
    iletisim_tarihi = models.DateTimeField(('İletişim Formu Gönderilme Tarihi'), auto_now_add=True)

    def __str__(self):
        return self.iletisim_adsoyad

    class Meta:
        verbose_name = ("İletişim Talebi")
        verbose_name_plural = ("İletişim Talepleri")
        ordering = ("-iletisim_tarihi",)

