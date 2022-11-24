from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Category, Product

@receiver(pre_save, sender=Category)
def create_category(sender, instance, *arg, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)


@receiver(pre_save, sender=Product)
def create_product(sender, instance, *arg, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)


def create_unique_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name, allow_unicode=True)

    instanceClass = instance.__class__
    qs = instanceClass.objects.filter(slug=slug)

    if qs.exists():
        new_slug = f"{slug}-{qs.first().id}"
        return create_unique_slug

    return slug
