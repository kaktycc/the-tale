
import smart_imports

smart_imports.all()


DEFAULT_TEXT = '''Здравствуйте!
Давайте дружить.'''


class RequestForm(dext_forms.Form):
    text = utils_bbcode.BBField(label='Сообщение', initial=DEFAULT_TEXT)
