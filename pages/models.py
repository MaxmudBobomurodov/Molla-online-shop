from django.db import models
from django.utils.translation import gettext_lazy as _




class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ContactModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone_number = models.CharField(
        max_length=13, null=True, blank=True,
        verbose_name=_('phone_number')
    )
    subject = models.CharField(
        max_length=255, null=True, blank=True,
        verbose_name=_('subject')
    )
    message = models.TextField(verbose_name=_('message'))
    is_read = models.BooleanField(default=False, verbose_name=_('is_read'))

    def __str__(self):
        return f"{self.name} | {self.email}"

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class StoreModel(BaseModel):
    image = models.ImageField(upload_to='stores/', verbose_name=_('image'))
    name = models.CharField(max_length=128, verbose_name=_('name'))
    address = models.CharField(max_length=128, verbose_name=_('address'))
    phone_number = models.CharField(max_length=13, verbose_name=_('phone_number'))
    working_hours = models.CharField(max_length=255, verbose_name=_('working_hours'))
    location_link = models.URLField(verbose_name=_('location_link'))
    picked = models.BooleanField(default=False, verbose_name=_('picked'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('store')
        verbose_name_plural = _('stores')