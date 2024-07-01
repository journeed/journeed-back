from unidecode import unidecode

def custom_slugify(title):
    symbol_mapping = (
        (' ', '-'),
        ('.', '-'),
        (',', '-'),
        ('!', '-'),
        ('/', '-'),
        ('(', '-'),
        (')', '-'),
        ('?', '-'),
        ("'", '-'),
        ('"', '-'),
        ('ə', 'e'),
        ('ı', 'i'),
        ('İ', 'i'),
        ('i', 'i'),
        ('ö', 'o'),
        ('ğ', 'g'),
        ('ü', 'u'),
        ('ş', 's'),
        ('ç', 'c'),
    )
    title_url = title.strip().lower()

    for before, after in symbol_mapping:
        title_url = title_url.replace(before, after)

    return unidecode(title_url)


def unique_slug_generator(instance, slug_name, new_slug=None, old_slug=None, i=2):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = custom_slugify(slug_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists() if old_slug is None else Klass.objects.exclude(slug=old_slug).filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=custom_slugify(slug_name),
            randstr=i
        )
        a = i + 1
        return unique_slug_generator(instance, new_slug=new_slug, i=a)
    return slug
