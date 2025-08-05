from modeltranslation.translator import register, TranslationOptions, translator

from pages.models import StoreModel

@register(StoreModel)
class StoreModelTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'working_hours')
