import gettext
import os
import pathlib


from babel.support import LazyProxy


INTERFACE_DIR = pathlib.Path(__file__).parent
LOCALES_DIR = INTERFACE_DIR.joinpath('locales')


class I18N:
    def __init__(self, domain, path=None, default='en'):
        if path is None:
            path = os.path.join(os.getcwd(), LOCALES_DIR)

        self.domain = domain
        self.path = path
        self.default = default

        self.locales = self.find_locales()

    def find_locales(self):
        translations = {}

        for name in os.listdir(self.path):
            if not os.path.isdir(os.path.join(self.path, name)):
                continue
            mo_path = os.path.join(
                self.path,
                name,
                'LC_MESSAGES',
                self.domain + '.mo',
            )

            if os.path.exists(mo_path):
                with open(mo_path, 'rb') as fp:
                    translations[name] = gettext.GNUTranslations(fp)
            elif os.path.exists(mo_path[:-2] + 'po'):
                raise RuntimeError(
                    f"Найден перевод '{name}', но "
                    f"этот перевод не скомпилирован"
                )

        return translations

    def reload(self):
        self.locales = self.find_locales()

    @property
    def available_locales(self):
        return tuple(self.locales.keys())

    def __call__(self, singular, plural=None, n=1, locale=None) -> str:
        return self.gettext(singular, plural, n, locale)

    def gettext(self, singular, plural=None, n=1, locale=None) -> str:
        if locale is None:
            locale = self.default

        if locale not in self.locales:
            if n == 1:
                return singular
            return plural

        translator = self.locales[locale]

        if plural is None:
            return translator.gettext(singular)
        return translator.ngettext(singular, plural, n)

    def lazy_gettext(
            self, singular, plural=None, n=1,
            locale=None, enable_cache=False
    ) -> LazyProxy:
        return LazyProxy(
            self.gettext, singular,
            plural, n, locale, enable_cache=enable_cache
        )
